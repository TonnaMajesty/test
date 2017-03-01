<?php

namespace App\Http;

use Illuminate\Foundation\Http\Kernel as HttpKernel;

class Kernel extends HttpKernel {
	
	/**
	 * The application's global HTTP middleware stack.
	 *
	 * @var array
	 */
	// 若是希望中间件被所有的 HTTP 请求给执行，只要将中间件的类加入到 app/Http/Kernel.php 的 $middleware 属性清单列表中
	protected $middleware = [ 
			'Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode',
			'Illuminate\Cookie\Middleware\EncryptCookies',
			'Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse',
			'Illuminate\Session\Middleware\StartSession',
			'Illuminate\View\Middleware\ShareErrorsFromSession',
			'App\Http\Middleware\VerifyCsrfToken',
			'App\Http\Middleware\SysLogger' 
	];
	
	/**
	 * The application's route middleware.
	 *
	 * @var array
	 */
	// 如果你要指派中间件给特定的路由，你得先将中间件在 app/Http/Kernel.php 配置一个键值，
	// 默认情况下，这个文件内的 $routeMiddleware 属性已包含了 Laravel 目前配置的中间件，你只需要在清单列表中加上一组自定义的键值即可。
	protected $routeMiddleware = [ 
			'auth' => 'App\Http\Middleware\Authenticate',
			'auth.basic' => 'Illuminate\Auth\Middleware\AuthenticateWithBasicAuth',
			'guest' => 'App\Http\Middleware\RedirectIfAuthenticated' 
	];
}
