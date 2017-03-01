<?php

namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\RoleService;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;

class RoleController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view ( "systemsettings.role" );
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
		$roleName = $request->input ( 'roleName' );
		$desc = $request->input ( 'desc' );
		$user = $request->user ();
		$role = array (
				"roleName" => $roleName,
				"roleDesc" => $desc 
		);
		$roleService = new RoleService ();
		$roleService->insert ( $role, $user );
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
	public function edit(Request $request, $id) {
		//
		$roleService = new RoleService ();
		$role = $roleService->show ( $id, $request->user () );
		return "{success:1,data:" . json_encode ( $role ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update(Request $request, $id) {
		//
		$roleName = $request->input ( 'roleName' );
		$desc = $request->input ( 'desc' );
		$user = $request->user ();
		$role = array (
				"roleName" => $roleName,
				"roleDesc" => $desc 
		);
		$roleService = new RoleService ();
		$roleService->update ( $id, $role, $user );
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
		$roleService = new RoleService ();
		$roleService->delete ( $ids, $request->user () );
		return "{success:1}";
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function getList(Request $request) {
		try {
			$secho = $request->input ( 'sEcho' );
			$iDisplayStart = $request->input ( 'iDisplayStart' );
			$iDisplayLength = $request->input ( 'iDisplayLength' );
			$user = $request->user ();
			$roleService = new RoleService ();
			return $roleService->getRoleList ( $secho, $iDisplayStart, $iDisplayLength, $user );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	/**
	 * 获取Role树
	 *
	 * @param Request $request        	
	 */
	public function getRoleTree(Request $request) {
		$nodeId = $request->input ( 'id' );
		if (empty ( $nodeId )) {
			$roleService = new RoleService ();
			$roles = $roleService->getRoleTree ( $request->user () );
			return json_encode ( $roles );
		}
	}
}
