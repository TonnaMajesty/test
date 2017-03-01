<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class SysMenuType extends Model {
	
	//
	public function hasOneMenuTypeImg() {
		return $this->hasOne ( 'App\SysImgDetail' );
	}
}
