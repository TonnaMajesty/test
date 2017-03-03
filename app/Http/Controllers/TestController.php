<?php

namespace App\Http\Controllers;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AutoExecReportService;
use Illuminate\Support\Facades\Auth;
use App\Services\ProjectService;
use App\Services\SysDictService;
use App\Services\WormQueueService;
use DB;

class TestController extends Controller 
{

	public function __construct()
	{
		$this->wq = new WormQueueService();
	}
	// public function test()
	// {
	// 	$result = DB::select("select ats.id,chrTaskName taskName,u.chrUserName createUser,ate.chrBrowserNames browserNames,
	// 			ate.id taskExecID,ats.intProjectID projectId,ate.updated_at,
	// 			apro.chrProjectName projectName
	// 			from auto_tasks ats
	// 			INNER JOIN users u on u.id=ats.intCreaterID
	// 			LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intFlag=0 
	// 			and ate.intTimerTaskID=0 and ate.intCreaterID=23
	// 			INNER JOIN auto_projects apro on apro.id=ats.intProjectID
	// 			where ats.intFlag=0 and ats.intCompanyID=8 and ats.intTaskType=0 AND ate.id=1141");
	// 	dd($result);
	// }

//案例详情
// 	public function test()
// 	{
// 		$result = DB::select("select DISTINCT 
// aus.id,
// ats.chrTaskName 任务名称,
// chrSchemeName schemeName,apro.chrProjectName projectName,u.chrUserName createUser,
//               case when ate.intState=0 then '排队中' when ate.intState=1 then '执行中' when ate.intState=2 then '执行成功'
//               when ate.intState=3 then '执行失败' else '未执行' end state,ate.chrBrowserNames browserNames,ats.intProjectID projectId ,ate.id taskExecID 
//               from auto_schemes aus
//               INNER JOIN users u on u.id=aus.intCreaterID
//               INNER JOIN auto_task_relations atr on atr.intSchemeID=aus.id
//               INNER JOIN auto_tasks ats on ats.id=atr.intTaskID -- and ats.intTaskType=1
//               LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intFlag=0 and ate.intTimerTaskID=0
//               LEFT JOIN auto_projects apro on apro.id=ats.intProjectID
//               where aus.intFlag=0 and ats.id in (select intTaskID from auto_timer_relate_tasks where intTiTaskID=116)");
// 		dd($result);
// 	}

	// public function test()
	// {
	// 	$result = DB::select("SELECT arep.created_at,arep.updated_at,a.allCount,b.*,c.stepErrCount from (
	// 					select count(intScriptID) allCount,intScriptID from (
	// 					select intScriptID from auto_logs
	// 					GROUP BY intScriptID,intReportID HAVING intReportID=871 and intScriptID<>0)b)a
	// 					LEFT JOIN
	// 					(select asch.chrSchemeName,asri.chrScriptName,alog.intSchemeID,alog.intScriptID,
	// 					alog.intOrderNo,alog.chrCmd,alog.chrCmdParam,alog.chrDescription,alog.chrErrorMessage 
	// 					from auto_logs alog
	// 					left JOIN auto_scripts asri on asri.id=alog.intScriptID
	// 					left JOIN auto_schemes asch on asch.id=alog.intSchemeID
	// 					where intReportID=871 and chrResult ='error')b on 1=1
	// 					LEFT JOIN(
	// 					select COUNT(*) stepErrCount,intScriptID from auto_logs alog 
	// 					GROUP BY intScriptID,intReportID,chrResult
	// 					HAVING intReportID=871 and chrResult ='error')c on c.intScriptID=a.intScriptID
	// 					left JOIN auto_reports arep on arep.id=871");
	// 	dd($result);
	// }
	public function test()
	{
		$result = $this->wq->parseEmailData('1226');
		dd($result);
	}
}
