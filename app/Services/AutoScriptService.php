<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\Utils\UEUploader;
use App\AutoScript;
use App\Utils\FileHelper;
use App\Utils\StringUtil;

class AutoScriptService {
	
	/**
	 * 根据父节点 获取脚本
	 *
	 * @param unknown $parentId        	
	 */
	public function getScriptByParent($parentId, $user) {
		return DB::select ( "SELECT id,intProjectID as pId,chrScriptName as name,'false' isParent,'testcase' as iconSkin
				FROM auto_scripts where intProjectID=$parentId and intCompanyID=$user->intCompanyID order by id desc" );
	}
	/**
	 * 根据父节点 获取脚本
	 *
	 * @param unknown $parentId        	
	 */
	public function getScriptByParentLimit($parentId, $user) {
		return DB::select ( "SELECT id FROM auto_scripts where intProjectID=$parentId and intCompanyID=$user->intCompanyID limit 1" );
	}
	
	/**
	 *
	 * @param unknown $user        	
	 * @param unknown $search        	
	 */
	private function getScriptCount($user, $search, $wl) {
		$res = DB::select ( "SELECT count(*) as allCount
				FROM auto_scripts aus
				inner join auto_projects aup on aup.id=aus.intProjectID
				inner join auto_projects apro on apro.id=aus.intTopProjectID
				inner join users u on u.id=aus.intCreaterID
				left JOIN (select DISTINCT intScriptID from auto_script_files)asf on asf.intScriptID=aus.id  
				where aus.intFlag=0 and aus.intCompanyID=$user->intCompanyID and $search $wl  order by aus.id desc" );
		return $res [0]->allCount;
	}
	/**
	 *
	 * @param unknown $search        	
	 */
	private function structureSearchSQL($search) {
		if (! empty ( $search )) {
			$sql = array ();
			/*
			 * $where = "aus.id='$nodeId'"; if ($isParent == "true")
			 */
			$isParent = empty ( $search ["isParent"] ) ? "" : $search ["isParent"];
			$nodeId = empty ( $search ["nodeId"] ) ? "" : $search ["nodeId"];
			$scriptName = trim ( $search ["scriptName"] );
			$uploadArgs = $search ["uploadArgs"];
			$uploadNeeds = $search ["uploadNeeds"];
			$creater = trim ( $search ["creater"] );
			if ($nodeId) {
				array_push ( $sql, "(aup.intParentID='$nodeId' or aup.id='$nodeId')" );
			}
			if ($scriptName)
				array_push ( $sql, "aus.chrScriptName='$scriptName'" );
			if ($scriptName)
				array_push ( $sql, "aus.chrScriptName='$scriptName'" );
			if ($uploadArgs)
				array_push ( $sql, "aus.intParamAttID is not null" );
			else if ($uploadArgs !== "")
				array_push ( $sql, "aus.intParamAttID is null" );
			if ($uploadNeeds)
				array_push ( $sql, "asf.intScriptID is not null" );
			else if ($uploadNeeds !== "")
				array_push ( $sql, "asf.intScriptID is null" );
			if ($creater)
				array_push ( $sql, "u.chrUserName='$creater'" );
			$sql = implode ( " and ", $sql );
		}
		if (empty ( $sql ))
			$sql = "1=1";
		return $sql;
	}
	
	/**
	 * 根据父节点 获取脚本json
	 *
	 * @param unknown $parentId        	
	 */
	public function getScriptJsonByParent($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl) {
		$search = $this->structureSearchSQL ( $search );
		$allcount = $this->getScriptCount ( $user, $search, $wl );
		$scripts = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$pagecount = $iDisplayStart;
		$rows = DB::select ( "SELECT aus.id,chrScriptName as scriptName,aup.chrProjectName as productName,apro.chrProjectName projectName ,asr.intAttID attId,
				u.chrUserName as userName,case when aus.intParamAttID is null THEN '否' else '是' end param,
				case when asf.intScriptID is null THEN '否' else '是' end files,CONCAT('V',asr.intVersion) version
				FROM auto_scripts aus
				inner join auto_projects aup on aup.id=aus.intProjectID
				inner join auto_projects apro on apro.id=aus.intTopProjectID
				inner join users u on u.id=aus.intCreaterID
				inner JOIN auto_script_relations asr on asr.intScriptID=aus.id and asr.intFlag=0
				left JOIN (select DISTINCT intScriptID from auto_script_files)asf on asf.intScriptID=aus.id  
				where aus.intFlag=0 and aus.intCompanyID=$user->intCompanyID and $search $wl order by aus.id desc limit ?,?", [ 
				$pagecount,
				$iDisplayLength 
		] );
		$scripts .= json_encode ( $rows );
		$scripts .= "}";
		return $scripts;
	}
	
	/**
	 *
	 * @param unknown $action        	
	 * @param unknown $CONFIG        	
	 * @return Ambigous <multitype:, multitype:Ambigous <number, unknown> string Ambigous <string, unknown> Ambigous <string, multitype:string > >
	 */
	public function uploadfile($action, $CONFIG, $tmpStore) {
		$config = array (
				"pathFormat" => $CONFIG ['filePathFormat'],
				"maxSize" => $CONFIG ['fileMaxSize'],
				"allowFiles" => $CONFIG ['fileAllowFiles'],
				"tmpStore" => $CONFIG ['tmpStore'] 
		);
		$formName = $CONFIG ['fileFieldName'];
		/* 生成上传实例对象并完成上传 */
		$up = new UEUploader ( $formName, $config, $tmpStore );
		/**
		 * 得到上传文件所对应的各个参数,数组结构
		 * array(
		 * "state" => "", //上传状态，上传成功时必须返回"SUCCESS"
		 * "url" => "", //返回的地址
		 * "title" => "", //新文件名
		 * "original" => "", //原始文件名
		 * "type" => "" //文件类型
		 * "size" => "", //文件大小
		 * )
		 */
		
		/* 返回数据 */
		return $up->getFileInfo ();
	}
	
	/**
	 * 读取脚本内容 每次读完再不改变内容的情况下 存储到缓存中
	 *
	 * @param unknown $id        	
	 */
	public function readScriptContent($id, $user) {
		$rows = DB::select ( "select chrFile from sys_attachments satt
				inner JOIN auto_script_relations asr on asr.intAttID=satt.id
				where asr.intFlag=0 and asr.intScriptID=$id and asr.intCompanyID=$user->intCompanyID" );
		if (! empty ( $rows )) {
			$file = base_path () . $rows [0]->chrFile;
			$file = StringUtil::iconv ( $file );
			return FileHelper::readfile_fgets ( $file );
		}
	}
	
	/**
	 * 获取脚本的历史文件
	 *
	 * @param unknown $scriptId        	
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 */
	public function getAnnalsScriptList($scriptId, $attId, $secho, $iDisplayStart, $iDisplayLength) {
		$res = DB::select ( "select count(*) as allCount from auto_script_relations 
				where intAttID not in ($attId)  and intScriptID=$scriptId" );
		$allcount = $res [0]->allCount;
		$annals = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select satt.id,asr.id relateId,asr.intScriptID scriptId,satt.chrFileName fileName,uc.chrUserName creUserName,
				um.chrUserName modUserName,asr.created_at,asr.updated_at,CONCAT('V',asr.intVersion) version,chrBackMemo backMemo
				from auto_script_relations asr 
				inner join sys_attachments satt on satt.id=asr.intAttID
				INNER JOIN users uc on uc.id=asr.intCreaterID
				INNER JOIN users um on um.id=asr.intModifyID
				LEFT JOIN (select intScriptRelateID,chrBackMemo from auto_script_back_logs 
				where id in (select MAX(id) from auto_script_back_logs GROUP BY intScriptRelateID))back on back.intScriptRelateID=asr.id
				where asr.intAttID not in ($attId) and asr.intScriptID=$scriptId 
				order by satt.id desc limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$annals .= json_encode ( $rows );
		$annals .= "}";
		return $annals;
	}
	
	/**
	 *
	 * @param unknown $attId        	
	 */
	public function getScriptText($attId) {
		$rows = DB::select ( "select chrFile,CONCAT('V',asr.intVersion) version 
				from sys_attachments satt
				INNER JOIN auto_script_relations asr on asr.intAttID=satt.id where satt.id =$attId" );
		$file = $rows [0]->chrFile;
		$filename = base_path () . $file;
		$filename = StringUtil::iconv ( $filename );
		$script = array (
				"version" => $rows [0]->version 
		);
		if (file_exists ( $filename )) {
			$content = FileHelper::readfile_fgets ( $filename );
			$script ["content"] = $content;
		}
		return $script;
	}
	
	/**
	 *
	 * @param unknown $attId        	
	 * @param unknown $nowAttId        	
	 * @param unknown $scriptId        	
	 */
	public function rollBack($attId, $nowAttId, $scriptId, $backMemo, $user) {
		DB::beginTransaction ();
		try {
			$rows = DB::select ( "select id,intVersion from auto_script_relations where intAttID=$attId
					union all
					select id,intVersion from auto_script_relations where intAttID=$nowAttId" );
			$relateId = $rows [0]->id;
			$version = $rows [0]->intVersion;
			$nowVersion = $rows [1]->intVersion;
			$nowRelateId = $rows [1]->id;
			
			$sysMemo = $user->chrUserName . "于" . date ( "Y-m-d H:i:s", time () ) . "从V" . $nowVersion . "版本回滚到V" . $version . "版本：" . $backMemo;
			// $nowSysMemo = $user->chrUserName . "于" . date ( "Y-m-d H:i:s", time () ) . "将V" . $nowVersion . "版本替换掉，当前应用版本为V" . $version . "版本：" . $backMemo;
			DB::insert ( "insert into auto_script_back_logs (intScriptID,intScriptRelateID,chrBackMemo,intCreaterID,intMain)
					values (?,?,?,?,1),(?,?,?,?,0)", [ 
					$scriptId,
					$relateId,
					$sysMemo,
					$user->id,
					$scriptId,
					$nowRelateId,
					$sysMemo,
					$user->id 
			] );
			DB::update ( "update auto_script_relations set intFlag=0 where intScriptID=$scriptId and intAttID=$attId and intFlag=1" );
			DB::update ( "update auto_script_relations set intFlag=1 where intScriptID=$scriptId and intAttID=$nowAttId and intFlag=0" );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $scriptId        	
	 */
	public function getScriptBackLogList($secho, $iDisplayStart, $iDisplayLength, $scriptId) {
		$res = DB::select ( "select count(*) allCount from auto_script_back_logs where intMain=1 and intScriptID=$scriptId" );
		$allcount = $res [0]->allCount;
		$blogs = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select chrBackMemo backMemo,created_at from auto_script_back_logs 
				where intMain=1 and intScriptID=$scriptId ORDER BY id desc  limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$blogs .= json_encode ( $rows );
		$blogs .= "}";
		return $blogs;
	}
	
	/**
	 *
	 * @param unknown $scriptId        	
	 * @param unknown $scriptRelateId        	
	 */
	public function getScriptVerBackLogList($secho, $iDisplayStart, $iDisplayLength, $scriptId, $scriptRelateId) {
		$res = DB::select ( "select count(*) allCount from auto_script_back_logs 
				where intMain=1 and intScriptID=$scriptId and intScriptRelateID=$scriptRelateId" );
		$allcount = $res [0]->allCount;
		$blogs = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select chrBackMemo backMemo,created_at from auto_script_back_logs 
				where intMain=1 and intScriptID=$scriptId and intScriptRelateID=$scriptRelateId 
				ORDER BY id desc limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$blogs .= json_encode ( $rows );
		$blogs .= "}";
		return $blogs;
	}
	
	/**
	 *
	 * @param unknown $script        	
	 * @param unknown $user        	
	 */
	public function insert($scriptPath, $script, $user) {
		$companyID = $user->intCompanyID;
		DB::beginTransaction ();
		try {
			$auto_script = new AutoScript ();
			$rows = DB::select ( "select ass.id,intParamAttID,satt.chrFile,satt.chrFileName,
					satt.chrFileType,asr.intAttID,asr.intVersion from auto_scripts ass
					INNER JOIN auto_script_relations asr on asr.intScriptID=ass.id
					INNER JOIN sys_attachments satt on satt.id=asr.intAttID
					where asr.intFlag=0 and chrScriptName=? and intProjectID=? and ass.intCompanyID=?", [ 
					$script ["scriptName"],
					$script ["productId"],
					$companyID 
			] );
			$scriptId = 0;
			$vsersion = 1;
			if (empty ( $rows )) { // 若脚本不存在 插入脚本
				$oldname = $auto_script->chrScriptName = $script ["scriptName"];
				$auto_script->intProjectID = $script ["productId"];
				$auto_script->intTopProjectID = $script ["projectId"];
				$auto_script->intCreaterID = $auto_script->intModifyID = $user->id;
				$auto_script->intCompanyID = $companyID;
				$auto_script->save ();
				$scriptId = $auto_script->id;
				$oldname .= $script ["type"];
			} else { // 若存在 则逻辑删除脚本附件关联信息 同时将脚本更改原脚本的名称 用于脚本回滚
				$auto_script = $rows [0];
				$scriptId = $auto_script->id;
				$vsersion = intval ( $auto_script->intVersion ) + 1;
				DB::update ( "update auto_script_relations set intFlag=1,intModifyID=?
						where intScriptID=? and intFlag=0", [ 
						$user->id,
						$scriptId 
				] );
				// 原文件名
				$oldname = $auto_script->chrFileName;
				$oldfile = $auto_script->chrFile; // 原文件具体路径（包含具体文件名）
				$bakDir = str_replace ( $oldname, "worm_" . time (), $oldfile );
				@mkdir ( StringUtil::iconv ( base_path () . $bakDir ), 0777, true );
				$newfile = $bakDir . "/" . $oldname; // 新文件的具体路径
				FileHelper::rename ( base_path () . $oldfile, base_path () . $newfile ); // 将原先存在的脚本名称更改
				DB::update ( "update sys_attachments set chrFile=? where id=?", [ 
						$newfile,
						$auto_script->intAttID 
				] ); // 将存储在数据库中的文件信息更改备份
			}
			$oldfile = $script ["file"];
			$this->changeScriptAttach ( $scriptPath, $oldname, $oldfile, $script ["attId"] );
			DB::insert ( "insert into auto_script_relations (intScriptID,intAttID,intCreaterID,intModifyID,intVersion,intCompanyID) 
					values (?,?,?,?,?,?)", [ 
					$scriptId,
					$script ["attId"],
					$user->id,
					$user->id,
					$vsersion,
					$companyID 
			] );
			/*
			 * $redis = RedisHelper::getInstance (); $projectId = $script ["projectId"]; $key = "script.day.company" . $companyID; $date = date ( 'Y-m-d', time () ); $redis->hIncrBy ( $key, $date, 1 ); $key = "script.day.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "W", time () ); $key = "script.week.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "script.week.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "m", time () ); $key = "script.mon.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "script.mon.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 );
			 */
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 * 改变脚本附件最终的存放地址以及数据库的存放地址
	 *
	 * @param unknown $scriptPath
	 *        	最终存放的目录
	 * @param unknown $oldname
	 *        	原文件名称
	 * @param unknown $oldfile
	 *        	原文件的具体路径（包含具体文件）
	 * @param unknown $newfile
	 *        	新文件的具体路径（包含具体文件）
	 */
	private function changeScriptAttach($scriptPath, $oldname, $oldfile, $attId) {
		$dest = base_path () . $scriptPath;
		$newfile = $scriptPath . $oldname;
		$dest = iconv ( 'UTF-8', 'gbk', $dest );
		@mkdir ( $dest, 0777, true );
		$oldpath = base_path () . $oldfile . "tmp";
		// 将上传的临时文件 拷贝到自动化目录下
		FileHelper::rename ( $oldpath, base_path () . $newfile );
		$index = strrpos ( $oldpath, "/" );
		FileHelper::resource_remove ( substr ( $oldpath, 0, $index ) );
		DB::update ( "update sys_attachments set chrFile=? where id =?", [ 
				$newfile,
				$attId 
		] );
	}
	
	/**
	 * 删除
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids, $user) {
		DB::beginTransaction ();
		try {
			DB::delete ( "delete from auto_scripts where id in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::delete ( "delete from auto_script_relations where intScriptID in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 * 修改脚本参数化文件关联关系
	 *
	 * @param unknown $script        	
	 */
	public function updateParams($scriptPath, $script, $user) {
		DB::beginTransaction ();
		try {
			$this->changeScriptAttach ( $scriptPath, $script ["filename"], $script ["file"], $script ["attId"] );
			DB::update ( "update auto_scripts set intParamAttID=? where id=?", [ 
					$script ["attId"],
					$script ["scriptId"] 
			] );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $$filePath        	
	 * @param unknown $script        	
	 */
	public function updateFiles($filePath, $script, $user) {
		DB::beginTransaction ();
		try {
			$this->changeScriptAttach ( $filePath, $script ["filename"], $script ["file"], $script ["attId"] );
			DB::insert ( "insert into auto_script_files (intScriptID,intAttID,intCompanyID) values (?,?,?)", [ 
					$script ["scriptId"],
					$script ["attId"],
					$user->intCompanyID 
			] );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 * 根据脚本Id获取产品id
	 *
	 * @param unknown $scriptId        	
	 */
	public function getProjectByScriptId($scriptId, $user) {
		$rows = DB::select ( "select intProjectID from auto_scripts where id=$scriptId and intCompanyID=$user->intCompanyID" );
		return $rows [0]->intProjectID;
	}
	
	/**
	 *
	 * @param unknown $id        	
	 * @param unknown $content        	
	 */
	public function updateScriptContent($id, $content, $user) {
		$rows = DB::select ( "select satt.id,satt.chrFile,satt.chrFileName from auto_script_relations asr
				INNER JOIN sys_attachments satt on satt.id=asr.intAttID
				where asr.intFlag=0 and intScriptID=$id and asr.intCompanyID=$user->intCompanyID" );
		foreach ( $rows as $row ) {
			$file = base_path () . $row->chrFile;
			FileHelper::writefile_fopen ( StringUtil::iconv ( $file ), $content );
		}
	}
}

?>