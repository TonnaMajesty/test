<?php

namespace App\Services;

use App\SysLog;

class SystemLogService {
	
	/**
	 * 存储日志
	 *
	 * @param unknown $request        	
	 * @param unknown $requestResult        	
	 * @param unknown $user        	
	 */
	public function save($request, $requestResult, $user) {
		try {
			$sysLog = new SysLog ();
			$sysLog->intUserID = $user ? $user->id : 0; // 0表示未登录
			$sysLog->chrUrlRoot = $request->root ();
			$sysLog->chrRoute = $request->path ();
			$sysLog->intAjax = $request->ajax ();
			$sysLog->chrRequestType = $request->method ();
			$sysLog->chrRequestData = json_encode ( $request->all () ); // 将参数加密
			$sysLog->chrAreaIP = $request->ip ();
			$server = $request->server ();
			$sysLog->chrUserAgent = $server ["HTTP_USER_AGENT"];
			$sysLog->chrRequestResult = $requestResult;
			$sysLog->save ();
		} catch ( \Exception $e ) {
			// throw $e;
		}
	}
}

?>