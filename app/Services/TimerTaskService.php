<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\AutoTimerTask;
use Illuminate\Support\Facades\Log;

class TimerTaskService
{

    /**
     *
     * @param unknown $user
     * @param unknown $search
     */
    private function getTiTaskCount($user, $search, $wl)
    {
        $rows = DB::select("select COUNT(*) allCount from auto_timer_tasks atit
				left JOIN (
				select id,intTaskID,intState from auto_reports arep
				where arep.intFlag=0 and arep.intTaskType=2)arep on arep.intTaskID=atit.id
				INNER JOIN users u on u.id=atit.intCreaterID
				INNER JOIN auto_projects apro on apro.id=atit.intProjectID 
				where atit.intFlag=0 and atit.intCompanyID=$user->intCompanyID and $search $wl");
        return $rows [0]->allCount;
    }

    /**
     *
     * @param unknown $search
     */
    private function structureSearchSQL($search)
    {
        if (!empty ($search)) {
            $sql = array();
            $projectId = $search ["projectId"];
            $testType = $search ["testType"];
            $state = $search ["state"];
            $taskName = trim($search ["taskName"]);
            $creater = trim($search ["creater"]);
            if ($projectId) {
                array_push($sql, "atit.intProjectID=$projectId");
            }
            if ($testType) {
                array_push($sql, "atit.intTiTaskTypeID=$testType");
            }
            if ($state)
                array_push($sql, "arep.intState=$state");
            else if ($state !== "")
                array_push($sql, "arep.intState is NULL");
            if ($taskName)
                array_push($sql, "atit.chrTiTaskName='$taskName'");
            if ($creater)
                array_push($sql, "u.chrUserName='$creater'");
            $sql = implode(" and ", $sql);
        }
        if (empty ($sql))
            $sql = "1=1";
        return $sql;
    }

    /**
     *
     * @param unknown $secho
     * @param unknown $iDisplayStart
     * @param unknown $iDisplayLength
     * @return string
     */
    public function getTimerTaskList($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl)
    {
        $search = $this->structureSearchSQL($search);
        $allcount = $this->getTiTaskCount($user, $search, $wl);
        $tiTasks = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
        $pagecount = $iDisplayStart;
        $rows = DB::select("select atit.id,atit.chrTiTaskName tiTaskName,dic.chrDictValue taskType,u.chrUserName userName,ate.chrBrowserNames browserNames,
				atitr.intExecCount execCount,case when atitr.intState=1 then '执行中' when atitr.intState=2 then '执行成功' 
				when atitr.intState=3 then '执行失败' else '排队中' end state,arep.id as reportId,apro.chrProjectName projectName
				from auto_timer_tasks atit
				INNER JOIN sys_dicts dic on dic.id=atit.intTiTaskTypeID and dic.chrDictName='titasktype' 
				INNER JOIN auto_timer_task_relations atitr on atitr.intTiTaskID=atit.id
				LEFT JOIN auto_reports arep on arep.intTaskID=atit.id and arep.intTaskType=2 and arep.intFlag=0
				INNER JOIN auto_projects apro on apro.id=atit.intProjectID 
				INNER JOIN users u on u.id=atit.intCreaterID
				LEFT JOIN (select DISTINCT intTimerTaskID,chrBrowserNames 
				from auto_task_execs where intFlag=0)ate on ate.intTimerTaskID=atit.id
				where $search $wl and atit.intCompanyID=$user->intCompanyID and atit.intFlag=0 order by atit.id desc limit ?,?", [
            $pagecount,
            $iDisplayLength
        ]);
        $tiTasks .= json_encode($rows);
        $tiTasks .= "}";
        return $tiTasks;
    }

    /**
     *
     * @param unknown $titask
     * @param unknown $user
     */
    public function insert($titask, $user)
    {
        DB::beginTransaction();
        try {
            $titask_model = new AutoTimerTask ();
            $titask_model->chrTiTaskName = $titask ["titaskName"];
            $titask_model->intProjectID = $titask ["projectId"];
            $titask_model->intTiTaskTypeID = $titask ["titaskType"];
            $titask_model->intCreaterID = $titask_model->intModifyID = $user->id;
            $titask_model->intCompanyID = $user->intCompanyID;
            $titask_model->intFlag = 1;
            $titask_model->save();

            $titaskId = $titask_model->id;
            DB::insert("insert into auto_timer_task_relations (intTiTaskID,chrExecBrowserIds,chrEmails,intExecRateID,
					dtExecBeginDate,dtExecEndDate,chrExecTime,intState,intCompanyID) values (?,?,?,?,?,?,?,?,?)", [
                $titaskId,
                implode(";", $titask ["selBrowsers"]),
                $titask ["emails"],
                $titask ["execRate"],
                $titask ["execBeginDate"],
                $titask ["execEndDate"],
                $titask ["execTime"],
                0,
                $user->intCompanyID
            ]);
            foreach ($titask ["taskIds"] as $taskId) {
                DB::insert("insert into auto_timer_relate_tasks (intTiTaskID,intTaskID,intCreaterID,intModifyID,intCompanyID) 
						values (?,?,?,?,?)", [
                    $titaskId,
                    $taskId,
                    $user->id,
                    $user->id,
                    $user->intCompanyID
                ]);
            }
            DB::commit();
            return $titaskId;
        } catch (\Exception $e) {
            DB::rollback();
            throw $e;
        }
    }

    public function updateFlag($tiTaskId)
    {
        DB::update("update auto_timer_tasks set intFlag=0 where id=$tiTaskId");
    }

    /**
     *
     * @param unknown $ids
     * @param unknown $user
     * @throws Exception
     */
    public function delete($ids, $user)
    {
        DB::beginTransaction();
        try {
            // 删除队列相关
            DB::delete("delete from auto_jobs where intExecTaskID in (
				select id from auto_task_execs where intTimerTaskID in ($ids))");
            // 删除任务执行情况
            DB::delete("delete from auto_task_execs where intTimerTaskID in ($ids) and intCompanyID=$user->intCompanyID");
            // 删除报告相关
            DB::delete("delete from auto_reports where intTaskID in ($ids) and intTaskType=2");
            // 删除定时任务相关
            DB::delete("delete from auto_timer_relate_tasks where intTiTaskID in ($ids) and intCompanyID=$user->intCompanyID");
            DB::delete("delete from auto_timer_task_relations where intTiTaskID in ($ids) and intCompanyID=$user->intCompanyID");
            DB::delete("delete from auto_timer_tasks where id in ($ids) and intCompanyID=$user->intCompanyID");
            DB::commit();
        } catch (\Exception $e) {
            DB::rollback();
            throw $e;
        }
    }

    /**
     */
    public function getTimerJobState($id, $user)
    {
        return DB::select("SELECT aj.id,aj.intBrowserID browserId,aj.tPayload payload,aj.tintState state,ate.id execId
				from auto_jobs aj
				INNER JOIN auto_task_execs ate on ate.id=aj.intExecTaskID and ate.intTimerTaskID=$id
				where ate.intCompanyID=$user->intCompanyID
				ORDER BY aj.tintState desc");
    }

    /**
     *
     * @param unknown $jobs
     * @param unknown $selBrowsers
     */
    private function updateJobsBrowser($jobs, $selBrowsers)
    {
        $jobIds = array();
        $delBrowsers = array();
        foreach ($jobs as $job) {
            $browserId = $job->browserId;
            array_push($jobIds, $job->id);
            if (($index = array_search($browserId, $selBrowsers)) === false) {
                array_push($delBrowsers, $browserId); // 需要删除的ids
            }
        }
        foreach ($selBrowsers as $key => $selBrowser) {
            foreach ($jobs as $jk => $job) {
                if ($job->browserId == $selBrowser) {
                    unset ($selBrowsers [$key]);
                }
            }
        }
        $selBrowsers = array_filter($selBrowsers); // 去空
        $jobIds = implode(',', $jobIds);
        foreach ($selBrowsers as $selBrowser) { // 插入不存在的浏览器
            DB::statement("insert into auto_jobs (intBrowserID,intExecTaskID,tPayload,tintState) 
			select $selBrowser,intExecTaskID,tPayload,0 from auto_jobs
			where intBrowserID=$browserId and id in ($jobIds)");
        }
        if (!empty ($delBrowsers)) {
            $delBrowsers = implode(',', $delBrowsers);
            DB::delete("delete from auto_jobs where intBrowserID in ($delBrowsers) and id in ($jobIds)");
        }
        return explode(',', $jobIds);
    }

    /**
     *
     * @param unknown $timer
     * @param unknown $oldTimer
     * @param unknown $jobIds
     */
    private function updateJobsPayload($jobs, $timer, $oldTimer)
    {
        if ($timer ["execRate"] != $oldTimer ["execRate"] || $timer ["execTime"] != $oldTimer ["execTime"] || $timer ["execBeginDate"] != $oldTimer ["execBeginDate"] || $timer ["execEndDate"] != $oldTimer ["execEndDate"]) {
            foreach ($jobs as $job) {
                $payload = json_decode($job->payload, true);
                $payload ["timer"] = $timer;
                DB::update("update auto_jobs set tPayload=? where id=$job->id", [
                    json_encode($payload)
                ]);
            }
        }
    }

    /**
     *
     * @param unknown $selBrowsers
     * @param unknown $execId
     * @param unknown $payload
     */
    private function inserJobs($selBrowsers, $execId, $payload)
    {
        foreach ($selBrowsers as $browser) {
            // 放入队列中等待分配机器执行
            DB::insert("insert into auto_jobs (intBrowserID,intExecTaskID,tPayload) values (?,?,?)", [
                $browser,
                $execId,
                json_encode($payload)
            ]);
        }
    }

    /**
     *
     * @param unknown $id
     * @param unknown $taskIds
     * @param unknown $oldTaskIds
     * @param unknown $selBrowsers
     * @param unknown $emails
     * @param unknown $payload
     * @param unknown $timer
     */
    private function updateJobsTaskExec($id, $taskIds, $oldTaskIds, $selBrowsers, $emails, $timer, $user)
    {
        $existIds = array();
        foreach ($taskIds as $taskId) {
            if (($key = array_search($taskId, $oldTaskIds)) === FALSE) {
                DB::insert("insert into auto_timer_relate_tasks (intTiTaskID,intTaskID) values (?,?)", [
                    $id,
                    $taskId
                ]);
                DB::insert("insert into auto_task_execs (intTimerTaskID,intTaskID,chrBrowserIDs,chrEmails,intCreaterID,intState)
						values (?,?,?,?,?,?)", [
                    $id,
                    $taskId,
                    $selBrowsers,
                    $emails,
                    $user->id,
                    0
                ]);
                $rows = DB::select("select @@identity as autoID from auto_task_execs");
                $execId = $rows [0]->autoID;
                $payload = array(
                    'taskId' => $taskId,
                    'execTaskId' => $execId,
                    'tiTaskId' => $id,
                    'timer' => $timer
                );
                $selBrowsers = explode(";", $selBrowsers);
                $this->inserJobs($selBrowsers, $execId, $payload);
            } else {
                $existIds [] = $taskId;
                array_splice($oldTaskIds, $key, 1); // 删除存在的
            }
        }
        if (!empty ($oldTaskIds)) {
            $delIds = implode(',', $oldTaskIds);
            DB::delete("delete from auto_timer_relate_tasks where intTiTaskID=$id and intTaskID in ($delIds)");
            DB::delete("delete from auto_jobs where intExecTaskID in (
			select id from auto_task_execs where intTimerTaskID=$id and intTaskID in ($delIds))");
        }
        return $existIds;
    }

    /**
     *
     * @param unknown $id
     * @param unknown $tiTask
     * @param unknown $user
     * @param unknown $payload
     */
    public function update($id, $tiTask, $user, $jobs)
    {
        DB::beginTransaction();
        try {
            $timer = array(
                "execRate" => $tiTask ["execRate"],
                "execTime" => $tiTask ["execTime"],
                "execBeginDate" => $tiTask ["execBeginDate"],
                "execEndDate" => $tiTask ["execEndDate"],
                "lastDate" => ""
            );
            if (!empty ($jobs)) {
                $jobIds = $this->updateJobsBrowser($jobs, $tiTask ["selBrowsers"]); // 更新任务队列中不存在的浏览器
                $payload = json_decode($jobs [0]->payload, true);
                $oldTimer = $payload ["timer"];
                $timer ["lastDate"] = $oldTimer ["lastDate"];
                // 更新存在队列的payload
                $this->updateJobsPayload($jobs, $timer, $oldTimer);
            }
            $selBrowsers = implode(";", $tiTask ["selBrowsers"]);
            $emails = $tiTask ["emails"];
            // 更新任务相关
            DB::update("update auto_timer_tasks set chrTiTaskName=?,intTiTaskTypeID=?,intModifyID=?,intProjectID=? 
					where id=? and intCompanyID=?", [
                $tiTask ["titaskName"],
                $tiTask ["titaskType"],
                $user->id,
                $tiTask ["projectId"],
                $id,
                $user->intCompanyID
            ]);
            DB::update("update auto_timer_task_relations set chrExecBrowserIds=?,chrEmails=?,intExecRateID=?,
			dtExecBeginDate=?,dtExecEndDate=?,chrExecTime=? where intTiTaskID=? and  intCompanyID=?", [
                $selBrowsers,
                $emails,
                $tiTask ["execRate"],
                $tiTask ["execBeginDate"],
                $tiTask ["execEndDate"],
                $tiTask ["execTime"],
                $id,
                $user->intCompanyID
            ]);
            $taskIds = $tiTask ["taskIds"];
            $oldTaskIds = $tiTask ["oldTaskIds"];
            $existIds = $this->updateJobsTaskExec($id, $taskIds, $oldTaskIds, $selBrowsers, $emails, $timer, $user); // 任务队列更新
            if (empty ($jobs) && !empty ($existIds)) {
                // 将原有存在的task插入到队列任务中
                $existIds = implode(",", $existIds);
                $rows = DB::select("select id,intTaskID from auto_task_execs 
						where intTimerTaskID=$id and intTaskID in ($existIds) and intFlag=0 and intCompanyID=$user->intCompanyID ");
                foreach ($rows as $row) {
                    $payload = array(
                        'taskId' => $row->intTaskID,
                        'execTaskId' => $row->id,
                        'tiTaskId' => $id,
                        'timer' => $timer
                    );
                    $browsers = explode(";", $selBrowsers);
                    $this->inserJobs($browsers, $row->id, $payload);
                }
            }
            DB::commit();
        } catch (\Exception $e) {
            DB::rollback();
            throw $e;
        }
    }

    /**
     *
     * @param unknown $id
     */
    public function show($id, $user)
    {
        return DB::select("select atit.chrTiTaskName titaskName,atit.intTiTaskTypeID titaskType,atitr.chrExecBrowserIds execBrowserIds,
				atitr.chrEmails emails,ats.id,ats.chrTaskName taskName,atitr.chrExecTime execTime,atitr.dtExecBeginDate execBeginDate,
				atitr.dtExecEndDate execEndDate,atitr.intExecRateID execRate,atit.intProjectID projectId 
				from auto_timer_tasks atit
				INNER JOIN auto_timer_task_relations atitr on atitr.intTiTaskID=atit.id
				INNER JOIN auto_timer_relate_tasks atrt on atrt.intTiTaskID=atit.id
				INNER JOIN auto_tasks ats on ats.id=atrt.intTaskID
				where atit.id=$id and ats.intCompanyID=$user->intCompanyID");
    }
}

?>