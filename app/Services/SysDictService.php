<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;

class SysDictService {
	
	/**
	 *
	 * @param unknown $dicName        	
	 */
	public function getDictsByName($dictName) {
		return DB::select ( "select * from sys_dicts where chrDictName='$dictName'" );
	}
	
	/**
	 *
	 * @return multitype:multitype:string
	 */
	public function getTaskExecState() {
		$states = array (
				array (
						"id" => "",
						"state" => "未执行" 
				),
				array (
						"id" => "0",
						"state" => "排队中" 
				),
				array (
						"id" => "1",
						"state" => "执行中" 
				),
				array (
						"id" => "2",
						"state" => "执行成功" 
				),
				array (
						"id" => "3",
						"state" => "执行失败" 
				) 
		);
		return $states;
	}
}

?>