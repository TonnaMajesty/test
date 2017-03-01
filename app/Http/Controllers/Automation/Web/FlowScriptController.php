<?php

namespace App\Http\Controllers\Automation\Web;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\UEUploadService;
use Illuminate\Support\Facades\Log;
use App\Services\FlowProcessService;
use Illuminate\Support\Facades\Auth;
use App\Services\FlowService;

class FlowScriptController extends Controller {
	
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
	public function store() {
		//
	}
	
	/**
	 * Display the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function show($id) {
		//
		var_dump ( "show--" . $id );
		return view ( 'automation.web.flowscript' );
	}
	
	/**
	 * Show the form for editing the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function edit($id) {
		//
		var_dump ( "edit--" . $id );
		return view ( 'automation.web.flowscript' );
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
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function uploader(Request $request) {
		try {
			if (! isset ( $_GET ['action'] ))
				return view ( "common.webuploader.webuploader" );
			$filepath = base_path () . '\config\webuploader\uploaderscript.json';
			$CONFIG = json_decode ( preg_replace ( "/\/\*[\s\S]+?\*\//", "", file_get_contents ( $filepath ) ), true );
			$action = $_GET ['action'];
			switch ($action) {
				case 'config' :
					$result = json_encode ( $CONFIG );
					break;
				/* 上传文件 */
				case 'uploadfile' :
					$uploader = new UEUploadService ();
					$result = $uploader->uploadfile ( $action, $CONFIG );
					$result = json_encode ( $result );
					break;
				default :
					$result = json_encode ( array (
							'state' => '请求地址出错' 
					) );
					break;
			}
		} catch ( \Exception $e ) {
			throw ($e);
		}
		
		/* 输出结果 */
		if (isset ( $_GET ["callback"] )) {
			if (preg_match ( "/^[\w_]+$/", $_GET ["callback"] )) {
				echo htmlspecialchars ( $_GET ["callback"] ) . '(' . $result . ')';
			} else {
				echo json_encode ( array (
						'state' => 'callback参数不合法' 
				) );
			}
		} else {
			echo $result;
		}
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
		Log::info ( $processinfo );
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
