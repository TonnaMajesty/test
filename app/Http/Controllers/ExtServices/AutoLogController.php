<?php

namespace App\Http\Controllers\ExtServices;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AutoLogService;
use App\Services\WormQueueService;
use Illuminate\Support\Facades\Log;
use App\Utils\RedisHelper;

class AutoLogController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
	}
	
	/**
	 * Show the form for creating a new resource.
	 *
	 * @return Response
	 */
	public function create() {
		//
	}
	
	/**
	 * Store a newly created resource in storage.
	 *
	 * @return Response
	 */
	public function store(Request $request) {
		// 存储日志
		$logs = $request->all ();
		// $redis=RedisHelper::getInstance();
		// $redis->lPush("autolog",json_encode($logs));
		$scriptId = $logs ["scriptId"]; // 脚本ID
		$schemeId = $logs ["schemeId"]; // 案例ID
		$args = json_decode ( $logs ["uniqueCode"], true ); // log详细信息
		$jobId = $args ["jobId"]; // 工作队列ID
		$reportId = $args ["reportId"];
		$payload = $args ["payload"];
		$browsers = $args ["browsers"];
		$execTaskId = $payload ["execTaskId"]; // 执行任务ID
		$wqService = new WormQueueService ();
		$wqService->moveLogImage ( $logs, $jobId ); // 移动日志图片
		$alogService = new AutoLogService ();
		// 插入日志记录
		$alogService->insert ( $logs, $scriptId, $schemeId, $execTaskId, $jobId, $reportId, $payload, $browsers );
		// 根据回传的日志 更新队列任务以及任务状态
		$wqService->receive ( $jobId, $reportId, $payload, $browsers, $schemeId, $logs ["status"] );
	}
	
	/**
	 * Display the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function show($id) {
		//
	}
	
	/**
	 * Show the form for editing the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function edit($id) {
		//
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update($id) {
		//
	}
	
	/**
	 * Remove the specified resource from storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function destroy($id) {
		//
	}
}
