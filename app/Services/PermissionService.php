<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class PermissionService {
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getRightTree($user) {
		if ($user->intAdmin)
			return DB::select ( "SELECT chrRightCode id,id tId,case when chrParentCode is NULL then intMenuID else chrParentCode end as pId,
				chrRightName as name,'false' isParent,'true' open,'button' type
				FROM sys_permissions
				union ALL
				select id,id tId,intParentID pId,chrMenuName name,'true' isParent,'true' open,'menu' type  from sys_menus" );
		return DB::select ( "select DISTINCT case when sper.chrPriviligeOperationType='button' then spm.chrRightCode else smenu.id end id,
				case when sper.chrPriviligeOperationType='button' then spm.id else smenu.id end tId,
				case when sper.chrPriviligeOperationType='button' and spm.chrParentCode is NULL then spm.intMenuID 
				when sper.chrPriviligeOperationType='menu' then smenu.intParentID else spm.chrParentCode end pId,
				case when sper.chrPriviligeOperationType='button' then spm.chrRightName else smenu.chrMenuName end name,
				case when sper.chrPriviligeOperationType='button' then 'false' else 'true' end isParent,'true' open,
				sper.chrPriviligeOperationType type
				from  sys_priviliges sper
				left JOIN sys_permissions spm on spm.chrRightCode=sper.chrPriviligeOperationTypeValue and sper.chrPriviligeOperationType='button'
				left join sys_menus smenu on smenu.id=sper.chrPriviligeOperationTypeValue and sper.chrPriviligeOperationType='menu'
				where sper.chrPriviligeOperationType in ('button','menu')" ); // and sper.intCompanyID=$user->intCompanyID
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getDataRightTree($user) {
		return DB::select ( "select chrResourceCode id,'0' as pId,chrResourceName as name,'true' isParent,'true' open 
				from sys_resources where intFlag=0
				union all
				select sro.chrResObjCode id,chrResourceCode as pId,apro.chrProjectName as name,'true' isParent,'true' open
				from auto_projects apro
				INNER JOIN sys_resource_objects sro on sro.intObjectID=apro.id and sro.chrResourceCode='PROJECT'
				where apro.intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 *
	 * @param unknown $orgCode        	
	 * @param unknown $user        	
	 */
	public function getOrgDataRightTree($orgCode, $user) {
		return DB::select ( "select sorg.id,intParentID as pId,sorg.chrOrgName as name,'true' isParent,'true' open 
				from sys_organizations sorg
				LEFT JOIN sys_resource_objects sro on sro.intObjectID=sorg.id and sro.chrResourceCode='$orgCode'
				where sorg.intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 *
	 * @param unknown $orgCode        	
	 * @param unknown $user        	
	 */
	public function getProjectDataRightTree($proCode, $user) {
		return DB::select ( "select sro.chrResObjCode id,intParentID as pId,apro.chrProjectName as name,'true' isParent,'true' open
				from auto_projects apro
				INNER JOIN sys_resource_objects sro on sro.intObjectID=apro.id and sro.chrResourceCode='$proCode'
				where apro.intCompanyID=$user->intCompanyID" );
	}
}

?>