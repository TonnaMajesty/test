<?php


namespace App\Http\Controllers\SystemSettings;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AuthMenuService;
use Illuminate\Support\Facades\Auth;

class MenuController extends Controller {
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		$user = Auth::user ();
		$amService = new AuthMenuService ();
		$menus = $amService->getAllMenus ( $user );
		return view ( "systemsettings.menu" )->withMenus ( $menus );
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
			$secho = $request->input ( 'sEcho' );
			$iDisplayStart = $request->input ( 'iDisplayStart' );
			$iDisplayLength = $request->input ( 'iDisplayLength' );
			$amService = new AuthMenuService ();
			return $amService->getMenuList ( $secho, $iDisplayStart, $iDisplayLength );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	/**
	 * Store a newly created resource in storage.
	 *
	 * @return Response
	 */
	public function store(Request $request) {
		//
		$parentId = $request->input ( 'parentId' );
		$menuAsc = $request->input ( 'menuAsc' );
		$menuName = $request->input ( 'menuName' );
		$menuArgs = $request->input ( 'menuArgs' );
		$memo = $request->input ( 'memo' );
		$user = Auth::user ();
		$menu = array (
				"parentId" => $parentId,
				"menuAsc" => $menuAsc,
				"menuName" => $menuName,
				"menuArgs" => $menuArgs,
				"memo" => $memo 
		);
		$amService = new AuthMenuService ();
		$amService->insert ( $menu, $user );
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
		$amService = new AuthMenuService ();
		$menu = $amService->show ( $id );
		return "{success:1,menu:" . json_encode ( $menu ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update($id, Request $request) {
		//
		$amService = new AuthMenuService ();
		$parentId = $request->input ( 'parentId' );
		$menuAsc = $request->input ( 'menuAsc' );
		$menuName = $request->input ( 'menuName' );
		$menuArgs = $request->input ( 'menuArgs' );
		$memo = $request->input ( 'memo' );
		$menu = array (
				"parentId" => $parentId,
				"menuAsc" => $menuAsc,
				"menuName" => $menuName,
				"menuArgs" => $menuArgs,
				"memo" => $memo 
		);
		$amService->update ( $id, $menu );
		return "{success:1}";
	}
	
	/**
	 * Remove the specified resource from storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function destroy($ids) {
		//
		$amService = new AuthMenuService ();
		$amService->delete ( $ids );
		return "{success:1}";
	}
}
