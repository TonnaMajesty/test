<?php

namespace App;

use Illuminate\Auth\Authenticatable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Auth\Passwords\CanResetPassword;
use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
use Illuminate\Contracts\Auth\CanResetPassword as CanResetPasswordContract;

class User extends Model implements AuthenticatableContract, CanResetPasswordContract {
	
	use Authenticatable, CanResetPassword;
	
	/**
	 * The database table used by the model.
	 *
	 * @var string
	 */
	protected $table = 'users';
	
	/**
	 * The attributes that are mass assignable.
	 *
	 * @var array
	 */
	protected $fillable = [ 
			'chrUserCode',
			'chrUserName',
			'chrEmail',
			'password',
			'intDeptId',
			'intHeadId',
			'intState' 
	];
	
	/**
	 * The attributes excluded from the model's JSON form.
	 *
	 * @var array
	 */
	protected $hidden = [ 
			'password',
			'remember_token' 
	];
	
	/**
	 *
	 * @return \Illuminate\Database\Eloquent\Relations\BelongsToMany
	 */
	/*
	 * 最终生成的sql语句： select `menus`.*, `menu_users`.`A_UserID` as `pivot_A_UserID`, `menu_users`.`A_MenuID` as `pivot_A_MenuID` from `menus` inner join `menu_users` on `menus`.`id` = `menu_users`.`A_MenuID` where `menu_users`.`A_UserID` = 1
	 */
	public function hasManyUserMenus() {
		return $this->belongsToMany ( 'App\SysMenu', 'menu_users', 'A_UserID', 'A_MenuID' );
	}
}
