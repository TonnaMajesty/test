<?php

namespace App\Http\Controllers\Verify;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Session;
use App\Services\VerifyService;
use Illuminate\Http\Request;
use App\Services\TelEmailService;
use App\Utils\RegHelper;
use App\Services\UserService;
use Illuminate\Support\Facades\Log;

class VerifyController extends Controller {
	
	/**
	 * 图片验证码
	 *
	 * @return Response
	 */
	public function index(Request $request) {
		// 生成验证码图片
		try {
			$verify = new VerifyService ();
			$verify->getImageCode ( 4, 90, 30 );
		} catch ( \Exception $e ) {
			throw ($e);
		}
	}
}
