<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\Utils\FileHelper;
use App\SysFlow;
use App\AutoScheme;
use App\Utils\XMLHelper;
use App\Utils\StringUtil;
use App\Utils\ZipArchiveHelper;
use App\AutoTask;
use App\AutoTaskRelation;

class AutoSchemeService {
	
	/**
	 * 获取案例总数
	 */
	private function getSchemeCount($user, $search, $wl) {
		$res = DB::select ( "select COUNT(*) allcount from auto_schemes aus
				INNER JOIN users u on u.id=aus.intCreaterID
				INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
				INNER JOIN auto_tasks ats on ats.id=atr.intTaskID and ats.intTaskType=1
				LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intFlag=0 and ate.intTimerTaskID=0 and ate.intCreaterID=$user->id
				LEFT JOIN auto_projects apro on apro.id=ats.intProjectID
				where aus.intFlag=0 and aus.intCompanyID=$user->intCompanyID and $search $wl" );
		return $res [0]->allcount;
	}
	/**
	 *
	 * @param unknown $search        	
	 */
	private function structureSearchSQL($search) {
		if (! empty ( $search )) {
			$sql = array ();
			$projectId = $search ["projectId"];
			$state = $search ["state"];
			$schemeName = trim ( $search ["schemeName"] );
			$creater = trim ( $search ["creater"] );
			if ($projectId) {
				array_push ( $sql, "ats.intProjectID=$projectId" );
			}
			if ($state === "") {
				array_push ( $sql, "ate.intState is NULL" );
			} else if ($state >= 0)
				array_push ( $sql, "ate.intState=$state" );
			if ($schemeName)
				array_push ( $sql, "aus.chrSchemeName='$schemeName'" );
			if ($creater)
				array_push ( $sql, "u.chrUserName='$creater'" );
			$sql = implode ( " and ", $sql );
		}
		if (empty ( $sql ))
			$sql = "1=1";
		return $sql;
	}
	/**
	 * 获取案例列表
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 * @return string
	 */
	public function getSchemeList($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl) {
		$search = $this->structureSearchSQL ( $search );
		$allcount = $this->getSchemeCount ( $user, $search, $wl );
		$schemes = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select DISTINCT aus.id,chrSchemeName schemeName,u.chrUserName createUser,ate.id taskExecID,ate.chrBrowserNames browserNames,
				case when ate.intState=0 then '排队中' when ate.intState=1 then '执行中' when ate.intState=2 then '执行成功' 
				when ate.intState=3 then '执行失败' else '未执行' end state,ats.intProjectID projectId,apro.chrProjectName projectName
				from auto_schemes aus
				INNER JOIN users u on u.id=aus.intCreaterID
				INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
				INNER JOIN auto_tasks ats on ats.id=atr.intTaskID and ats.intTaskType=1
				LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intFlag=0 and ate.intTimerTaskID=0 and ate.intCreaterID=$user->id
				LEFT JOIN auto_projects apro on apro.id=ats.intProjectID
				where aus.intFlag=0 and aus.intCompanyID=$user->intCompanyID and $search $wl order by aus.id desc limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$schemes .= json_encode ( $rows );
		$schemes .= "}";
		return $schemes;
	}
	
	/**
	 *
	 * @param unknown $id        	
	 */
	private function getSchemeProcess($id, $user) {
		$sql = "select sfp.id,ats.intProjectID,ausr.intFlowID,aus.id schemeID,aus.chrSchemeName,ass.chrScriptName,ass.id scriptID,
		atts.chrFile scriptFile,atts.chrFileName sfileName,attp.chrFile scriptParam,attp.chrFileName spfileName,chrProcessName,
		chrProcessStyle,chrProcessType,case when chrProcessTo is null then '' else chrProcessTo end chrProcessTo
		from auto_schemes aus
		INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
		INNER JOIN auto_tasks ats on ats.id=atr.intTaskID and ats.intTaskType=1
		INNER JOIN auto_scheme_relations ausr on ausr.intSchemeID=aus.id
		LEFT JOIN sys_flow_processes sfp on sfp.intFlowID=ausr.intFlowID and sfp.intFlag=0
		LEFT JOIN auto_scripts ass on ass.id=sfp.intRelationID
		LEFT JOIN auto_script_relations asr on asr.intScriptID=ass.id and asr.intFlag=0
		LEFT JOIN sys_attachments atts on atts.id=asr.intAttID
		LEFT JOIN sys_attachments attp on attp.id=ass.intParamAttID
		where aus.id=$id and aus.intCompanyID=$user->intCompanyID";
		return DB::select ( $sql );
	}
	
	/**
	 *
	 * @param unknown $id        	
	 */
	public function getSchemeFlowProcess($id, $user) {
		$rows = $this->getSchemeProcess ( $id, $user );
		$index = 0;
		$processData = array ();
		foreach ( $rows as $row ) {
			if (! empty ( $row->id )) {
				$processData ["list"] [$index] = array (
						"id" => $row->id,
						"flow_id" => $row->intFlowID,
						"process_name" => $row->chrScriptName,
						"process_to" => $row->chrProcessTo,
						"icon" => ($row->chrProcessType ? "icon-star" : "icon-ok"),
						"style" => $row->chrProcessStyle 
				);
			}
			$index ++;
		}
		$processData ["total"] = -- $index;
		$processData ["flowid"] = (empty ( $rows ) ? 0 : $rows [0]->intFlowID);
		$processData ["projectId"] = (empty ( $rows ) ? 0 : $rows [0]->intProjectID);
		return $processData;
	}
	
	/**
	 * 获取结束节点
	 *
	 * @param unknown $rows        	
	 */
	private function getEndNode(& $rows) {
		$endNodes = array ();
		foreach ( $rows as $key => $row ) {
			if (empty ( $row->chrProcessTo ) && $row->id) {
				$endNodes [] = $row;
				// unset ( $rows [$key] );
			}
		}
		return $endNodes;
	}
	
	/**
	 * 获取开始节点
	 *
	 * @param unknown $rows        	
	 */
	private function getBeginNode($rows) {
		$beginNodes = array ();
		foreach ( $rows as $row ) {
			$nodeId = $row->id;
			$begin = true;
			foreach ( $rows as $rowTo ) {
				$nodeTo = $rowTo->chrProcessTo;
				if (stripos ( $nodeTo, strval ( $nodeId ) ) !== false) {
					$begin = false;
					break;
				}
			}
			if ($begin) {
				$beginNodes [] = $row;
			}
		}
		return $beginNodes;
	}
	
	/**
	 * 获取依赖节点
	 *
	 * @param unknown $line        	
	 */
	private function getReferNodes($cid, $rows, $models, $index, & $line) {
		try {
			foreach ( $rows as $key => $row ) {
				$fid = $row->id;
				$pto = $row->chrProcessTo;
				$ptos = explode ( ",", $pto );
				foreach ( $ptos as $pto ) {
					if ($cid == $pto) {
						$sekey = array_search ( $fid, $line );
						if ($sekey !== false) {
							array_splice ( $line, $sekey, 1 );
						}
						array_unshift ( $line, $fid );
					}
				}
				unset ( $rows [$key] );
				array_filter ( $rows );
				if (count ( $rows ) == 0 && $index < count ( $models )) {
					$index ++;
					$this->getReferNodes ( $line [0], $models, $models, $index, $line );
				}
			}
		} catch ( \Exception $e ) {
			throw $e;
		}
	}
	
	/**
	 * 生成案例下载包
	 *
	 * @param unknown $id        	
	 */
	public function makeSchemePackage($id, $selBrowsers, $allBrowsers, $user) {
		$rows = $this->getSchemeProcess ( $id, $user );
		$endNodes = $this->getEndNode ( $rows );
		if (! empty ( $endNodes )) {
			foreach ( $endNodes as $endNode ) {
				$endNodeId = $endNode->id;
				$line = array (
						$endNodeId 
				);
				$this->getReferNodes ( $endNodeId, $rows, $rows, 1, $line );
				$lines [] = array_filter ( $line );
			}
			$schemeName = $rows [0]->chrSchemeName;
			$root = database_path ( "schemes" );
			$resource = $root . DIRECTORY_SEPARATOR . "easyTest";
			$dest = $root . DIRECTORY_SEPARATOR . $schemeName;
			$resource = StringUtil::iconv ( $resource );
			$dest = StringUtil::iconv ( $dest );
			// 不拷贝文件夹下的文件 但是会创建响应的文件夹
			$nodirs = array (
					"common", // 下载时拷贝
					"config", // 案例保存时生成
					"data", // 下载时拷贝
					"files", // 下载时拷贝
					"testCase", // 下载时拷贝
					"SRC"  // 下载时再拷贝
						);
			FileHelper::resource_copy ( $resource, $dest, $nodirs, false, array (
					"use.py" 
			) ); // 参照拷贝生成一份新的案例
			$bowsers = array ();
			foreach ( $allBrowsers as $allBrowser ) {
				if (in_array ( $allBrowser->id, $selBrowsers )) {
					array_push ( $bowsers, $allBrowser->browserENName );
				}
			}
			foreach ( $nodirs as $nodir ) {
				FileHelper::resource_remove ( $dest . "/script/" . $nodir, false );
			}
			$schemeName = StringUtil::iconv ( $schemeName );
			$this->updateSchemeConfig ( $rows, $lines, $resource, $dest, $id, $schemeName, $bowsers );
			/*
			 * $zipname = $root . DIRECTORY_SEPARATOR . "zips" . DIRECTORY_SEPARATOR . $rows [0]->schemeID . ".zip"; // zip具体路径 ZipArchiveHelper::openZip ( $zipname ); // 创建并打开zip ZipArchiveHelper::addFileToZip ( $dest, strlen ( $root ) + 1 ); // 将文件夹压缩zip ZipArchiveHelper::closeZip (); // 关闭zip
			 */
		}
	}
	/**
	 *
	 * @param unknown $schemeId        	
	 * @return boolean
	 */
	public function makeSchemeZip($schemeId, $user) {
		$rows = DB::select ( "select chrSchemeName from auto_schemes where id =$schemeId and intCompanyID=$user->intCompanyID" );
		if (! empty ( $rows )) {
			$root = database_path ( "schemes/" );
			$easyTest = $root . "easyTest";
			$scripts = $this->getSchemeProcess ( $schemeId, $user );
			$dest = $root . DIRECTORY_SEPARATOR . StringUtil::iconv ( $rows [0]->chrSchemeName );
			foreach ( $scripts as $script ) {
				$scriptFile = $script->scriptFile; // 存储在服务器上的具体相对路径
				$sfileName = $script->sfileName; // 文件名称
				$scriptParam = $script->scriptParam; // 脚本参数的相对路径
				$spfileName = $script->spfileName;
				$scriptId = $script->scriptID;
				// 下载时 拷贝案例包含的脚本文件：脚本、脚本参数、脚本图片 即"testCase","data","files",文件夹下的文件
				$this->copyScriptFiles ( $easyTest, $dest, $scriptFile, $sfileName, $scriptParam, $spfileName, $scriptId, true );
			}
			$scriptCommon = "/script/common";
			FileHelper::resource_copy ( $easyTest . $scriptCommon, $dest . $scriptCommon, array (), false ); // 拷贝脚本下的common
			$src = "/SRC";
			FileHelper::resource_copy ( $easyTest . $src, $dest . $src, array (), false ); // 拷贝SRC
			$zipname = $root . DIRECTORY_SEPARATOR . "zips" . DIRECTORY_SEPARATOR . $schemeId . ".zip"; // zip具体路径
			ZipArchiveHelper::openZip ( $zipname ); // 创建并打开zip
			ZipArchiveHelper::addFileToZip ( $dest, strlen ( $root ) + 1 ); // 将文件夹压缩zip
			ZipArchiveHelper::closeZip (); // 关闭zip
			return true;
		}
		return false;
	}
	
	/**
	 *
	 * @param unknown $rows        	
	 * @param unknown $lines        	
	 * @param unknown $root        	
	 * @param unknown $schemeName        	
	 */
	private function updateSchemeConfig($rows, $lines, $resource, $dest, $id, $schemeName, $bowsers) {
		$configDir = "/script/config/";
		$oldname = $resource . $configDir . "demo.xml";
		$newname = $resource . $configDir . "$schemeName.xml";
		copy ( $oldname, $newname );
		$doc = XMLHelper::openDoc ( $newname );
		$nodeList = XMLHelper::getNodeList ( $doc, "hub" );
		foreach ( $nodeList as $node ) {
			$attrValue = XMLHelper::getNodeAttrValue ( $node, "browser" );
			if (in_array ( $attrValue, $bowsers )) {
				XMLHelper::setNodeAttr ( $node, "enabled", "True" );
			}
		}
		foreach ( $lines as $line ) {
			$newNode = XMLHelper::createNode ( $doc, "catalog", "scene" );
			XMLHelper::setNodeAttr ( $newNode, "description", "脚本执行顺序为子标签排列顺序" );
			XMLHelper::setNodeAttr ( $newNode, "schemeId", $id );
			foreach ( $line as $lin ) {
				foreach ( $rows as $row ) {
					if ($lin == $row->id) {
						$scriptFile = $row->scriptFile; // 存储在服务器上的具体相对路径
						$sfileName = $row->sfileName; // 文件名称
						$scriptParam = $row->scriptParam; // 脚本参数的相对路径
						$spfileName = $row->spfileName;
						$scriptId = $row->scriptID;
						// 下载时 拷贝案例包含的脚本文件：脚本、脚本参数、脚本图片 即"testCase","data","files",文件夹下的文件
						$paths = $this->copyScriptFiles ( $resource, $dest, $scriptFile, $sfileName, $scriptParam, $spfileName, $scriptId );
						// 写入xml文件
						$childNode = XMLHelper::createChildNode ( $doc, $newNode, "testCase", StringUtil::iconv_UTF ( $paths ["proDir"] ) . $row->sfileName );
						XMLHelper::setNodeAttr ( $childNode, "paramPath", $paths ["relaScriptParam"] );
						XMLHelper::setNodeAttr ( $childNode, "enabled", "True" );
						XMLHelper::setNodeAttr ( $childNode, "scriptId", $scriptId ); // 脚本ID
						break;
					}
				}
			}
		}
		XMLHelper::save ( $doc, $newname );
		$destfile = $dest . $configDir . "$schemeName.xml";
		copy ( $newname, $destfile ); // 拷贝案例配置文件xml
		$runfile = $dest . DIRECTORY_SEPARATOR . "script" . DIRECTORY_SEPARATOR . "runTest.py";
		$schemeName = iconv ( "gbk", "UTF-8", $schemeName );
		FileHelper::writefile_fopen ( $runfile, "Main('$schemeName.xml').run()", "a" );
	}
	
	/**
	 *
	 * @param unknown $resource
	 *        	"D:\ApacheAppServ\www\testworm\database\schemes\easyTest"
	 * @param unknown $dest
	 *        	"D:\ApacheAppServ\www\testworm\database\schemes\案例名称"
	 * @param unknown $scriptFile
	 *        	/database/schemes/easyTest/script/testCase/U商城/公共脚本/登录.py
	 * @param unknown $scriptParam        	
	 * @param unknown $scriptId        	
	 */
	public function copyScriptFiles($resource, $dest, $scriptFile, $sfileName, $scriptParam, $spfileName, $scriptId, $copy = false) {
		$replace_path = "/database/schemes/easyTest";
		$testCaseDir = "/script/testCase/";
		$dataDir = "/script/data/";
		$filesDir = "/script/files/";
		$resFileDir = $resource . $filesDir . $scriptId;
		$destFileDir = $dest . $filesDir . $scriptId; // 每个脚本图片存放位置
		$relaScriptFile = str_replace ( $replace_path . $testCaseDir, "", $scriptFile ); // 相对script下的路径
		$relaScriptParam = str_replace ( $replace_path . $dataDir, "", $scriptParam );
		// 脚本相对路径 $relaScriptFile 如：U商城/公共脚本/1476776974/
		$destScriptDir = $resourceFileDir = StringUtil::iconv ( str_replace ( $sfileName, "", $relaScriptFile ) );
		$pathinfo = pathinfo ( $destScriptDir );
		if (strrpos ( $destScriptDir, "worm_" ) === false)
			$proDir = $destScriptDir;
		else
			$proDir = $pathinfo ["dirname"] . "/";
		$destCaseDir = $dest . $testCaseDir . $proDir;
		// 参数
		$destParamDir = $resourceParamDir = StringUtil::iconv ( str_replace ( $spfileName, "", $relaScriptParam ) );
		if ($copy) {
			FileHelper::resource_copy ( $resFileDir, $destFileDir ); // 将脚本所需要的图片拷贝到指定位置
			@mkdir ( $destCaseDir, 0777, true );
			$destDataDir = $dest . $dataDir . $destParamDir; // 目标参数位置
			@mkdir ( $destDataDir, 0777, true );
			// 拷贝具体的脚本
			copy ( $resource . $testCaseDir . $resourceFileDir . StringUtil::iconv ( $sfileName ), $destCaseDir . StringUtil::iconv ( $sfileName ) );
			$dspfile = $resource . $dataDir . $resourceParamDir . StringUtil::iconv ( $spfileName );
			if (is_file ( $dspfile ))
				// 拷贝具体的参数化文件
				copy ( $resource . $dataDir . $resourceParamDir . StringUtil::iconv ( $spfileName ), $destDataDir . StringUtil::iconv ( $spfileName ) );
		}
		return array (
				"proDir" => $proDir,
				"relaScriptParam" => $relaScriptParam 
		);
	}
	
	/**
	 * 新增案例
	 *
	 * @param unknown $schemes        	
	 * @param unknown $user        	
	 * @throws Exception
	 * @return unknown
	 */
	public function insert($schemes, $user) {
		DB::beginTransaction ();
		try {
			$flow = new SysFlow ();
			$auto_scheme = new AutoScheme ();
			$flow->chrFlowName = $auto_scheme->chrSchemeName = $schemes ["schemeName"];
			$flow->intCreaterID = $flow->intModifyID = $auto_scheme->intCreaterID = $auto_scheme->intModifyID = $user->id;
			$flow->intFlowType = 1;
			$flow->intCompanyID = $user->intCompanyID;
			$flow->save ();
			$flowId = $flow->id;
			$auto_scheme->intFlag = 1;
			$auto_scheme->intCompanyID = $user->intCompanyID;
			$auto_scheme->save ();
			$schemeId = $auto_scheme->id;
			DB::insert ( "insert into auto_scheme_relations (intSchemeID,intFlowID,intCompanyID) values (?,?,?)", [ 
					$schemeId,
					$flowId,
					$user->intCompanyID 
			] );
			// 生成一条虚拟任务
			$auto_task = new AutoTask ();
			$auto_task->chrTaskName = $schemes ["schemeName"];
			$auto_task->intTaskType = 1;
			$auto_task->intCreaterID = $auto_task->intModifyID = $user->id;
			$auto_task->intCompanyID = $user->intCompanyID;
			$auto_task->save ();
			$taskId = $auto_task->id;
			$auto_task_rel = new AutoTaskRelation ();
			$auto_task_rel->intTaskID = $taskId;
			$auto_task_rel->intSchemeID = $schemeId;
			$auto_task_rel->intCreaterID = $auto_task_rel->intModifyID = $user->id;
			$auto_task_rel->intCompanyID = $user->intCompanyID;
			$auto_task_rel->save ();
			DB::commit ();
			return $schemeId;
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $projectId        	
	 */
	public function update($projectId, $id, $user) {
		DB::beginTransaction ();
		try {
			DB::update ( "update auto_schemes set intFlag=0 where id=$id and intCompanyID=$user->intCompanyID" );
			DB::update ( "update auto_tasks set intProjectID=$projectId where id in (
			select intTaskID from auto_task_relations where intSchemeID=$id and intTaskType=1 and intCompanyID=$user->intCompanyID)" );
			$companyID = $user->intCompanyID;
			/*
			 * $redis = RedisHelper::getInstance (); $key = "scheme.day.company" . $companyID; $date = date ( 'Y-m-d', time () ); $redis->hIncrBy ( $key, $date, 1 ); $key = "scheme.day.product" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "W", time () ); $key = "scheme.week.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "scheme.week.product" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "m", time () ); $key = "scheme.mon.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "scheme.mon.product" . $companyID; $redis->hIncrBy ( $key, $date, 1 );
			 */
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids, $user) {
		$flows = DB::select ( "select asch.id schemeId,intFlowID,asch.chrSchemeName,ats.id as taskId 
				from auto_scheme_relations asr
				INNER JOIN auto_schemes asch on asch.id=asr.intSchemeID
				INNER JOIN auto_task_relations atr on atr.intSchemeID=asch.id
				INNER JOIN auto_tasks ats on ats.id=atr.intTaskID and ats.intTaskType=1
				where asr.intSchemeID in ($ids) and asch.intCompanyID=$user->intCompanyID" );
		$flowIds = ""; // 流程ID
		$taskIds = "";
		foreach ( $flows as $flow ) {
			$flowIds .= $flow->intFlowID . ",";
			$taskIds .= $flow->taskId . ",";
		}
		$flowIds = substr ( $flowIds, 0, - 1 );
		$taskIds = substr ( $taskIds, 0, - 1 );
		$process = DB::select ( "select id from sys_flow_processes where intFlowID in ($flowIds) and intCompanyID=$user->intCompanyID" );
		$processIds = 0;
		foreach ( $process as $pro )
			$processIds .= $pro->id . ",";
		if ($process)
			$processIds = substr ( $processIds, 0, - 1 );
		DB::beginTransaction ();
		try {
			// 根据查询的数据删除相关
			// 删除步骤相关
			DB::delete ( "delete from sys_flow_pro_relations where intProcessID in ($processIds)" );
			DB::delete ( "delete from sys_flow_processes where id in ($processIds)" );
			// 删除流程相关
			DB::delete ( "delete from sys_flows where id in ($flowIds)" );
			// 删除虚拟任务相关
			DB::delete ( "delete from auto_task_execs where intTimerTaskID=0 and intTaskID in ($taskIds)" );
			DB::delete ( "delete from auto_task_relations where intTaskID in ($taskIds)" );
			DB::delete ( "delete from auto_tasks where id in ($taskIds)" );
			// 删除报告相关
			DB::delete ( "delete from auto_reports where intTaskID in ($taskIds) and intTaskType=1" );
			
			// 删除案例相关
			DB::delete ( "delete from auto_scheme_relations where intSchemeID in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::delete ( "delete from auto_schemes where id in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::commit ();
			try {
				$root = database_path ( "schemes/" );
				// 删除具体的文件
				foreach ( $flows as $flow ) {
					// 删除案例存放位置
					FileHelper::resource_remove ( $root . StringUtil::iconv ( $flow->chrSchemeName ), true, true );
					// 删除虚拟任务案例运行的存放位置
					FileHelper::resource_remove ( $root . $flow->taskId, true, true );
					FileHelper::resource_remove ( $root . "zips/" . $flow->schemeId . ".zip" );
				}
			} catch ( \Exception $e ) {
			}
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
}

?>