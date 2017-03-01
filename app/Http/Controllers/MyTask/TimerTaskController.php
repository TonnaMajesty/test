<?php

namespace App\Http\Controllers\MyTask;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\TimerTaskService;
use App\Services\SysDictService;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Auth;
use App\Services\AutoTaskExecService;
use App\Services\ProjectService;

class TimerTaskController extends Controller
{

    /**
     * Display a listing of the resource.
     *
     * @return Response
     */
    public function index(Request $request)
    {
        //
        $user = $request->user();
        $sdService = new SysDictService ();
        $taskTypes = $sdService->getDictsByName("titasktype");
        $rates = $sdService->getDictsByName("execrate");
        $proService = new ProjectService ();
        $projects = $proService->getProjectTree($user);
        $sdService = new SysDictService ();
        $states = $sdService->getTaskExecState();
        $states = array_splice($states, 1, count($states) - 1);
        $pages = array(
            "tasktypes" => $taskTypes,
            "rates" => $rates,
            "projects" => $projects,
            "states" => $states
        );
        return view("mytask.timertask")->with($pages);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @return Response
     */
    public function store(Request $request)
    {
        //
        $titask = $request->all();
        if (!empty ($titask ["taskIds"])) {
            $ttService = new TimerTaskService ();
            $user = $request->user();
            $tiTaskId = $ttService->insert($titask, $user);
            // 将任务放入队列
            $ateService = new AutoTaskExecService ();
            $execInfo = array(
                "taskId" => implode(";", $titask ["taskIds"]),
                "selBrowsers" => $titask ["selBrowsers"],
                "emails" => $titask ["emails"]
            );
            $rows = $ateService->getTiTaskExecStateByUser($tiTaskId, $user);
            if (empty ($rows)) { // 若不存在正在执行的定时任务
                $timer = array(
                    "execRate" => $titask ["execRate"],
                    "execTime" => $titask ["execTime"],
                    "execBeginDate" => $titask ["execBeginDate"],
                    "execEndDate" => $titask ["execEndDate"],
                    "lastDate" => ""
                );
                $ret = $ateService->insert($execInfo, $user, $tiTaskId, $timer);
                $ttService->updateFlag($tiTaskId);
                return "{success:1}";
            } else
                return "{success:0,error:'任务正在运行，已锁定...'}";
        }
        return "{success:0,error:'请选择任务'}";
    }

    /**
     * Display the specified resource.
     *
     * @param int $id
     * @return Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param int $id
     * @return Response
     */
    public function edit(Request $request, $id)
    {
        //
        $user = $request->user();
        $ttService = new TimerTaskService ();
        $tiTasks = $ttService->show($id, $user);
        return "{success:1,data:" . json_encode($tiTasks) . "}";
    }

    /**
     * Update the specified resource in storage.
     *
     * @param int $id
     * @return Response
     */
    public function update(Request $request, $id)
    {
        //
        $user = $request->user();
        $tiTask = $request->all();
        $ttService = new TimerTaskService ();
        $jobs = $ttService->getTimerJobState($id, $user);
        if (!empty ($jobs) && $jobs [0]->state) { // 正在执行
            return "{success:0,error:'定时任务正在执行，暂时不允许更改'}";
        } else { // 定时任务在队列中处于排队过程中
            $ttService->update($id, $tiTask, $user, $jobs);
        }
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param int $id
     * @return Response
     */
    public function destroy(Request $request, $ids)
    {
        //
        $user = $request->user();
        $titService = new TimerTaskService ();
        $titService->delete($ids, $user);
    }

    /**
     *
     * @param Request $request
     */
    public function getTimerTaskList(Request $request)
    {
        $proService = new ProjectService ();
        $wl = $proService->getProjectDataAuth();
        $user = $request->user();
        $secho = $request->input('sEcho');
        $iDisplayStart = $request->input('iDisplayStart');
        $iDisplayLength = $request->input('iDisplayLength');
        $search = json_decode($request->input('search'), true);
        $titService = new TimerTaskService ();
        return $titService->getTimerTaskList($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl);
    }
}
