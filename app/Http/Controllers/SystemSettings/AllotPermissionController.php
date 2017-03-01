<?php

namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\RoleService;
use Illuminate\Support\Facades\Log;
use App\Services\PriviligeService;
use Illuminate\Support\Facades\Auth;

class AllotPermissionController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view ( "systemsettings.allotpermission" );
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
		$roleId = $request->input ( 'roleId' );
		$funcPerm = $request->input ( 'funcPerm' );
		$dataPerm = $request->input ( 'dataPerm' );
		$pviService = new PriviligeService ();
		$user = Auth::user ();
		$pviService->insert ( $roleId, $funcPerm, $dataPerm, $user );
	}
	
	/**
	 * Display the specified resource.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function show(Request $request, $roleId) {
		//
		$pviService = new PriviligeService ();
		$pvis = $pviService->getPrivilige ( $roleId, $request->user () );
		return "{success:1,data:" . json_encode ( $pvis ) . "}";
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
