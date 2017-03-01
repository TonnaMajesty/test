<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Log;

class ProductService {
	/**
	 *
	 * @return string
	 */
	private function getProjectDataAuth() {
		$userAuth = Session::get ( "auth" );
		$wl = "";
		$dataAuths = $userAuth->dataAuths;
		if (! empty ( $dataAuths ["PROJECT"] )) {
			$wl = " and apro.id in (" . $dataAuths ["PROJECT"] . ")";
		}
		return $wl;
	}
	
	/**
	 * 获取产品树的数据
	 *
	 * @param unknown $user        	
	 */
	public function getProductTree($user) {
		$wl = $this->getProjectDataAuth ();
		return DB::select ( "SELECT id,intParentID as pId,chrProjectName as name,'true' isParent,
				case when intParentID=0 then 'project' else 'project_node' end iconSkin,'true' open
				FROM auto_projects apro where intCompanyID=$user->intCompanyID" );
	}
}

?>