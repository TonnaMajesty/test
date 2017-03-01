<?php

namespace App\Http\Controllers\Design;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Auth;
use App\Services\FlowService;
use App\Services\FlowProcessService;

class FlowDesignController extends Controller {
	
	public function scriptEdit(){
		return view('automation.web.flowscript_edit' );
	}
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		return view ( 'design.flowscript' );
	}
	
	/**
	 * 获取流程脚本
	 *
	 * @param Request $request        	
	 * @return string
	 */
	public function getFlowProcess(Request $request) {
		$flowid = $request->input ( 'flowid', 1 );
		$fproService = new FlowProcessService ();
		$processData = $fproService->getFlowProcess ( $flowid );
		return "{success:1,processData:" . json_encode ( $processData ) . "}";
	}
	
	/**
	 * 添加流程单
	 *
	 * @param Request $request        	
	 */
	public function addFlow(Request $request) {
		$user = Auth::user ();
		$flows = $request->all ();
		$flowService = new FlowService ();
		$flowService->addFlow ( $flows, $user );
	}
	
	/**
	 * 保存流程步骤面板的所有信息
	 *
	 * @param Request $request        	
	 */
	public function saveFlowProcess(Request $request) {
		$flowprocess = $request->input ( 'flowprocess' );
		$flowprocess = json_decode ( $flowprocess, true );
		$fproService = new FlowProcessService ();
		foreach ( $flowprocess as $processid => $process ) {
			$process ['processTo'] = implode ( ",", $process ["process_to"] );
			$fproService->updateProcess ( $process, $processid ); // 更新流程步骤的信息
		}
		return "{success:1}";
	}
	
	/**
	 * 添加步骤
	 *
	 * @param Request $request        	
	 */
	public function addProcess(Request $request) {
		$process = $request->all ();
		$user = Auth::user ();
		$fproService = new FlowProcessService ();
		$processinfo = $fproService->addProcess ( $process, $user );
		Log::info($processinfo);
		return "{success:1,info:" . json_encode ( $processinfo ) . "}";
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function delProcess(Request $request) {
		$processid = $request->input ( 'processid' );
		$fproService = new FlowProcessService ();
		$fproService->delProcess ( $processid );
	}
}
