<?php

namespace App\Services;

use App\SysOrganization;
use Illuminate\Support\Facades\DB;

class OrganizeService {
	
	/**
	 * 获取产品树的数据
	 *
	 * @param unknown $user        	
	 */
	public function getOrgTree($user) {
		return DB::select ( "SELECT id,intParentID as pId,chrOrgName as name,'true' isParent,
				case when intParentID=0 then 'project' else 'project_node' end iconSkin,'true' open
				FROM sys_organizations where intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 * 新增组织机构
	 *
	 * @param unknown $project        	
	 * @param unknown $user        	
	 */
	public function insert($org, $user) {
		DB::beginTransaction ();
		try {
			$org_model = new SysOrganization ();
			$org_model->chrOrgName = $org ['orgName'];
			$org_model->intParentID = $org ['parentId'];
			$org_model->intOrgType = 0;
			$org_model->intCompanyID = $user->intCompanyID;
			$org_model->save ();
			$orgId = $org_model->id;
			DB::insert ( "insert into sys_resource_objects (chrResObjCode,chrResourceCode,intObjectID,intCompanyID)
					values (uuid(),?,?,?)", [ 
					"ORG",
					$orgId,
					$user->intCompanyID 
			] );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
		
		return $org_model->id;
	}
	
	/**
	 * 删除
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids, $user) {
		DB::delete ( "delete from sys_organizations where id in ($ids) and intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 *
	 * @param unknown $org        	
	 */
	public function update($id, $org, $user) {
		DB::update ( "update sys_organizations set chrOrgName=? where id=? and intCompanyID=?", [ 
				$org ["orgName"],
				$id,
				$user->intCompanyID 
		] );
	}
}

?>