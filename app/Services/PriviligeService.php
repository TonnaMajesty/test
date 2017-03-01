<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class PriviligeService {
	
	/**
	 *
	 * @param unknown $roleId        	
	 */
	public function getPrivilige($roleId, $user) {
		$wl = "and intCompanyID=" . $user->intCompanyID;
		if ($user->intAdmin)
			$wl = "";
		return DB::select ( "select distinct chrPriviligeOperationTypeValue pvId from sys_priviliges 
				where chrPriviligeType='role' and intPriviligeTypeValue=? $wl", [ 
				$roleId 
		] );
	}
	/**
	 *
	 * @param unknown $roleId        	
	 * @param unknown $permis        	
	 * @param unknown $oldPermis        	
	 * @param unknown $user        	
	 */
	public function insert($roleId, $funcPerm, $dataPerm, $user) {
		DB::beginTransaction ();
		try {
			$pivs = array ();
			// 功能权限
			$permis = $funcPerm ["node"];
			$oldPermis = empty ( $funcPerm ["oldNode"] ) ? array () : $funcPerm ["oldNode"];
			foreach ( $permis as $permi ) {
				if (($key = array_search ( $permi ["id"], $oldPermis )) === FALSE) {
					$piv = array (
							"chrPriviligeType" => "role",
							"intPriviligeTypeValue" => $roleId 
					);
					$piv ["chrPriviligeOperationType"] = $permi ["type"];
					$piv ["chrPriviligeOperationTypeValue"] = $permi ["id"];
					$piv ["intCompanyID"] = ($user->intAdmin ? 1 : $user->intCompanyID); // 若是超级管理员 则做特殊处理 暂时写死
					array_push ( $pivs, $piv );
				} else
					array_splice ( $oldPermis, $key, 1 ); // 删除存在的
			}
			// 数据权限
			$dpermis = empty ( $dataPerm ["node"] ) ? array () : $dataPerm ["node"];
			$olddPermis = empty ( $dataPerm ["oldNode"] ) ? array () : $dataPerm ["oldNode"];
			foreach ( $dpermis as $dpermi ) {
				Log::info ( $dpermi );
				if (($key = array_search ( $dpermi ["id"], $olddPermis )) === FALSE) {
					$piv = array (
							"chrPriviligeType" => "role",
							"intPriviligeTypeValue" => $roleId,
							"chrPriviligeOperationType" => (empty ( $dpermi ["type"] ) ? "data" : $dpermi ["type"]),
							"chrPriviligeOperationTypeValue" => $dpermi ["id"],
							"intCompanyID" => ($user->intAdmin ? 1 : $user->intCompanyID) 
					);
					array_push ( $pivs, $piv );
				} else
					array_splice ( $olddPermis, $key, 1 ); // 删除存在的
			}
			DB::table ( "sys_priviliges" )->insert ( $pivs );
			if (! empty ( $oldPermis )) {
				$delIds = str_replace ( ",", "','", implode ( ',', $oldPermis ) );
				DB::delete ( "delete from sys_priviliges where chrPriviligeType='role' and intPriviligeTypeValue=$roleId 
				and chrPriviligeOperationTypeValue in ('$delIds')" );
			}
			if (! empty ( $olddPermis )) {
				$delIds = str_replace ( ",", "','", implode ( ',', $olddPermis ) );
				DB::delete ( "delete from sys_priviliges where chrPriviligeType='role' and intPriviligeTypeValue=$roleId
				and chrPriviligeOperationTypeValue in ('$delIds')" );
			}
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
}

?>