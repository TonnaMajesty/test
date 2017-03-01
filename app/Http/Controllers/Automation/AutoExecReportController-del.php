<?php

namespace App\Http\Controllers\Automation;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Services\AutoExecReportService;
use Illuminate\Support\Facades\Log;

class AutoExecReportController_del extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index(Request $request) {
		//
		$user = Auth::user ();
		$aerService = new AutoExecReportService ();
		$taskType = $request->input ( 'taskType' );
		$keyId = $request->input ( 'keyId' );
		switch ($taskType) {
			case 1 : // 普通任务和虚拟
				$rows = $aerService->getTaskExecReportStep ( $keyId, $user, 1 );
				break;
			case 2 : // 定时任务
				$rows = $aerService->getTimerTaskExecReportStep ( $keyId, $user, 1 );
				break;
		}
		$pages = array (
				"step" => (empty ( $rows ) ? "" : $rows [0]),
				"taskType" => $taskType,
				"keyId" => $keyId 
		);
		return view ( "automation.report.report" )->with ( $pages );
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
	public function store() {
		//
	}
	
	/**
	 * Display the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function show(Request $request, $keyId) {
		//
		$user = Auth::user ();
		$aerService = new AutoExecReportService ();
		$taskType = $request->input ( 'taskType' );
		switch ($taskType) {
			case 1 : // 普通任务
				$rows = $aerService->getTaskExecReportStep ( $keyId, $user );
				break;
			case 2 : // 定时任务
				$rows = $aerService->getTimerTaskExecReportStep ( $keyId, $user );
				break;
		}
		if (! empty ( $rows ))
			return "{success:1,data:" . json_encode ( $rows ) . "}";
		return "{success:0,error:'报告未生成，暂时不能查看'}";
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
