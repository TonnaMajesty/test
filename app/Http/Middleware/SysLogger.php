<?php


namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Auth;
use App\Services\SystemLogService;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

class SysLogger {
	
	/**
	 * Handle an incoming request.
	 *
	 * @param \Illuminate\Http\Request $request        	
	 * @param \Closure $next        	
	 * @return mixed
	 */
	public function handle($request, Closure $next) {
		$user = Auth::user ();
		$ylogService = new SystemLogService ();
		try {
			$response = $next ( $request );
			$ylogService->save ( $request, 1, $user ); // 成功日志
			return $response;
		} catch ( \Exception $e ) {
			// 失败日志
			$error = array (
					"message" => $e->getMessage (),
					"file" => $e->getFile (),
					"line" => $e->getLine () 
			);
			if ($e instanceof NotFoundHttpException) {
				$error ["code"] = $e->getStatusCode ();
				$error ["exception"] = "NotFoundHttpException";
			} else {
				$error ["code"] = $e->getCode ();
				$start = 11;
				$end = strpos ( $e, "with" );
				$length = $end - $start - 2;
				$error ["exception"] = substr ( $e, $start, ($length > 0) ? $length : 0 );
			}
			$ylogService->save ( $request, json_encode ( $error ), $user );
			throw $e;
		}
		return $next ( $request );
	}
}
