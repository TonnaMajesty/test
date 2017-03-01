<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\SysFlow;

class FlowService {
	
	/**
	 * 添加流程
	 *
	 * @param unknown $flows        	
	 */
	public function addFlow($flows, $user) {
		$flow = new SysFlow ();
		$flow->intFormID = $flows ['formid'];
		$flow->chrFlowType = $flows ['flowtype'];
		$flow->chrFlowName = $flows ['flowname'];
		$flow->chrMemo = $flows ['memo'];
		$flow->intFlowAsc = $flows ['flowasc'];
		$flow->intCreaterID = $user->id;
		$flow->intCompanyID = $user->intCompanyID;
		$flow->save ();
		return $flow->id;
	}
}

?>