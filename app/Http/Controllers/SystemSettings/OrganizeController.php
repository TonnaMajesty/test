<?php

namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Services\OrganizeService;
use Illuminate\Support\Facades\Log;

class OrganizeController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view ( "systemsettings.organize" );
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
		$orgName = $request->input ( 'name' );
		$parentId = $request->input ( 'pId' );
		$user = $request->user ();
		$org = array (
				"orgName" => $orgName,
				"parentId" => $parentId,
				"memo" => "" 
		);
		$orgService = new OrganizeService ();
		return "{success:1,nodeId:" . $orgService->insert ( $org, $user ) . "}";
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
	public function update(Request $request, $id) {
		//
		$orgName = $request->input ( 'name' );
		$user = Auth::user ();
		$org = array (
				"orgName" => $orgName,
				"memo" => "" 
		);
		$orgService = new OrganizeService ();
		$orgService->update ( $id, $org, $user );
		return "{success:1}";
	}
	
	/**
	 * Remove the specified resource from storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function destroy(Request $request, $id) {
		//
		$orgService = new OrganizeService ();
		$orgService->delete ( $id, $request->user () );
		return "{success:1}";
	}
	
	/**
	 *
	 * @param Request $request        	
	 * @return string
	 */
	public function getOrgTree(Request $request) {
		$nodeId = $request->input ( 'id' );
		if (! $nodeId) {
			$orgService = new OrganizeService ();
			$orgs = $orgService->getOrgTree ( $request->user () );
			return json_encode ( $orgs );
		}
	}
}
