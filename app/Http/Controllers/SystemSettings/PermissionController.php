<?php

namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\PermissionService;
use Illuminate\Support\Facades\Log;

class PermissionController extends Controller {
	
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
	
	/**
	 * 获取Right树
	 *
	 * @param Request $request        	
	 */
	public function getRightTree(Request $request) {
		$nodeId = $request->input ( 'id' );
		if (! $nodeId) {
			$perService = new PermissionService ();
			$rights = $perService->getRightTree ( $request->user () );
			return json_encode ( $rights );
		}
	}
	/**
	 * 获取Right树
	 *
	 * @param Request $request        	
	 */
	public function getDataRightTree(Request $request) {
		$nodeId = $request->input ( 'id' );
		$perService = new PermissionService ();
		if (! $nodeId) {
			$rights = $perService->getDataRightTree ( $request->user () );
			return json_encode ( $rights );
		} /*
		   * else { switch ($nodeId) { case "ORG" : $rights = $perService->getOrgDataRightTree ( $nodeId, $request->user () ); break; case "PROJECT" : $rights = $perService->getProjectDataRightTree ( $nodeId, $request->user () ); break; } }
		   */
	}
}
