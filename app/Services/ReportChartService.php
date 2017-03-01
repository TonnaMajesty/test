<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;

class ReportChartService {
	function __construct() {
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getWebTaskPie($user) {
		$companyId = $user->intCompanyID;
		$rows = DB::select ( "SELECT case when intState=0 then '未执行' 
				when intState=1 then '执行中' when intState=2 then '执行成功' else '执行失败' end name,
				count(id) as value,case when intState=0 then 'not' when intState=1 then 'ing' 
				when intState=2 then 'success' else 'fail' end state from (
				select ats.id,IFNULL(ate.intState,0) intState from auto_tasks ats 
				left join auto_task_execs ate on ate.intTaskID=ats.id and ate.intTimerTaskID=0
				where ats.intTaskType=0 and ats.intCompanyID=$companyId
				union ALL
				select att.id,IFNULL(ate.intState,0) intState from auto_timer_tasks att 
				left join auto_task_execs ate on ate.intTaskID=att.id and ate.intTimerTaskID<>0
				where att.intCompanyID=$companyId
				)a GROUP BY intState" );
		return $rows;
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getWebTaskLine($user, $cycle) {
		$companyId = $user->intCompanyID;
		$df = "";
		switch ($cycle) {
			case "month" :
				$df = "%Y-%m";
				break;
			case "year" :
				$df = "%Y";
				break;
			case "day" :
				$df = "%Y-%m-%d";
				break;
			case "week" :
				$df = "%U";
				break;
		}
		$rows = DB::select ( "select name,COUNT(*) value from (
				SELECT arep.id,DATE_FORMAT(arep.created_at,'$df') name 
				from auto_timer_tasks att
				INNER JOIN auto_reports arep on arep.intTaskID=att.id and arep.intTaskType=2
				where att.intCompanyID=$companyId
				UNION ALL
				SELECT arep.id,DATE_FORMAT(arep.created_at,'$df') name from auto_tasks ats
				INNER JOIN auto_reports arep on arep.intTaskID=ats.id and arep.intTaskType=1 
				where ats.intTaskType=0 and ats.intCompanyID=$companyId)a GROUP BY name" );
		return $rows;
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getSchemeChart($user, $cycle) {
		$companyId = $user->intCompanyID;
		$df = "";
		switch ($cycle) {
			case "month" :
				$df = "%Y-%m";
				break;
			case "year" :
				$df = "%Y";
				break;
			case "day" :
				$df = "%Y-%m-%d";
				break;
			case "week" :
				$df = "%U";
				break;
		}
		$rows = DB::select ( "select name,count(id) value from (
				select DATE_FORMAT(created_at,'$df') name,id 
				from auto_schemes asch where intFlag=0 and asch.intCompanyID=$companyId
				)a GROUP BY name" );
		return $rows;
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getScriptChart($user) {
		$companyId = $user->intCompanyID;
		$rows = DB::select ( "select COUNT(*) value from auto_scripts asci 
				where intFlag=0 and asci.intCompanyID=$companyId" );
		return $rows;
	}
}

?>