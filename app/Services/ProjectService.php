<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\AutoProject;
use Illuminate\Support\Facades\Session;

class ProjectService {
	
	/**
	 *
	 * @return string
	 */
	public function getProjectDataAuth() {
		$userAuth = Session::get ( "auth" );
		$wl = "";
		$dataAuths = $userAuth->dataAuths;
		if (! empty ( $dataAuths ["PROJECT"] )) {
			$wl = " and apro.id in (" . $dataAuths ["PROJECT"] . ")";
		}
		return $wl;
	}
	
	/**
	 *
	 * @param unknown $rows        	
	 */
	private function filterProductDataAuth($rows) {
		$userAuth = Session::get ( "auth" );
		$dataAuths = $userAuth->dataAuths;
		if (! empty ( $dataAuths ["PROJECT"] )) {
			$dataAuths = explode ( ",", $dataAuths ["PROJECT"] );
			$pId = 0;
			$idxs = array ();
			foreach ( $rows as $key => $row ) {
				if ($row->pId) {
					$pId = $this->getTopProjectId ( $row->pId, $rows );
				} else {
					$pId = $row->id;
				}
				if (! in_array ( $pId, $dataAuths )) {
					array_push ( $idxs, $key );
				}
			}
			foreach ( $idxs as $key => $idx ) {
				unset ( $rows [$idx] );
			}
		}
		return array_merge ( array_filter ( $rows ) );
	}
	
	/**
	 *
	 * @param unknown $pId        	
	 * @param unknown $rows        	
	 */
	private function getTopProjectId($pId, $rows) {
		foreach ( $rows as $row ) {
			if ($pId == $row->id) {
				if ($row->pId)
					$pId = $this->getTopProjectId ( $row->pId, $rows );
				break;
			}
		}
		return $pId;
	}
	
	/**
	 *
	 * @param unknown $id        	
	 * @param unknown $rows        	
	 */
	private function getLinksById($id, $rows, & $links) {
		foreach ( $rows as $key => $row ) {
			if ($row->id == $id) {
				array_unshift ( $links, $row );
				unset ( $rows [$key] );
				$this->getLinksById ( $row->intParentID, $rows, $links );
				break;
			}
		}
	}
	
	/**
	 * 根据产品id 获取父级
	 *
	 * @param unknown $id        	
	 */
	public function getProjectLinkById($id, $user) {
		$rows = DB::select ( "select id,chrProjectName,intParentID from auto_projects 
				where intFlag=0 and intCompanyID=$user->intCompanyID" );
		$links = array ();
		$this->getLinksById ( $id, $rows, $links );
		return $links;
	}
	
	/**
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 */
	public function getProjectList($secho, $iDisplayStart, $iDisplayLength, $user) {
		$wl = $this->getProjectDataAuth ();
		$res = DB::select ( "select count(*) as allCount from auto_projects apro where intFlag=0 and intParentID=0 $wl" );
		$allcount = $res [0]->allCount;
		$projects = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$pagecount = $iDisplayStart;
		$rows = DB::select ( "select id,chrProjectName projectName,chrMemo memo 
				from auto_projects apro where intFlag=0 and intCompanyID=$user->intCompanyID and intParentID=0 $wl order by chrProjectName limit ?,?", [ 
				$pagecount,
				$iDisplayLength 
		] );
		$projects .= json_encode ( $rows );
		$projects .= "}";
		return $projects;
	}
	
	/**
	 * 获取产品树的数据
	 *
	 * @param unknown $user        	
	 */
	public function getProductTree($user) {
		$rows = DB::select ( "SELECT id,intParentID as pId,chrProjectName as name,'true' isParent,
				case when intParentID=0 then 'project' else 'project_node' end iconSkin,'true' open
				FROM auto_projects apro where intCompanyID=$user->intCompanyID" );
		$rows = $this->filterProductDataAuth ( $rows );
		return $rows;
	}
	
	/**
	 *
	 * @param unknown $user        	
	 */
	public function getProjectTree($user) {
		$wl = $this->getProjectDataAuth ();
		return DB::select ( "SELECT id,intParentID as pId,chrProjectName as name,'true' isParent,'project' iconSkin,'true' open
				FROM auto_projects apro where intCompanyID=$user->intCompanyID and intParentID=0 $wl" );
	}
	
	/**
	 * 查看、编辑
	 *
	 * @param unknown $id        	
	 */
	public function show($id) {
		$res = DB::select ( "select chrProjectName projectName,chrMemo memo from auto_projects where id=$id" );
		return $res [0];
	}
	
	/**
	 * 新增项目
	 *
	 * @param unknown $project        	
	 * @param unknown $user        	
	 */
	public function insert($project, $user) {
		DB::beginTransaction ();
		try {
			$auto_project = new AutoProject ();
			$auto_project->chrProjectName = $project ['projectName'];
			$auto_project->intParentID = $project ['parentId'];
			$auto_project->chrMemo = $project ['memo'];
			$auto_project->intCreaterID = $user->id;
			$auto_project->intModifyID = $user->id;
			$auto_project->intModifyID = $user->id;
			$auto_project->intCompanyID = $user->intCompanyID;
			$auto_project->save ();
			if (! $auto_project->intParentID) {
				$projectId = $auto_project->id;
				DB::insert ( "insert into sys_resource_objects (chrResObjCode,chrResourceCode,intObjectID,intCompanyID)
					values (uuid(),?,?,?)", [ 
						"PROJECT",
						$projectId,
						$user->intCompanyID 
				] );
			}
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
		return $auto_project->id;
	}
	
	/**
	 *
	 * @param unknown $project        	
	 */
	public function update($id, $project, $user) {
		DB::update ( "update auto_projects set chrProjectName=?,chrMemo=?,intModifyID=? where id=? and intCompanyID=?", [ 
				$project ["projectName"],
				$project ["memo"],
				$user->id,
				$id,
				$user->intCompanyID 
		] );
	}
	
	/**
	 * 删除
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids, $user) {
		DB::delete ( "delete from auto_projects where id in ($ids) and intCompanyID=$user->intCompanyID" );
	}
}

?>