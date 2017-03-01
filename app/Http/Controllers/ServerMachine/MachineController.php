<?php

namespace App\Http\Controllers\ServerMachine;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\MachineService;
use Illuminate\Support\Facades\Auth;

class MachineController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view ( "servermachine.machine" );
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
		$machine = $request->all ();
		$user = Auth::user ();
		$machService = new MachineService ();
		$machService->insert ( $machine, $user );
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
		$machService = new MachineService ();
		$row = $machService->show ( $id );
		return "{success:1,data:" . json_encode ( $row ) . "}";
	}
	
	/**
	 * Update the specified resource in storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function update(Request $request, $id) {
		//
		$machine = $request->all ();
		$user=Auth::user();
		$machService = new MachineService ();
		$machService->update($machine, $id, $user);
	}
	
	/**
	 * Remove the specified resource from storage.
	 *
	 * @param int $id        	
	 * @return Response
	 */
	public function destroy($ids) {
		//
		$machService = new MachineService ();
		$machService->delete ( $ids );
	}
	
	/**
	 *
	 * @param Request $request        	
	 */
	public function getMachineList(Request $request) {
		try {
			$secho = $request->input ( 'sEcho' );
			$iDisplayStart = $request->input ( 'iDisplayStart' );
			$iDisplayLength = $request->input ( 'iDisplayLength' );
			$machService = new MachineService ();
			return $machService->getMachineList ( $secho, $iDisplayStart, $iDisplayLength );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
}
