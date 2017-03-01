<?php

namespace App\Http\Controllers\Project;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Services\ProductService;
use Illuminate\Support\Facades\Log;
use App\Services\AutoScriptService;
use App\Services\ProjectService;

class ProductController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		$user = Auth::user ();
		return view ( "project.product" );
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
		$projectName = $request->input ( 'name' );
		$parentId = $request->input ( 'pId' );
		$user = $request->user ();
		$project = array (
				"projectName" => $projectName,
				"parentId" => $parentId,
				"memo" => "" 
		);
		$proService = new ProjectService ();
		$asService = new AutoScriptService ();
		$rows = $asService->getScriptByParentLimit ( $parentId, $user );
		if (empty ( $rows ))
			return "{success:1,nodeId:" . $proService->insert ( $project, $user ) . "}";
		else
			return "{success:0,error:'该产品下已存在脚本，不允许创建子产品'}";
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
	public function update($id, Request $request) {
		//
		$projectName = $request->input ( 'name' );
		$user = Auth::user ();
		$project = array (
				"projectName" => $projectName,
				"memo" => "" 
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
	public function destroy($id, Request $request) {
		//
		$user = $request->user ();
		$proService = new ProjectService ();
		$proService->delete ( $id, $user );
		return "{success:1}";
	}
	
	/**
	 * 获取产品树
	 *
	 * @param Request $request        	
	 */
	public function getProductTree(Request $request) {
		$nodeId = $request->input ( 'id' );
		if (! $nodeId) {
			$pduService = new ProjectService ();
			$products = $pduService->getProductTree ( $request->user () );
			return json_encode ( $products );
		}
	}
}
