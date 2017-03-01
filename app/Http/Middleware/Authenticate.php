<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Contracts\Auth\Guard;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Session;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

class Authenticate {
	
	/**
	 * The Guard implementation.
	 *
	 * @var Guard
	 */
	protected $auth;
	
	/**
	 * Create a new filter instance.
	 *
	 * @param Guard $auth        	
	 * @return void
	 */
	public function __construct(Guard $auth) {
		$this->auth = $auth;
	}
	
	/**
	 * Handle an incoming request.
	 *
	 * @param \Illuminate\Http\Request $request        	
	 * @param \Closure $next        	
	 * @return mixed
	 */
	public function handle($request, Closure $next) {
		if ($this->auth->guest ()) {
			if ($request->ajax ()) {
				return response ( 'Unauthorized.', 401 );
			} else {
				return redirect ()->guest ( 'auth/login' );
			}
		}
		$pri = $this->judgeOperateAuth ( $request );
		if ($pri) {
			$response = $next ( $request );
			return $response;
		}
	}
	
	/**
	 *
	 * @param unknown $request        	
	 */
	private function judgeOperateAuth($request) {
		/*
		 * $au = $request->input ( 'au' ); if (empty ( $au )) throw new NotFoundHttpException ();
		 */
		return true;
	}
}
