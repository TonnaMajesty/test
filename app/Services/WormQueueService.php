<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\Utils\FileHelper;
use App\Utils\EmailHelper;
use App\User;
use App\AutoReport;
use Illuminate\Support\Facades\Auth;

class WormQueueService {
	
	/**
	 * 获取队列中的所有任务
	 */
	public function getQueueJobs() {
		return DB::select ( "select aeb.id as browserID,aeb.chrBrowserENName,aj.id jobID,aj.intExecTaskID,
				aj.tPayload from auto_exec_browsers aeb
				INNER JOIN auto_jobs aj on aj.intBrowserID=aeb.id and aj.tintState=0
				ORDER BY aj.id" );
	}
	
	/**
	 *
	 * @return unknown
	 */
	private function getTimerRates() {
		$rows = DB::select ( "select id,chrDictName,chrDictValue from sys_dicts where chrDictName='execrate'" );
		// 存入缓存
		return $rows;
	}
	
	/**
	 *
	 * @param unknown $payload        	
	 * @return boolean
	 */
	private function containsDate($timer) {
		$now_date = strtotime ( date ( 'Y-m-d' ) );
		$lastDate = $timer ["lastDate"];
		if ($now_date == $lastDate) // 当前天已执行过
			return false;
		$execBeginDate = strtotime ( $timer ["execBeginDate"] );
		$execEndDate = strtotime ( $timer ["execEndDate"] );
		// 还需要继续循环执行该定时任务
		if ($now_date >= $execBeginDate && $now_date <= $execEndDate) {
			if (empty ( $lastDate )) // 第一次执行
				return true;
			$execRate = $timer ["execRate"];
			$rates = $this->getTimerRates ();
			$dictValue = "";
			foreach ( $rates as $rate ) {
				if ($rate->id == $execRate) {
					$dictValue == $rate->chrDictName;
					break;
				}
			}
			switch ($dictValue) {
				case "每周" :
					$nextDate = strtotime ( "+1 week", strtotime ( $lastDate ) );
					break;
				case "每月" :
					$nextDate = strtotime ( "+1 month", strtotime ( $lastDate ) );
					break;
				case "每年" :
					$nextDate = strtotime ( "+1 year", strtotime ( $lastDate ) );
					break;
				default :
					$nextDate = strtotime ( "+1 day", strtotime ( $lastDate ) );
					break;
			}
			if ($now_date == $nextDate)
				return true;
			return false;
		}
		return false;
	}
	
	/**
	 *
	 * @param unknown $tiTaskId        	
	 */
	private function updateReport($tiTaskId, $taskId) {
		$taskType = 1;
		$tId = $taskId;
		if ($tiTaskId) {
			$taskType = 2; // 定时任务
			$tId = $tiTaskId;
		}
		$rows = DB::select ( "select id from auto_reports 
				where intTaskID=$tId and intTaskType=$taskType and intState=1 and intFlag=0" );
		if (empty ( $rows )) {
			$report_model = new AutoReport ();
			$report_model->intTaskID = $tId;
			$report_model->intTaskType = $taskType;
			$report_model->intState = 1;
			$report_model->save ();
			DB::update ( "update auto_reports set intFlag=1 where intTaskID=$tId and intTaskType=$taskType 
			and intState in (2,3) and intFlag=0" );
			return $report_model->id;
		}
		return $rows [0]->id;
	}
	
	/**
	 * 分发自动化任务
	 *
	 * @param unknown $connection        	
	 * @param unknown $queue        	
	 * @param unknown $delay        	
	 * @param unknown $memory        	
	 * @param unknown $daemon        	
	 * @param unknown $tries        	
	 */
	public function dispachAutoTask(&$jobs, $connection, $queue, $delay, $memory, $daemon, $tries) {
		$ret = true;
		try {
			foreach ( $jobs as $key => $job ) {
				$payload = json_decode ( $job->tPayload, true );
				$tiTaskId = $payload ['tiTaskId'];
				if ($tiTaskId) {
					$timer = $payload ["timer"];
					// 表示该定时任务在可执行日期内
					if ($this->containsDate ( $timer )) {
						$execTime = $timer ["execTime"];
						$now_hour = date ( "H" );
						$execTime = date ( "H", strtotime ( $execTime ) );
						// 该定时任务在执行时间点中
						if ($now_hour != $execTime) { // 若该定时任务在该hour上不执行 则继续下条记录
							$ret = false;
							print_r ( "this job is timer not time\r\n" );
							continue;
						}
					} else
						continue;
				}
				$browserId = $job->browserID;
				$machines = DB::select ( "select aeb.chrBrowserENName,smac.id machID,smac.chrMachName,smac.chrIp,
						smr.id mconfID,smr.chrHub,smr.intHubPort from auto_exec_browsers aeb
						INNER JOIN sys_machine_configs smc on smc.intBrowserID=aeb.id
						INNER JOIN sys_machines smac on smac.id=smc.intMachineID
						INNER JOIN sys_machine_relations smr on smr.intMachineID=smc.intMachineID and smr.intHubNowCount<smr.intHubMaxCount
						where aeb.id=$browserId ORDER BY (smr.intHubMaxCount-smr.intHubNowCount) desc limit 1" );
				if (! empty ( $machines )) { // 有机器空闲
					$machine = $machines [0];
					$hubUrl = "http://" . $machine->chrIp . ":" . $machine->intHubPort . $machine->chrHub;
					$machId = $machine->machID;
					$args = array (
							'jobId' => $job->jobID,
							'payload' => $payload,
							'browsers' => array (
									'browserId' => $browserId,
									'machineId' => $machId,
									$machine->chrBrowserENName => $hubUrl 
							),
							'requestURL' => 'http://localhost:8088/ext/log?token=q8E89zRdp' 
					);
					$root = database_path ( "schemes" ) . DIRECTORY_SEPARATOR;
					$taskId = $payload ["taskId"];
					
					// $runService = new RunTaskPthreadService ( $run );
					// $runService->start ();
					// popen ( "cmd /c $run &", 'r' ); // 必须放到最后
					$status = 0;
					if ($status === 0) { // 发送命令成功
						DB::beginTransaction ();
						try {
							$reportId = $this->updateReport ( $tiTaskId, $taskId ); // 任务开启前 插入一条报告记录
							DB::update ( "update auto_jobs set tintState=1 where id=$job->jobID" );
							$execTaskId = $payload ['execTaskId'];
							DB::update ( "update auto_task_execs set intState=1 where id=$execTaskId" );
							if ($tiTaskId) {
								DB::update ( "update auto_timer_task_relations set intState=1 where intTiTaskID=$tiTaskId and intState=0" );
							}
							DB::update ( "update sys_machine_relations set intHubNowCount=intHubNowCount+1 where intMachineID=$machId" );
							/* $redis = RedisHelper::getInstance (); */
							DB::commit ();
							$args ['reportId'] = $reportId;
							$json = str_replace ( "\"", "\\\"", json_encode ( $args ) );
							$run = $root . $taskId;
							// $run .= "/script/runTest.py " . $json;
							$run .= "/script/run.py " . $json;
							// Log::info ( $run );
							exec ( "cmd /c $run", $ret, $status );
						} catch ( \Exception $e ) {
							DB::rollback ();
							throw $e;
						}
					} else {
						$ret = false;
						print_r ( "worm send dos order error:" . json_encode ( $args ) . "\r\n" );
					}
				}
			}
		} catch ( \Exception $e ) {
			$ret = false;
			print_r ( "worm exec error:" . $e->getMessage () . "\r\n" );
		}
		return $ret;
	}
	
	/**
	 *
	 * @param unknown $logs        	
	 * @param unknown $jobId        	
	 */
	public function moveLogImage(&$logs, $jobId) {
		$resource = database_path ( 'schemes/' ) . $logs ["image"];
		$screenShot = "/schemes/report/images/";
		$relativeDir = $screenShot . date ( 'Y-m-d' ) . "/" . $jobId . "/";
		$dest = public_path () . $relativeDir;
		@mkdir ( $dest, 0777, true );
		if (is_file ( $resource )) {
			rename ( $resource, $dest . basename ( $logs ["image"] ) );
			$logs ["image"] = $relativeDir . basename ( $logs ["image"] );
		} else
			$logs ["image"] = $screenShot . "shot_default.jpg";
		/*
		 * else $logs ["image"] = "no";
		 */
	}
	
	/**
	 * 获取指定执行任务下的队列任务
	 *
	 * @param unknown $jobId        	
	 */
	private function getQueueJobsByExecId($jobId, $execTaskId) {
		return DB::select ( "select id from auto_jobs 
				where intExecTaskID=$execTaskId and id not in ($jobId) LIMIT 1" );
	}
	
	/**
	 * 删除队列中的任务
	 *
	 * @param unknown $jobId        	
	 */
	private function deleteQueue($jobId) {
		DB::delete ( "delete from auto_jobs where id=$jobId" );
	}
	
	/**
	 * 释放被占用的机器
	 *
	 * @param unknown $browsers        	
	 */
	private function releaseMachine($browsers) {
		$machineId = $browsers ["machineId"];
		DB::update ( "update sys_machine_relations set intHubNowCount=intHubNowCount-1 where intMachineID=$machineId and intHubNowCount>0" );
	}
	
	/**
	 *
	 * @param unknown $execTaskId        	
	 */
	private function sendEmail($execTaskId, $state, $reportId, $taskName) {
		try {
			switch ($state) {
				case 3 :
					$stateinfo = "失败";
					break;
				default :
					$stateinfo = "成功";
					break;
			}
			$execInfos = DB::select ( "select ate.id,ate.intCompanyID,ate.intCreaterID,chrEmails,chrUserName 
					from auto_task_execs ate
					LEFT JOIN users u on u.chrEmail=REPLACE(ate.chrEmails,';','') 
					where ate.id =$execTaskId" );
			$emails = $execInfos [0]->chrEmails;
			if (! empty ( $emails )) {
				$slogs = DB::select ( "select arep.created_at,arep.updated_at,a.allCount,b.*,c.stepErrCount from (
						select count(intScriptID) allCount,intScriptID from (
						select intScriptID from auto_logs
						GROUP BY intScriptID,intReportID HAVING intReportID=$reportId and intScriptID<>0)b)a
						LEFT JOIN
						(select asch.chrSchemeName,asri.chrScriptName,alog.intSchemeID,alog.intScriptID,
						alog.intOrderNo,alog.chrCmd,alog.chrCmdParam,alog.chrDescription,alog.chrErrorMessage 
						from auto_logs alog
						left JOIN auto_scripts asri on asri.id=alog.intScriptID
						left JOIN auto_schemes asch on asch.id=alog.intSchemeID
						where intReportID=$reportId and chrResult ='error')b on 1=1
						LEFT JOIN(
						select COUNT(*) stepErrCount,intScriptID from auto_logs alog 
						GROUP BY intScriptID,intReportID,chrResult
						HAVING intReportID=$reportId and chrResult ='error')c on c.intScriptID=a.intScriptID
						left JOIN auto_reports arep on arep.id=$reportId" );
				$errLists = array ();
				$errSCount = 0;
				$stepErrCount = 0;
				$scriptId = 0;
				$schemeId = 0;
				foreach ( $slogs as $slog ) {
					$intSchemeId = $slog->intSchemeID;
					$intScriptId = $slog->intScriptID;
					if (! empty ( $intSchemeId )) {
						$stepErrCount ++;
						if ($schemeId != $intSchemeId) {
							$errList = array (
									"schemeName" => $slog->chrSchemeName,
									"scriptName" => "",
									"optName" => "",
									"msg" => "" 
							);
							$schemeId = $intSchemeId;
							array_push ( $errLists, $errList ); // 案例
						}
						if ($scriptId != $intScriptId) {
							$errList = array (
									"schemeName" => "",
									"scriptName" => $slog->chrScriptName,
									"optName" => "步骤：" . $slog->stepErrCount,
									"msg" => "错误详情" 
							);
							array_push ( $errLists, $errList ); // 脚本
							$scriptId = $intScriptId;
							$errSCount ++;
						}
						$errList = array (
								"schemeName" => "",
								"scriptName" => "",
								"optName" => "失败步骤：" . $slog->intOrderNo . $slog->chrDescription,
								"msg" => $slog->chrErrorMessage 
						);
						array_push ( $errLists, $errList ); // 步骤
					}
				}
				$allCount = $slogs [0]->allCount; //
				$sucSCount = ($allCount - $errSCount);
				$sucSPercent = intval ( ($sucSCount / $allCount) * 100 );
				$scripts = array (
						"sCount" => $allCount,
						"errSCount" => $errSCount,
						"sucSCount" => $sucSCount,
						"sucSPercent" => $sucSPercent . "%" 
				);
				$emails = explode ( ";", $emails );
				$name = count ( $emails ) > 1 ? "各位" : ($execInfos [0]->chrUserName);
				$beginTime = $slogs [0]->created_at;
				$endTime = $slogs [0]->updated_at;
				$date = floor ( (strtotime ( $endTime ) - strtotime ( $beginTime )) / 86400 );
				$hour = floor ( (strtotime ( $endTime ) - strtotime ( $beginTime )) % 86400 / 3600 );
				$minute = floor ( (strtotime ( $endTime ) - strtotime ( $beginTime )) % 86400 / 60 );
				$second = floor ( (strtotime ( $endTime ) - strtotime ( $beginTime )) ) % 86400 % 60;
				$times = $date . "天" . $hour . "小时" . $minute . "分" . $second . "秒";

				$parse = $this->parseEmailData($execTaskId);

				$pageData = array (
						"user" => array (
								"name" => $name 
						),
						"state" => $stateinfo,
						"sysUrl" => "http://10.10.12.163:8088/",
						"rlist" => array (
								"taskName" => $taskName,
								"beginTime" => $beginTime,
								"endTime" => $endTime,
								"times" => $times,
								"script" => $scripts 
						),
						"errors" => $errLists,
						"task_list" => $parse['task_list'], 
						"scheme_list" => $parse['scheme_list'], 
						"script_sum" => $parse['script_sum']
				);
				$emailInfo = array (
						"to" => $emails,
						"subject" => "用友优普云测试报告" 
				);
				EmailHelper::sendEmail ( "emails.report", $pageData, $emailInfo );
			}
		} catch ( \Exception $e ) {
			Log::info ( "send email error:" . $e->getMessage () );
		}
	}
	
	/**
	 *
	 * @param unknown $payload        	
	 * @return boolean
	 */
	private function containsExecDate($timer) {
		$now_date = strtotime ( date ( 'Y-m-d' ) );
		$execBeginDate = strtotime ( $timer ["execBeginDate"] );
		$execEndDate = strtotime ( $timer ["execEndDate"] );
		// 还需要继续循环执行该定时任务
		if ($now_date > $execBeginDate && $now_date < $execEndDate) {
			return true;
		}
		return false;
	}
	
	/**
	 *
	 * @param unknown $execs        	
	 * @param unknown $payload        	
	 */
	private function resetTimerTask($execs, $timer) {
		// 还需要继续循环执行该定时任务
		if ($this->containsExecDate ( $timer )) {
			$user = new User ();
			foreach ( $execs as $exec ) {
				$user->id = $exec->intCreaterID;
				$tiTaskId = $exec->intTimerTaskID;
				$taskIds [] = $exec->intTaskID;
				$selBrowsers = $exec->chrBrowserIDs;
				$emails = $exec->chrEmails;
			}
			$execInfo = array (
					"taskId" => implode ( ";", $taskIds ),
					"selBrowsers" => explode ( ";", $selBrowsers ),
					"emails" => $emails 
			);
			$timer ["lastDate"] = date ( 'Y-m-d' );
			// 重新生成队列任务
			$ateService = new AutoTaskExecService ();
			$ateService->insert ( $execInfo, $user, $tiTaskId, $timer );
		}
	}
	
	/**
	 *
	 * @param unknown $tiTaskState        	
	 * @param unknown $payload        	
	 */
	private function updateReportState($tiTaskState, $reportId) {
		DB::update ( "update auto_reports set intState=$tiTaskState,updated_at=now() where id=$reportId" );
	}
	
	/**
	 * 更改任务执行状态
	 *
	 * @param unknown $execTaskId        	
	 */
	private function updateExecState($jobId, $execTaskId, $payload, $reportId, $taskId, $tiTaskId) {
		$rows = $this->getQueueJobsByExecId ( $jobId, $execTaskId );
		if (empty ( $rows )) {
			$rows = DB::select ( "select id from auto_logs
				where intExecTaskID=$execTaskId and chrResult in ('error') limit 1" );
			if (empty ( $rows )) // 没有失败的操作
				$state = 2; // 成功
			else
				$state = 3;
				// 更改任务的执行状态
			DB::update ( "update auto_task_execs set intState=$state where id=$execTaskId" );
			// 若$tiTaskId!=0 则为定时任务
			if ($tiTaskId) {
				// 判断定时任务下的任务是否执行完毕
				$execs = DB::select ( "select ate.id,ate.intTimerTaskID,ate.intTaskID,ate.intState,
						ate.chrBrowserIDs,ate.chrEmails,ate.intCreaterID,atit.chrTiTaskName taskName
						from auto_task_execs ate
						INNER JOIN auto_timer_tasks atit on atit.id=ate.intTimerTaskID
						where intTimerTaskID=$tiTaskId order by intState" );
				$tiTaskState = 2; // 成功
				foreach ( $execs as $exec ) {
					if ($exec->intState == 1)
						return;
					else if ($exec->intState == 3) {
						$tiTaskState = 3;
						break;
					}
				}
				// 更新定时任务的执行状态和执行次数
				DB::update ( "update auto_timer_task_relations set intState=$tiTaskState,intExecCount=intExecCount+1,
				dtLastTime=NOW() where intTiTaskID=$tiTaskId" );
				$this->updateReportState ( $tiTaskState, $reportId );
				$this->sendEmail ( $execTaskId, $tiTaskState, $reportId, $execs [0]->taskName ); // 发送邮件
				$timer = $payload ["timer"];
				$this->resetTimerTask ( $execs, $timer );
			} else {
				$this->updateReportState ( $state, $reportId );
				$execs = DB::select ( "select chrTaskName taskName from auto_tasks where id=$taskId" );
				$this->sendEmail ( $execTaskId, $state, $reportId, $execs [0]->taskName ); // 发送邮件
			}
		}
	}
	
	/**
	 *
	 * @param unknown $jobId        	
	 */
	private function getJobById($jobId) {
		return DB::select ( "select id from auto_jobs where id=$jobId" );
	}
	
	/**
	 * 根据回传的日志 更新队列任务以及任务状态
	 *
	 * @param unknown $jobId        	
	 * @param unknown $payload        	
	 * @param unknown $browsers        	
	 * @param unknown $schemeId        	
	 * @param unknown $status        	
	 */
	public function receive($jobId, $reportId, $payload, $browsers, $schemeId, $status) {
		try {
			$execTaskId = $payload ["execTaskId"];
			$taskId = $payload ["taskId"];
			$tiTaskId = $payload ["tiTaskId"];
			if ($status == "END") { // 案例运行完毕
				$rows = DB::select ( "select COUNT(*) AllSchemeCount from auto_task_relations atr
                        INNER JOIN auto_schemes asch on asch.id=atr.intSchemeID
						where atr.intTaskID=$taskId
						UNION all
						select COUNT(*) AllSchemeCount from (
						select DISTINCT intSchemeID FROM auto_logs alo
						where alo.intJobID=$jobId and alo.chrStatus='END')a" );
				if ($rows [0]->AllSchemeCount == $rows [1]->AllSchemeCount) {
					$job = $this->getJobById ( $jobId );
					if (! empty ( $job )) { // 说明第一次结束
						DB::beginTransaction ();
						try {
							$this->releaseMachine ( $browsers ); // 释放被占用的机器
							$this->deleteQueue ( $jobId ); // 删除队列中的任务
							DB::commit ();
							$this->updateExecState ( $jobId, $execTaskId, $payload, $reportId, $taskId, $tiTaskId ); // 更改任务执行状态
						} catch ( \Exception $e ) {
							DB::rollback ();
							Log::info ( "update report state error" . $e->getMessage () );
							throw $e;
						}
					}
				}
			}
		} catch ( \Exception $e ) {
			throw $e;
		}
	}

	public function parseEmailData($execTaskId){
		$result = [];
		//任务详情
		$result['task_list'] = DB::select("SELECT ats.id, chrTaskName,apro.chrProjectName, u.chrUserName,ats.updated_at, case when ate.intState=0 then '排队中' when ate.intState=1 then '执行中' when ate.intState=2 then '执行成功' when ate.intState=3 then '执行失败' else '未执行' end state,ate.chrBrowserNames, ate.id taskExecID,ats.intProjectID projectId
              from auto_tasks ats INNER JOIN users u on u.id=ats.intCreaterID LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id INNER JOIN auto_projects apro on apro.id=ats.intProjectID where  ats.id in (select intTaskID from auto_timer_relate_tasks where intTiTaskID=(select intTimerTaskID from auto_task_execs where id=$execTaskId)) ORDER BY ats.chrTaskName desc
			");
		//案例详情
		$result['scheme_list'] = DB::select("SELECT DISTINCT aus.id,
				ats.chrTaskName, chrSchemeName schemeName,apro.chrProjectName projectName,u.chrUserName createUser, case when ate.intState=0 then '排队中' when ate.intState=1 then '执行中' when ate.intState=2 then '执行成功'
              when ate.intState=3 then '执行失败' else '未执行' end state,ate.chrBrowserNames browserNames,ats.intProjectID projectId ,ate.id taskExecID 
              from auto_schemes aus
              INNER JOIN users u on u.id=aus.intCreaterID
              INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
              INNER JOIN auto_tasks ats on ats.id=atr.intTaskID
              LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id 
              LEFT JOIN auto_projects apro on apro.id=ats.intProjectID
              where ats.id in (select intTaskID from auto_timer_relate_tasks where intTiTaskID=(select intTimerTaskID from auto_task_execs where id=$execTaskId))");
		//脚本日志统计分析
		$result['script_sum'] = DB::select("SELECT count(*) count, l.chrDescription,COUNT(CASE WHEN l.chrResult='PASS' THEN '成功' END)/count(*)*100 passlv from auto_logs l LEFT JOIN auto_scripts s on l.intScriptID=s.id	where l.intExecTaskID=$execTaskId  GROUP BY l.chrDescription");
		// dd($result['script_sum']);
		
		return $result;
	}
}

?>