<?php

namespace App\Http\Controllers\Project;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AuthMenuService;
use Illuminate\Support\Facades\Auth;
use App\Services\ProjectService;
use Illuminate\Support\Facades\Session;

class ProjectController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view ( "project.project" );
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
	 *
	 * @param Request $request        	
	 */
	public function getList(Request $request) {
		try {
			$user=$request->user();
			$secho = $request->input ( 'sEcho' );
			$iDisplayStart = $request->input ( 'iDisplayStart' );
			$iDisplayLength = $request->input ( 'iDisplayLength' );
			$proService = new ProjectService ();
			return $proService->getProjectList ( $secho, $iDisplayStart, $iDisplayLength ,$user);
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function getProjectTree(Request $request) {
	}
	
	/**
	 * Store a newly created resource in storage.
	 *
	 * @return Response
	 */
	public function store(Request $request) {
		//
		$projectName = $request->input ( 'projectName' );
		$memo = $request->input ( 'memo' );
		$user = $request->user ();
		$project = array (
				"projectName" => $projectName,
				"parentId" => 0,
				"memo" => $memo 
		);
		$proService = new ProjectService ();
		$proService->insert ( $project, $user );
		return "{success:1}";
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
		$proService = new ProjectService ();
		$project = $proService->show ( $id );
		return "{success:1,project:" . json_encode ( $project ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update(Request $request, $id) {
		//
		$projectName = $request->input ( 'projectName' );
		$memo = $request->input ( 'memo' );
		$user = $request->user ();
		$project = array (
				"projectName" => $projectName,
				"memo" => $memo 
		);
		$proService = new ProjectService ();
		$proService->update ( $id, $project, $user );
		return "{success:1}";
	}
	
	/**
	 * Remove the specified resource from storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function destroy(Request $request, $ids) {
		//
		$user = $request->user ();
		$proService = new ProjectService ();
		$proService->delete ( $ids, $user );
		return "{success:1}";
	}
}
