<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\Utils\FileHelper;
use App\Utils\StringUtil;
use Illuminate\Support\Facades\Log;

class AutoTaskExecService {
	
	/**
	 * 获取任务执行设置信息
	 *
	 * @param unknown $taskId        	
	 */
	public function getTaskExecInfo($taskId, $user) {
		$rows = DB::select ( "select id,intTaskID taskId,chrBrowserIDs browserIds,chrEmails emails,
				case when chrEmails='' then 0 else 1 end sendEmail
				from auto_task_execs where intFlag=0 and intTimerTaskID=0 
				and intTaskID=$taskId and intCreaterID=$user->id" );
		if (! empty ( $rows ))
			return $rows [0];
		return;
	}
	
	/**
	 *
	 * @param unknown $id        	
	 * @param unknown $user        	
	 */
	public function getSchemeExecState($id, $user) {
		$rows = DB::select ( "select asch.id,ats.id as taskID,case when ate.intState is null then 0 else 1 end state 
				from auto_schemes asch
				INNER JOIN auto_task_relations atr on atr.intSchemeID=asch.id
				INNER JOIN auto_tasks ats on ats.id=atr.intTaskID
				left JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intCreaterID=$user->id  and ate.intState in (0,1)
				where ats.intTaskType=1 and asch.id=$id and asch.intCompanyID=$user->intCompanyID" );
		if (! empty ( $rows ))
			return $rows [0];
	}
	
	/**
	 *
	 * @param unknown $taskId        	
	 * @param unknown $user        	
	 */
	public function getTaskExecState($taskId) {
		return DB::select ( "select id,intTaskID taskId,chrBrowserIDs browserIds,chrEmails emails,
				case when chrEmails='' then 0 else 1 end sendEmail
				from auto_task_execs where intFlag=0 and intTimerTaskID=0
				and intTaskID=$taskId and intState in (0,1)" );
	}
	
	/**
	 *
	 * @param unknown $taskId        	
	 * @param unknown $user        	
	 */
	public function getTaskExecStateByUser($execInfo, $user) {
		$taskId = $execInfo ['taskId'];
		return DB::select ( "select id,intTaskID taskId,chrBrowserIDs browserIds,chrEmails emails,
				case when chrEmails='' then 0 else 1 end sendEmail
				from auto_task_execs where intFlag=0 and intTimerTaskID=0 
				and intTaskID=$taskId and intCreaterID=$user->id and intState in (0,1)" );
	}
	
	/**
	 * 定时任务是否正在执行
	 *
	 * @param unknown $tiTaskId        	
	 * @param unknown $user        	
	 */
	public function getTiTaskExecStateByUser($tiTaskId, $user) {
		return DB::select ( "select id,intTaskID taskId,chrBrowserIDs browserIds,chrEmails emails,
				case when chrEmails='' then 0 else 1 end sendEmail
				from auto_task_execs where intFlag=0
				and intTimerTaskID=$tiTaskId and intState=1" ); // and intCreaterID=$user->id
	}
	
	/**
	 *
	 * @param unknown $execInfo        	
	 * @param unknown $taskId        	
	 * @param unknown $user        	
	 */
	public function insert($execInfo, $user, $tiTaskId = 0, $timer = array()) {
		$taskIds = $execInfo ["taskId"];
		$taskIds = explode ( ";", $taskIds );
		$selBrowsers = $execInfo ["selBrowsers"];
		$selBrowserNames = "";
		$abService = new AutoBrowserService ();
		$rows = $abService->getBrowsers (); // 以后改外从内存数据库中取数据
		foreach ( $rows as $row ) {
			if (in_array ( $row->id, $selBrowsers )) {
				$selBrowserNames .= $row->browserName . ";";
			}
		}
		DB::beginTransaction ();
		try {
			foreach ( $taskIds as $taskId ) {
				$this->createExecTask ( $taskId );
				if ($tiTaskId) { // 定时任务
					DB::update ( "update auto_task_execs set intFlag=1
					where intTimerTaskID=$tiTaskId and intTaskID=$taskId and intCreaterID=$user->id and intCompanyID=$user->intCompanyID" );
				} else { // 普通任务和虚拟任务
					DB::update ( "update auto_task_execs set intFlag=1 where intTimerTaskID=0 
					and intTaskID=$taskId and intCreaterID=$user->id and intCompanyID=$user->intCompanyID" );
					$tiTaskId = 0;
				}
				DB::insert ( "insert into auto_task_execs (intTimerTaskID,intTaskID,chrBrowserIDs,chrBrowserNames,chrEmails,intCreaterID,intState,intCompanyID) 
							values (?,?,?,?,?,?,?,?)", [ 
						$tiTaskId,
						$taskId,
						implode ( ";", $selBrowsers ),
						$selBrowserNames,
						$execInfo ["emails"],
						$user->id,
						0,
						$user->intCompanyID 
				] );
				$exec = DB::select ( "select @@IDENTITY as autoID" );
				$execTaskId = $exec [0]->autoID;
				// 放入sysjobs中
				$sysJService = new AutoJobsService ();
				$payload = array (
						'taskId' => $taskId,
						'execTaskId' => $execTaskId,
						'tiTaskId' => $tiTaskId,
						'timer' => $timer 
				);
				foreach ( $selBrowsers as $browser ) {
					// 放入队列中等待分配机器执行
					DB::insert ( "insert into auto_jobs (intBrowserID,intExecTaskID,tPayload) values (?,?,?)", [ 
							$browser,
							$execTaskId,
							json_encode ( $payload ) 
					] );
				}
			}
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $taskId        	
	 */
	private function createExecTask($taskId) {
		$root = database_path ( "schemes" ) . DIRECTORY_SEPARATOR; // 脚本存放根目录
		$dest = $root . $taskId . DIRECTORY_SEPARATOR; // 任务运行的目录
		$destScript = $dest . "script"; // 任务运行下的脚本目录
		@mkdir ( $destScript, 0777, true );
		$run = "/script/runTest.py";
		$easyTest = $root . "easyTest";
		$oldname = $easyTest . $run;
		$newname = $dest . $run; // runTest
		copy ( $oldname, $newname ); // 拷贝runTest.py脚本
		$rows = DB::select ( "select asch.chrSchemeName from auto_task_relations  atr
				INNER JOIN auto_schemes asch on asch.id=atr.intSchemeID
				where atr.intTaskID=$taskId ORDER BY atr.intExecOrder" );
		foreach ( $rows as $row ) {
			$schemeName = $row->chrSchemeName;
			$resource = $root . $schemeName;
			$resource = StringUtil::iconv ( $resource );
			$nodirs = array (
					"common",
					"data",
					"files",
					"testCase",
					"SRC" 
			); // 从案例中拷贝文件
			FileHelper::resource_copy ( $resource, $dest, $nodirs, false, array (
					"runTest.py" 
			) ); // 即只拷贝__init__.py\run.py以及案例config文件
			FileHelper::writefile_fopen ( $newname, "Main('$schemeName.xml').run()" . "\r\n", "a" );
		}
		$rows = $this->getTaskScripts ( $taskId );
		foreach ( $rows as $row ) {
			$scriptFile = $row->scriptFile; // 存储在服务器上的具体相对路径
			$sfileName = $row->sfileName; // 文件名称
			$scriptParam = $row->scriptParam; // 脚本参数的相对路径
			$spfileName = $row->spfileName;
			$scriptId = $row->scriptID;
			// 下载时 拷贝案例包含的脚本文件：脚本、脚本参数、脚本图片 即"testCase","data","files",文件夹下的文件
			$this->copyScriptFiles ( $easyTest, $dest, $scriptFile, $sfileName, $scriptParam, $spfileName, $scriptId, true );
		}
		$scriptCommon = "/script/common";
		FileHelper::resource_copy ( $easyTest . $scriptCommon, $dest . $scriptCommon, array (), false ); // 拷贝脚本下的common
		                                                                                                 // $src = "/SRC";
		                                                                                                 // FileHelper::resource_copy ( $easyTest . $src, $dest . $src, array (), false );
		$use = "/script/use.py"; // 在服务器上运行时必须拷贝此文件 该文件指定SRC存放位置
		FileHelper::resource_copy ( $easyTest . $use, $dest . $use );
	}
	
	/**
	 *
	 * @param unknown $taskId        	
	 */
	private function getTaskScripts($taskId) {
		$sql = "select sfp.id,ausr.intFlowID,aus.id schemeID,aus.chrSchemeName,ass.chrScriptName,ass.id scriptID,
		atts.chrFile scriptFile,atts.chrFileName sfileName,attp.chrFile scriptParam,attp.chrFileName spfileName,chrProcessName,
		chrProcessStyle,chrProcessType,case when chrProcessTo is null then '' else chrProcessTo end chrProcessTo
		from auto_schemes aus
		INNER JOIN auto_scheme_relations ausr on ausr.intSchemeID=aus.id
		LEFT JOIN sys_flow_processes sfp on sfp.intFlowID=ausr.intFlowID and sfp.intFlag=0
		LEFT JOIN auto_scripts ass on ass.id=sfp.intRelationID
		LEFT JOIN auto_script_relations asr on asr.intScriptID=ass.id and asr.intFlag=0
		LEFT JOIN sys_attachments atts on atts.id=asr.intAttID
		LEFT JOIN sys_attachments attp on attp.id=ass.intParamAttID
		INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
		where atr.intTaskID=$taskId";
		return DB::select ( $sql );
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
		    try{
                FileHelper::resource_copy ( $resFileDir, $destFileDir ); // 将脚本所需要的图片拷贝到指定位置
                @mkdir ( $destCaseDir, 0777, true );
                $destDataDir = $dest . $dataDir . $destParamDir; // 目标参数位置
                @mkdir ( $destDataDir, 0777, true );
                if (! empty ( $sfileName ))
                    // 拷贝具体的脚本
                    copy ( $resource . $testCaseDir . $resourceFileDir . StringUtil::iconv ( $sfileName ), $destCaseDir . StringUtil::iconv ( $sfileName ) );
                if (! empty ( $spfileName ))
                    // 拷贝具体的参数化文件
                    copy ( $resource . $dataDir . $resourceParamDir . StringUtil::iconv ( $spfileName ), $destDataDir . StringUtil::iconv ( $spfileName ) );
            }catch (\Exception $ex){
		        Log::info("脚本：".$resource . $testCaseDir . $resourceFileDir . StringUtil::iconv ( $sfileName )."\r\n");
                Log::info("参数文件：".$resource . $dataDir . $resourceParamDir . StringUtil::iconv ( $spfileName )."\r\n");
            }

		}
		return array (
				"proDir" => $proDir,
				"relaScriptParam" => $relaScriptParam 
		);
	}
}

?>