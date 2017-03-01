<?php

namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Services\UserService;
use Illuminate\Support\Facades\Log;
use App\Services\OrganizeService;
use App\Services\RoleService;

class UserController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index(Request $request) {
		//
		$user = $request->user ();
		$roleService = new RoleService ();
		$roles = $roleService->getRoleTree ( $user );
		$orgService = new OrganizeService ();
		$org = $orgService->getOrgTree ( $user );
		$pages = array (
				"orgs" => $org,
				"roles" => $roles 
		);
		return view ( "systemsettings.user" )->with ( $pages );
	}
	
	/**
	 * Show the form for creating a new resource.
	 *
	 * @return Response
	 */
	public function create(Request $request) {
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
		$employee = $request->all ();
		$userService = new UserService ();
		if ($userService->uniqueEmail ( $employee ["email"] ) == 0) {
			if ($userService->uniqueTel ( $employee ["tel"] ) == 0) {
				$userService->insert ( $employee, $user );
				return "{success:1}";
			} else
				return "{success:0,error:'手机号被占用'}";
		} else
			return "{success:0,error:'邮箱被占用'}";
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
		$userService = new UserService ();
		$employee = $userService->show ( $id, $user );
		return "{success:1,data:" . json_encode ( $employee ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update(Request $request, $id) {
		//
		$user = $request->user ();
		$employee = $request->all ();
		$userService = new UserService ();
		$userService->update ( $id, $employee, $user );
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
		$userService = new UserService ();
		$userService->delete ( $ids, $user );
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
			$userService = new UserService ();
			$user = $request->user ();
			return $userService->getUserList ( $secho, $iDisplayStart, $iDisplayLength, $user );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	/**
	 * 切换用户系统展现
	 *
	 * @param Request $request        	
	 * @return string
	 */
	public function updateUserOSDisplay(Request $request) {
		try {
			$osDisplay = $request->input ( 'osdisplay' );
			$user = Auth::user ();
			$userService = new UserService ();
			$userService->updateUserOSDisplay ( $user, $osDisplay );
			return "success";
		} catch ( \Exception $e ) {
			Log::info ( $e->getMessage () );
		}
		return "{success:1,msg:''}";
	}
}
