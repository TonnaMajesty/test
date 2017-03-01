<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;

class AutoBrowserService {
	/**
	 * 获取所有浏览器
	 */
	public function getBrowsers() {
		return DB::select ( "select id,chrBrowserName as browserName,chrBrowserENName browserENName from auto_exec_browsers where intFlag=0" );
	}
	
	/**
	 * 根据浏览器ID 查询指定的某些浏览器
	 *
	 * @param unknown $browserIds        	
	 */
	public function getBrowserByID($browserIds) {
		return DB::select ( "select id,chrBrowserENName browserENName from auto_exec_browsers
				where id in ($browserIds)" );
	}
	
}

?>