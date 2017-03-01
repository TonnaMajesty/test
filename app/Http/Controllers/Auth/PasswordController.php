<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Contracts\Auth\Guard;
use Illuminate\Contracts\Auth\PasswordBroker;
use Illuminate\Foundation\Auth\ResetsPasswords;
use Illuminate\Http\Request;
use App\Services\UserService;
use App\Utils\RegHelper;
use App\User;
use App\Services\TelEmailService;
use App\Services\VerifyService;

class PasswordController extends Controller {
	
	/*
	 * |-------------------------------------------------------------------------- | Password Reset Controller |-------------------------------------------------------------------------- | | This controller is responsible for handling password reset requests | and uses a simple trait to include this behavior. You're free to | explore this trait and override any methods you wish to tweak. |
	 */
	
	use ResetsPasswords;
	
	/**
	 * Create a new password controller instance.
	 *
	 * @param \Illuminate\Contracts\Auth\Guard $auth        	
	 * @param \Illuminate\Contracts\Auth\PasswordBroker $passwords        	
	 * @return void
	 */
	public function __construct(Guard $auth, PasswordBroker $passwords) {
		$this->auth = $auth;
		$this->passwords = $passwords;
		
		$this->middleware ( 'guest' );
	}
	
	/**
	 * 发送验证码
	 *
	 * @param Request $request        	
	 */
	public function postSendcheckcode(Request $request) {
		try {
			$user = $request->user ();
			// 需要配置config/mail.php和文件.evn
			$receiver = $request->input ( 'receiver' );
			$userService = new UserService ();
			$verifService = new VerifyService ();
			$temService = new TelEmailService ();
			if (RegHelper::validateEmail ( $receiver )) { // 邮箱
				if (! empty ( $user ) && $user->email != $receiver)
					return $this->resetFail ( '输入邮箱与当前登录邮箱不一致' );
				if ($userService->uniqueEmail ( $receiver )) { // 若存在 才允许发送验证码
					$code = $verifService->getTelEmailCode ( $receiver );
					$temService->sendEmailVerify ( $code, $receiver );
				} else {
					return $this->resetFail ( '邮箱未注册' );
				}
			} else if (RegHelper::validateTel ( $receiver )) { // 若存在 才允许发送验证码
				if (! empty ( $user ) && $user->tel != $receiver)
					return $this->resetFail ( '输入手机与当前登录手机不一致' );
				if ($userService->uniqueTel ( $receiver )) { // 若存在 才允许发送验证码
					$code = $verifService->getTelEmailCode ( $receiver );
					$ret = $temService->sendTelVerify ( $code, $receiver );
				} else {
					return $this->resetFail ( '手机未注册' );
				}
			}
			return "{success:1}";
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
	
	/**
	 * Reset the given user's password.
	 *
	 * @param Request $request        	
	 * @return Response
	 */
	public function postReset(Request $request) {
		try {
			$reqaccount = $request->input ( 'email' ); // 注册帐号
			$reqcheckcode = $request->input ( 'checkcode' ); // 手机、邮箱验证码
			$temService = new TelEmailService (); // 验证码类
			$msg = $temService->verTelEmailCodeValidate ( $reqcheckcode, $reqaccount ); // 验证手机邮箱验证码
			if (! $msg) { // 返回空字符串表示验证通过
				$password = $request->input ( 'password' );
				$userService = new UserService ();
				$user = new User ();
				if (RegHelper::validateEmail ( $reqaccount )) {
					$user = $userService->resetPWD ( "chrEmail", $reqaccount, $password );
				} else if (RegHelper::validateTel ( $reqaccount )) {
					$user = $userService->resetPWD ( "chrTel", $reqaccount, $password );
				}
				$this->auth->login ( $user );
				return "{success:1,url:'/'}";
			}
			return $this->resetFail ( $msg );
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
	private function resetFail($msg) {
		return "{success:0,error:'{$msg}'}";
	}
	
	/**
	 * 成功返回的json信息
	 *
	 * @param unknown $url        	
	 * @return string
	 */
	private function resetSuccess($url) {
		return "{success:1,url:'{$url}'}";
	}
}
