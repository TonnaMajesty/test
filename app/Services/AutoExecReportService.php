<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class AutoExecReportService {
	/**
	 *
	 * @param unknown $taskExecId        	
	 * @param unknown $user        	
	 */
	public function getTaskExecReportStep($taskExecId, $user, $lit = "") {
		$limit = "";
		if ($lit)
			$limit = "limit 1";
			/*
		 * return DB::select ( "select * from auto_logs where intExecTaskID=$taskExecId order by intBrowserID,intOrderNo,intSchemeID $limit" );
		 */
		return DB::select ( "select aeb.chrBrowserName browserName,ast.chrScriptName scriptName,alog.* 
				from auto_logs alog
				INNER JOIN auto_task_relations atr on atr.intTaskID=alog.intTaskID and atr.intSchemeID=alog.intSchemeID
				left JOIN auto_scripts ast on ast.id=alog.intScriptID 
				LEFT JOIN auto_exec_browsers aeb on aeb.id=alog.intBrowserID
				where atr.intCompanyID=$user->intCompanyID and alog.intExecTaskID=$taskExecId
				order by atr.intExecOrder,intBrowserID,intOrderNo $limit" );
	}
	/**
	 *
	 * @param unknown $taskExecId        	
	 * @param unknown $user        	
	 */
	public function getTimerTaskExecReportStep($reportId, $user, $lit = "") {
		$limit = "";
		if ($lit)
			$limit = "limit 1";
		return DB::select ( "select aeb.chrBrowserName browserName,ast.chrScriptName scriptName,alog.* 
				from auto_logs alog
				INNER JOIN auto_task_relations atr on atr.intTaskID=alog.intTaskID and atr.intSchemeID=alog.intSchemeID
				left JOIN auto_scripts ast on ast.id=alog.intScriptID
				LEFT JOIN auto_exec_browsers aeb on aeb.id=alog.intBrowserID
				where atr.intCompanyID=$user->intCompanyID and alog.intReportID=$reportId
				order by intBrowserID,atr.intTaskID,atr.intExecOrder,intOrderNo $limit" );
	}
	
	/**
	 *
	 * @param unknown $user        	
	 * @param unknown $search        	
	 */
	private function getReportCount($user, $search,$wl) {
		$res = DB::select ( "SELECT count(*) allCount from 
				(
				select atit.intCreaterID,atit.intProjectID,atrep.id,'2' intReportType,atit.chrTiTaskName chrTaskName,atrep.intState,atrep.created_at
				from auto_timer_tasks atit
				INNER JOIN sys_dicts dic on dic.id=atit.intTiTaskTypeID and dic.chrDictName='titasktype'
				INNER JOIN auto_reports atrep on atrep.intTaskID=atit.id and atrep.intTaskType=2
				where atit.intCompanyID=$user->intCompanyID
				UNION ALL
				select ats.intCreaterID,ats.intProjectID,atrep.id,case when ats.intTaskType=1 then '0' else '1' end intReportType,
				ats.chrTaskName,atrep.intState,atrep.created_at
				from auto_tasks ats
				INNER JOIN auto_reports atrep on atrep.intTaskID=ats.id and atrep.intTaskType=1
				where ats.intCompanyID=$user->intCompanyID
				)a
				INNER JOIN auto_projects apro on apro.id=a.intProjectID
				INNER JOIN users u on u.id=a.intCreaterID  
				where $search $wl" );
		return $res [0]->allCount;
	}
	
	/**
	 *
	 * @param unknown $search        	
	 */
	private function structureSearchSQL($search) {
		if (! empty ( $search )) {
			$sql = array ();
			$projectId = $search ["projectId"];
			$reportType = $search ["reportType"];
			$state = $search ["state"];
			$taskName = trim ( $search ["taskName"] );
			$creater = trim ( $search ["creater"] );
			if ($projectId) {
				array_push ( $sql, "a.intProjectID=$projectId" );
			}
			if ($reportType !== "") {
				array_push ( $sql, "a.intReportType=$reportType" );
			}
			if ($state > 0)
				array_push ( $sql, "a.intState=$state" );
			if ($taskName)
				array_push ( $sql, "a.chrTaskName='$taskName'" );
			if ($creater)
				array_push ( $sql, "u.chrUserName='$creater'" );
			$sql = implode ( " and ", $sql );
		}
		if (empty ( $sql ))
			$sql = "1=1";
		return $sql;
	}
	
	/**
	 * 获取报告列表
	 *
	 * @param unknown $user        	
	 */
	public function getReportList($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl) {
		$search = $this->structureSearchSQL ( $search );
		$allcount = $this->getReportCount ( $user, $search,$wl );
		$reports = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$pagecount = $iDisplayStart;
		$rows = DB::select ( "SELECT a.id,case when a.intReportType=0 then '案例运行' when a.intReportType=1 then '普通任务' else '定时任务' end reportType,
				a.chrTaskName taskName,case when a.intState=2 then '执行成功' when a.intState=3 then '执行失败' else '执行中' end state,
				a.created_at,apro.chrProjectName projectName,u.chrUserName userName from 
				(
				select atit.intCreaterID,atit.intProjectID,atrep.id,'2' intReportType,atit.chrTiTaskName chrTaskName,atrep.intState,atrep.created_at
				from auto_timer_tasks atit
				INNER JOIN sys_dicts dic on dic.id=atit.intTiTaskTypeID and dic.chrDictName='titasktype'
				INNER JOIN auto_reports atrep on atrep.intTaskID=atit.id and atrep.intTaskType=2
				where atit.intCompanyID=$user->intCompanyID
				UNION ALL
				select ats.intCreaterID,ats.intProjectID,atrep.id,case when ats.intTaskType=1 then '0' else '1' end intReportType,
				ats.chrTaskName,atrep.intState,atrep.created_at
				from auto_tasks ats
				INNER JOIN auto_reports atrep on atrep.intTaskID=ats.id and atrep.intTaskType=1
				where ats.intCompanyID=$user->intCompanyID 
				)a
				INNER JOIN auto_projects apro on apro.id=a.intProjectID 
				INNER JOIN users u on u.id=a.intCreaterID 
				where $search $wl ORDER BY id desc
				limit ?,?", [ 
				$pagecount,
				$iDisplayLength 
		] );
		$reports .= json_encode ( $rows );
		$reports .= "}";
		return $reports;
	}

	public function getReportLogs($intExecTaskID){
		$result = DB::select("SELECT s.chrScriptName,l.intLineNo,l.chrCmd,l.chrCmdParam,l.chrDescription,l.chrErrorMessage,l.chrResult,l.fltDuring,l.chrImage from auto_logs l 
			LEFT JOIN auto_scripts s on l.intScriptID=s.id
			where l.intExecTaskID=$intExecTaskID ORDER BY intScriptID,l.id");

		return json_encode($result);
	}

}

?>