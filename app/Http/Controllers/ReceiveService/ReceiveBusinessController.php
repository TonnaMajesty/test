<?php

namespace App\Http\Controllers\ReceiveService;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class ReceiveBusinessController extends Controller {
	
	public function getBusinessJson(Request $request) {
		// return "ReceiveBusinessController-getBusinessJson()";
		$serviceId = $request->input ( "serviceId" );
		$json = "[{\"businessId\":\"011110\"},{\"businessId\":\"022220\"}]";
		// $json="[{'businessId':'1111'},{'businessId':'2222'}]";
		return $json;
		// return response ( $json );
		//return view ( "receiveService.businessdata" )->withBusinessjson ( $json );
	}
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		//return "ReceiveBusinessController-index()";
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
}
