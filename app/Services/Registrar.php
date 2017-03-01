<?php

namespace App\Services;

use App\User;
use Validator;
use Illuminate\Contracts\Auth\Registrar as RegistrarContract;
use App\SysCompany;
use Illuminate\Support\Facades\DB;

class Registrar implements RegistrarContract {
	
	/**
	 * Get a validator for an incoming registration request.
	 *
	 * @param array $data        	
	 * @return \Illuminate\Contracts\Validation\Validator
	 */
	public function validator(array $data) {
		return Validator::make ( $data, [ 
				'name' => 'required|max:255',
				'email' => 'required|email|max:255|unique:users',
				'password' => 'required|confirmed|min:6' 
		] );
	}
	
	/**
	 * Create a new user instance after a valid registration.
	 *
	 * @param array $data        	
	 * @return User
	 */
	public function create(array $data) {
		if (! empty ( $data )) {
			DB::beginTransaction ();
			try {
				$company = new SysCompany ();
				$company->chrCompanyName = $data ["company"];
				$company->chrCompanyCode = $data ["company"];
				$company->save ();
				$user = new User ();
				$user->chrUserCode = "000001";
				$user->chrUserName = $data ['email'];
				$user->chrEmail = $data ['email'];
				$user->password = $data ['password'];
				$user->chrTel = $data ['tel'];
				$user->intOrgID = 0;
				$user->intState = 0;
				$user->intCompanyID = $company->id; // 获取自增id
				$user->save ();
				DB::insert ( "insert into sys_user_roles (intUserID,intRoleID) values (?,?)", [ 
						$user->id,
						2 
				] );
				DB::insert ( "insert into sys_organizations (intParentID,chrOrgCode,chrOrgName,intOrgType,intCompanyID) 
						values (?,?,?,?,?)", [ 
						0,
						$data ["company"],
						$data ["company"],
						1,
						$company->id 
				] );
				DB::commit ();
				return $user;
			} catch ( \Exception $e ) {
				DB::rollback ();
				throw ($e);
			}
		}
		return null;
	}
}
