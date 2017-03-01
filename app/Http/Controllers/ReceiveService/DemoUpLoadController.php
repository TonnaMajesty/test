<?php
namespace App\Http\Controllers\ReceiveService;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Http\Utils\demoHelper;

class DemoUpLoadController extends Controller {
	
	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index() {
		//
		return view('updownload.demoload');
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
	public function store() {
		//
		$up = new demoHelper();
		// 设置属性(上传的位置， 大小， 类型， 名是是否要随机生成)
		$up->set ( "path", "./images/" );
		$up->set ( "maxsize", 2000000 );
		$up->set ( "allowtype", array (
				"gif",
				"png",
				"jpg",
				"jpeg" 
		) );
		$up->set ( "israndname", false );
		
		// 使用对象中的upload方法， 就可以上传文件， 方法需要传一个上传表单的名子 pic, 如果成功返回true, 失败返回false
		if ($up->upload ( "pic" )) {
			echo '<pre>';
			// 获取上传后文件名子
			var_dump ( $up->getFileName () );
			echo '</pre>';
		} else {
			echo '<pre>';
			// 获取上传失败以后的错误提示
			var_dump ( $up->getErrorMsg () );
			echo '</pre>';
		}
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
