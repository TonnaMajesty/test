<?php

namespace App\Http\Controllers\Automation\Web;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\FlowProcessService;
use App\Services\FlowService;
use Illuminate\Support\Facades\Auth;
use App\Services\AutoSchemeService;
use App\Utils\HttpHelper;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\DB;
use App\Services\AutoBrowserService;
use App\Services\AutoTaskService;
use App\Services\AutoTaskExecService;
use App\Services\ProjectService;
use App\Services\SysDictService;

class AutoSchemeController extends Controller {
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index(Request $request) {
		//
		$user = $request->user ();
		$proService = new ProjectService ();
		$projects = $proService->getProjectTree ( $user );
		$sdService = new SysDictService ();
		$states = $sdService->getTaskExecState ();
		$pages = array (
				"projects" => $projects,
				"states" => $states 
		);
		return view ( "automation.web.autoscheme" )->with ( $pages );
	}
	
	/**
	 * Show the form for creating a new resource.
	 *
	 * @return Response
	 */
	public function create(Request $request) {
		//
		$ascService = new AutoSchemeService ();
		$schemes = array (
				"schemeName" => $request->input ( 'schemeName' )  // "案例" . time ()
				);
		$user = $request->user ();
		$schemeId = $ascService->insert ( $schemes, $user );
		$pages = array (
				"schemeid" => $schemeId,
				"opt" => 1 
		);
		return view ( 'automation.web.autoscheme_edit' )->with ( $pages );
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
		return view ( 'automation.web.autoscheme_edit' );
	}
	
	/**
	 * Show the form for editing the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function edit($id) {
		$pages = array (
				"schemeid" => $id,
				"opt" => 2 
		);
		return view ( 'automation.web.autoscheme_edit' )->with ( $pages );
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
	public function destroy(Request $request, $id) {
		//
		$user = $request->user ();
		$ascService = new AutoSchemeService ();
		$ascService->delete ( $id, $user );
	}
	
	/**
	 * 获取案例列表F
	 *
	 * @param Request $request        	
	 */
	public function getSchemeList(Request $request) {
		$proService = new ProjectService ();
		$wl = $proService->getProjectDataAuth ();
		$secho = $request->input ( 'sEcho' );
		$iDisplayStart = $request->input ( 'iDisplayStart' );
		$iDisplayLength = $request->input ( 'iDisplayLength' );
		$search = json_decode ( $request->input ( 'search' ), true );
		$user = $request->user ();
		$ascService = new AutoSchemeService ();
		return $ascService->getSchemeList ( $secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl );
	}
	
	/**
	 * 获取流程脚本
	 *
	 * @param Request $request        	
	 * @return string
	 */
	public function getFlowProcess(Request $request, $id) {
		$user = $request->user ();
		$ascService = new AutoSchemeService ();
		$processData = $ascService->getSchemeFlowProcess ( $id, $user );
		return "{success:1,processData:" . json_encode ( $processData ) . "}";
	}
	
	/**
	 * 添加流程单
	 *
	 * @param Request $request        	
	 */
	public function addFlow(Request $request) {
		$user = $request->user ();
		$flows = $request->all ();
		$flowService = new FlowService ();
		$flowService->addFlow ( $flows, $user );
	}
	
	/**
	 * 保存流程步骤面板的所有信息
	 *
	 * @param Request $request        	
	 */
	public function saveFlowProcess(Request $request, $id) {
		$user = $request->user ();
		$ascService = new AutoSchemeService ();
		$projectId = $request->input ( 'projectId' );
		// 案例相关
		$ascService->update ( $projectId, $id, $user );
		// 流程相关
		$flowprocess = $request->input ( 'flowprocess' );
		$flowprocess = json_decode ( $flowprocess, true );
		$fproService = new FlowProcessService ();
		foreach ( $flowprocess as $processid => $process ) {
			foreach ( $process ['process_to'] as $key => $pro ) {
				if (! array_key_exists ( $pro, $flowprocess )) {
					unset ( $process ['process_to'] [$key] );
				}
			}
			array_filter ( $process ["process_to"] );
			$process ['processTo'] = implode ( ",", $process ["process_to"] );
			$fproService->updateProcess ( $process, $processid, $user ); // 更新流程步骤的信息
		}
		$selBrowsers = $request->input ( 'selBrowsers' );
		$abService = new AutoBrowserService ();
		$allBrowsers = $abService->getBrowsers ();
		$ascService->makeSchemePackage ( $id, $selBrowsers, $allBrowsers, $user );
		return "{success:1}";
	}
	
	/**
	 * 添加步骤
	 *
	 * @param Request $request        	
	 */
	public function addProcess(Request $request) {
		$process = $request->all ();
		$user = $request->user ();
		$fproService = new FlowProcessService ();
		$processinfo = $fproService->addProcess ( $process, $user );
		return "{success:1,info:" . json_encode ( $processinfo ) . "}";
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function delProcess(Request $request) {
		$user = $request->user ();
		$processid = $request->input ( 'processid' );
		$fproService = new FlowProcessService ();
		$fproService->delProcess ( $processid, $user );
	}
	
	/**
	 * 下载案例
	 *
	 * @param Request $request        	
	 */
	public function downScheme(Request $request, $id) {
		$user = $request->user ();
		$ascService = new AutoSchemeService ();
		if (! $_GET ["down"]) { // 是否为单纯的下载 即是否通过表单下载
			$selBrowsers = $request->input ( 'selBrowsers' );
			$abService = new AutoBrowserService ();
			$allBrowsers = $abService->getBrowsers ();
			$ascService->makeSchemePackage ( $id, $selBrowsers, $allBrowsers, $user );
		}
		$ascService->makeSchemeZip ( $id, $user );
		$filename = database_path ( 'schemes/zips/' ) . $id . ".zip";
		HttpHelper::download ( $filename );
	}
	
	/**
	 *
	 * @param Request $request        	
	 * @param unknown $id        	
	 */
	public function exec(Request $request, $id) {
		$selBrowsers = $request->input ( 'selBrowsers' );
		$ascService = new AutoSchemeService ();
		$user = Auth::user ();
		$ateService = new AutoTaskExecService ();
		$row = $ateService->getSchemeExecState ( $id, $user ); // 获取是否有正在执行的单独案例
		if (! $row->state) { // 若不存在正在指定的 state=1 正在执行 0 不存在
			$execInfo = array (
					"taskId" => $row->taskID,
					"selBrowsers" => $selBrowsers,
					"emails" => "" 
			);
			$ret = $ateService->insert ( $execInfo, $user );
			return "{success:1}";
		} else
			return "{success:0,error:'案例正在运行，已锁定...'}";
	}
}
