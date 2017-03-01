<?php

namespace App\Http\Controllers\Automation\Web;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AutoTaskService;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Auth;
use App\Services\AutoTaskExecService;
use App\Services\ProjectService;
use App\Services\SysDictService;

class AutoTaskController extends Controller {
	
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
		return view ( "automation.web.autotask" )->with ( $pages );
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
		//
		$user = $request->user ();
		$task = $request->all ();
		$atService = new AutoTaskService ();
		$atService->insert ( $task, $user );
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
	public function edit(Request $request, $id) {
		//
		$user = $request->user ();
		$atService = new AutoTaskService ();
		$task = $atService->getTaskById ( $id, $user );
		return "{success:1,task:" . json_encode ( $task ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update(Request $request, $id) {
		//
		$task = $request->all ();
		$ateService = new AutoTaskExecService ();
		$rows = $ateService->getTaskExecState ( $id );
		if (empty ( $rows )) {
			$user = $request->user ();
			$atService = new AutoTaskService ();
			$atService->update ( $id, $task, $user );
		} else
			return "{success:0,error:'任务正在运行，已锁定...'}";
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
		$atService = new AutoTaskService ();
		$atService->delete ( $id, $user );
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function getTaskList(Request $request) {
		$proService = new ProjectService ();
		$wl = $proService->getProjectDataAuth ();
		$secho = $request->input ( 'sEcho' );
		$iDisplayStart = $request->input ( 'iDisplayStart' );
		$iDisplayLength = $request->input ( 'iDisplayLength' );
		$search = json_decode ( $request->input ( 'search' ), true );
		$user = $request->user ();
		$atService = new AutoTaskService ();
		return $atService->getTaskList ( $secho, $iDisplayStart, $iDisplayLength, $user, $search ,$wl);
	}
}
