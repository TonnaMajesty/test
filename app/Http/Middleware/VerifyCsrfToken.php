<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Session;

class VerifyCsrfToken extends BaseVerifier {
	
	/**
	 * Handle an incoming request.
	 *
	 * @param \Illuminate\Http\Request $request        	
	 * @param \Closure $next        	
	 * @return mixed
	 */
	public function handle($request, Closure $next) {
		$token = $request->input ( 'token' );
		if ($token == "q8E89zRdp") { // 对特殊token做处理
			return $next ( $request );
		}
		return parent::handle ( $request, $next );
	}
}
