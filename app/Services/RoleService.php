<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;

class RoleService {
	
	/**
	 * 获取角色树的数据
	 *
	 * @param unknown $user        	
	 */
	public function getRoleTree($user) {
		return DB::select ( "SELECT id,'0' as pId,chrRoleName as name,'true' isParent,'true' open
				FROM sys_roles where intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 */
	public function getRoleList($secho, $iDisplayStart, $iDisplayLength, $user) {
		$res = DB::select ( "select count(*) as allCount from sys_roles where intFlag=0 and intCompanyID=$user->intCompanyID" );
		$allcount = $res [0]->allCount;
		$roles = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$pagecount = $iDisplayStart;
		$rows = DB::select ( "select id,chrRoleName roleName,chrRoleDesc roleDesc from sys_roles where intCompanyID=$user->intCompanyID limit ?,?", [ 
				$pagecount,
				$iDisplayLength 
		] );
		$roles .= json_encode ( $rows );
		$roles .= "}";
		return $roles;
	}
	
	/**
	 * 添加角色
	 *
	 * @param unknown $role        	
	 * @param unknown $user        	
	 */
	public function insert($role, $user) {
		DB::insert ( "insert into sys_roles (chrRoleName,chrRoleDesc,intCompanyID)
				values (?,?,?)", [ 
				$role ['roleName'],
				$role ['roleDesc'],
				$user->intCompanyID 
		] );
	}
	
	/**
	 * 添加角色
	 */
	public function delete($ids, $user) {
		DB::delete ( "delete from sys_roles where id in ($ids) and intCompanyID=$user->intCompanyID" );
	}
	
	/**
	 * 查看、编辑
	 *
	 * @param unknown $id        	
	 */
	public function show($id, $user) {
		$res = DB::select ( "select id,chrRoleName roleName,chrRoleDesc roleDesc from sys_roles 
				where id=$id and intCompanyID=$user->intCompanyID" );
		return $res [0];
	}
	
	/**
	 * 修改
	 *
	 * @param unknown $id        	
	 */
	public function update($id, $data, $user) {
		DB::update ( "update sys_roles set chrRoleName=?,chrRoleDesc=? where id=? and intCompanyID=?", [ 
				$data ['roleName'],
				$data ['roleDesc'],
				$id,
				$user->intCompanyID 
		] );
	}
}

?>