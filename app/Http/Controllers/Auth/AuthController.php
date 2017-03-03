<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Contracts\Auth\Guard;
use Illuminate\Contracts\Auth\Registrar;
use Illuminate\Foundation\Auth\AuthenticatesAndRegistersUsers;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use App\Services\UserService;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Session;
use App\Services\VerifyService;
use App\Services\TelEmailService;
use App\Utils\RegHelper;
use App\Services\AuthMenuService;
use Illuminate\Support\Facades\Auth;

class AuthController extends Controller {
	
	/*
	 * |-------------------------------------------------------------------------- | Registration & Login Controller |-------------------------------------------------------------------------- | | This controller handles the registration of new users, as well as the | authentication of existing users. By default, this controller uses | a simple trait to add these behaviors. Why don't you explore it? |
	 */
	
	use AuthenticatesAndRegistersUsers;
	
	/**
	 * Create a new authentication controller instance.
	 *
	 * @param \Illuminate\Contracts\Auth\Guard $auth        	
	 * @param \Illuminate\Contracts\Auth\Registrar $registrar        	
	 * @return void
	 */
	public function __construct(Guard $auth, Registrar $registrar) {
		$this->auth = $auth;
		$this->registrar = $registrar;
		
		$this->middleware ( 'guest', [ 
				'except' => 'getLogout' 
		] );
	}
	
	/**
	 * Show the application login form.
	 *
	 * @return \Illuminate\Http\Response
	 */
	public function getLogin() {
		return view ( 'auth.login' );
	}
	
	public function getIndex() {
		$user=Auth::user();
		$pages=array();
		if(!empty($user)){
			$pages["login"]="1";
		}
		return view ( 'campaign.index' )->with($pages);
	}
	
	/**
	 * 发送验证码
	 *
	 * @param Request $request        	
	 */
	public function postSendcheckcode(Request $request) {
		try {
			// 需要配置config/mail.php和文件.evn
			$receiver = $request->input ( 'receiver' );
			$verifService = new VerifyService ();
			$temService = new TelEmailService ();
			$userService = new UserService ();
			if (RegHelper::validateEmail ( $receiver )) 			// 邮箱
			{
				$code = $verifService->getTelEmailCode ( $receiver );
				if ($userService->uniqueEmail ( $receiver ) == 0)
					$temService->sendEmailVerify ( $code, $receiver );
				else
					return $this->registerFail ( "邮箱被注册" );
			} else if (RegHelper::validateTel ( $receiver )) 			// 手机
			{
				$code = $verifService->getTelEmailCode ( $receiver );
				if ($userService->uniqueTel ( $receiver ) == 0)
					$temService->sendTelVerify ( $code, $receiver );
				else
					return $this->registerFail ( "手机被注册" );
			}
			return $this->registerSuccess ( '' );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	/**
	 * 注册
	 *
	 * @param Request $request        	
	 * @return Ambigous <\Illuminate\Routing\Redirector, \Illuminate\Http\RedirectResponse, mixed, \Illuminate\Container\static>
	 */
	public function postRegister(Request $request) {
		try {
			$step = $request->input ( 'stepcode' );
			$email = $request->input ( 'email' ); // 注册帐号
			$reqcheckcode = $request->input ( 'checkcode' ); // 手机、邮箱验证码
			$tel = $request->input ( 'tel' ); // 手机、邮箱验证码
			$temService = new TelEmailService (); // 验证码验证类
			$msg = $temService->verTelEmailCodeValidate ( $reqcheckcode, $email ); // 验证手机邮件校验码
			if (! $msg) { // 返回空字符串表示验证通过
				/*
				 * $reqaccount = $request->input ( 'tel' ); if ($userService->uniqueTel ( $reqaccount ) != 0) $msg = "手机已被抢注";
				 */
				/*
				 * $reqaccount = $request->input ( 'username' ); if (($userService->uniqueUserName ( $reqaccount ) != 0)) $msg = "帐号已被注册";
				 */
				$userService = new UserService ();
				if ($userService->uniqueEmail ( $email ) != 0)
					$msg = "邮箱已被抢注";
				if (! $msg) {
					$udata = $request->all ();
					$udata ['password'] = bcrypt ( $udata ['password'] );
					$user = $this->registrar->create ( $udata ); // 注册
					if ($user) {
						// 登录
						$this->auth->login ( $user );
						// 存储用户、角色session信息
						$this->setUserAuthSession ();
					}
					Session::forget ( 'regcache' );
					return $this->registerSuccess ( '/' );
				}
			}
			return $this->registerFail ( $msg );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	// 重写 登录
	public function postLogin(Request $request) {
		try {
			$vercode = $request->input ( 'vercode' );
			$temService = new TelEmailService ();
			$msg = $temService->verImgCodeValidate ( $vercode ); // 验证图片校验码                          
			if (! $msg) { // 返回""则表示验证通过
				$email = $request->input ( 'email' );
				$pwd = $request->input ( 'password' );
				$credentials = array (
						// "chrEmail" => $email,
						// "password" => $pwd
						"chrEmail" => 'zhangfjb1@yonyou.com',
						"password" => '111111'
						 
				);
				if ($this->auth->attempt ( $credentials, $request->has ( 'remember' ) )) {
					// 存储用户、角色session信息
					$this->setUserAuthSession ();
					return response ()->json ( array (
							'success' => 1,
							'mgs' => 'ok',
							'url' => "" 
					) );
				}
				/*
				 * $userService = new UserService (); $user = $userService->getUser ( $email ); if (! empty ( $user )) { // 登录成功 if (Hash::check ( $pwd, $user->chrPassword )) { Session::put ( "user", $user ); // 登录成功以后存入session["bsuser"]中 return response ()->json ( array ( 'success' => 1, 'mgs' => 'ok', 'url' => "/desktop" ) ); } }
				 */
				// 登录失败
				return $this->registerFail ( "用户名或密码错误" );
			}
			return $this->registerFail ( $msg );
		} catch ( \Exception $e ) {
			throw $e;
		}
	}
	
	/**
	 * 注册失败返回的json信息
	 *
	 * @param unknown $msg        	
	 * @return string
	 */
	private function registerFail($msg) {
		return "{success:0,error:'{$msg}'}";
	}
	
	/**
	 * 成功返回的json信息
	 *
	 * @param unknown $url        	
	 * @return string
	 */
	private function registerSuccess($url) {
		return "{success:1,url:'{$url}'}";
	}
	/**
	 * 注册、登录时将用户信息以及权限信息存入到session中
	 *
	 * @param unknown $user        	
	 */
	private function setUserAuthSession() {
		$key = "auth";
		$user = Auth::user ();
		$amService = new AuthMenuService (); // 获取模块（即菜单）信息
		$user->menuAuths = $amService->getMenuAuths ( $user );
		$user->btnAuths = $amService->getButtonAuths ( $user );
		$user->dataAuths = $amService->getDataAuths ( $user );
		Session::put ( $key, $user );
		/*
		 * $redis = RedisHelper::getInstance (); $redis->zIncrBy ( "ulogin", 1, $user->id );
		 */
		// $redis->hSet ( "auth.menuAuths", $user->id, $user->menuAuths );
	}
}
