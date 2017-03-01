<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class SysMenuClassify extends Model {
	
	//
	public function hasOneClassifyImg() {
		return $this->hasOne ( 'App\SysImgDetail' );
	}
}
