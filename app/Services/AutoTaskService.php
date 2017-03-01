<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\AutoTask;
use App\AutoTaskRelation;
use Illuminate\Support\Facades\Log;
use App\Utils\FileHelper;

class AutoTaskService {
	
	/**
	 * 获取任务总数
	 */
	private function getTaskCount($user, $search, $wl) {
		$rows = DB::select ( "select COUNT(*) allCount from auto_tasks ats
				left JOIN (
				select id,intTaskID,intState from auto_task_execs ate 
				where ate.intFlag=0 and ate.intCreaterID=$user->id and intTimerTaskID=0
				)ate on ate.intTaskID=ats.id
				INNER JOIN users u on u.id=ats.intCreaterID 
				INNER JOIN auto_projects apro on apro.id=ats.intProjectID
				where ats.intFlag=0 and ats.intCompanyID=$user->intCompanyID and intTaskType=0 and $search $wl" );
		return $rows [0]->allCount;
	}
	
	/**
	 *
	 * @param unknown $search        	
	 */
	private function structureSearchSQL($search) {
		if (! empty ( $search )) {
			$sql = array ();
			$projectId = $search ["projectId"];
			$state = $search ["state"];
			$taskName = trim ( $search ["taskName"] );
			$creater = trim ( $search ["creater"] );
			if ($projectId) {
				array_push ( $sql, "ats.intProjectID=$projectId" );
			}
			if ($state === "") {
				array_push ( $sql, "ate.intState is NULL" );
			} else if ($state >= 0)
				array_push ( $sql, "ate.intState=$state" );
			if ($taskName)
				array_push ( $sql, "ats.chrTaskName='$taskName'" );
			if ($creater)
				array_push ( $sql, "u.chrUserName='$creater'" );
			$sql = implode ( " and ", $sql );
		}
		if (empty ( $sql ))
			$sql = "1=1";
		return $sql;
	}
	
	/**
	 * 获取任务列表信息
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 */
	public function getTaskList($secho, $iDisplayStart, $iDisplayLength, $user, $search, $wl) {
		$search = $this->structureSearchSQL ( $search );
		$allcount = $this->getTaskCount ( $user, $search, $wl );
		$tasks = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select ats.id,chrTaskName taskName,u.chrUserName createUser,ate.chrBrowserNames browserNames,
				case when ate.intState=0 then '排队中' when ate.intState=1 then '执行中' when ate.intState=2 then '执行成功' 
				when ate.intState=3 then '执行失败' else '未执行' end state,ate.id taskExecID,ats.intProjectID projectId,apro.chrProjectName projectName
				from auto_tasks ats
				INNER JOIN users u on u.id=ats.intCreaterID
				LEFT JOIN auto_task_execs ate on ate.intTaskID=ats.id and ate.intFlag=0 
				and ate.intTimerTaskID=0 and ate.intCreaterID=$user->id
				INNER JOIN auto_projects apro on apro.id=ats.intProjectID
				where ats.intFlag=0 and ats.intCompanyID=$user->intCompanyID and ats.intTaskType=0 and $search $wl ORDER BY ats.id desc  
				limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$tasks .= json_encode ( $rows );
		$tasks .= "}";
		return $tasks;
	}
	
	/**
	 * 获取任务
	 *
	 * @param unknown $id        	
	 */
	public function getTaskById($id, $user) {
		$rows = DB::select ( "select ats.id,ats.chrTaskName,atr.intSchemeID,aus.chrSchemeName,
		ats.intProjectID projectId,apro.chrProjectName projectName from  auto_tasks ats
		INNER JOIN auto_task_relations atr on atr.intTaskID=ats.id
		INNER JOIN auto_schemes aus on aus.id=atr.intSchemeID
		INNER JOIN auto_projects apro on apro.id=ats.intProjectID
		where ats.id=$id and ats.intCompanyID=$user->intCompanyID" );
		$task = array (
				"taskName" => $rows [0]->chrTaskName,
				"projectId" => $rows [0]->projectId 
		);
		foreach ( $rows as $row ) {
			$scheme = array (
					"id" => $row->intSchemeID,
					"schemeName" => $row->chrSchemeName,
					"projectId" => $row->projectId 
			);
			$task ["schemes"] [] = $scheme;
		}
		return $task;
	}
	
	/**
	 *
	 * @param unknown $task        	
	 */
	public function insert($task, $user) {
		DB::beginTransaction ();
		try {
			$auto_task = new AutoTask ();
			$auto_task->chrTaskName = $task ["taskName"];
			$auto_task->intProjectID = $task ["projectId"];
			$auto_task->intCreaterID = $auto_task->intModifyID = $user->id;
			$auto_task->intCompanyID = $user->intCompanyID;
			$auto_task->save ();
			$taskId = $auto_task->id;
			$schemes = $task ['schemes'];
			foreach ( $schemes as $idx => $scheme ) {
				$auto_task_rel = new AutoTaskRelation ();
				$auto_task_rel->intTaskID = $taskId;
				$auto_task_rel->intExecOrder = $idx;
				$auto_task_rel->intSchemeID = $scheme;
				$auto_task_rel->intCreaterID = $auto_task_rel->intModifyID = $user->id;
				$auto_task_rel->intCompanyID = $user->intCompanyID;
				$auto_task_rel->save ();
			}
			$companyID = $user->intCompanyID;
			$projectId = $task ["projectId"];
			/*
			 * $redis = RedisHelper::getInstance (); $key = "task.day.company" . $companyID; $date = date ( 'Y-m-d', time () ); $redis->hIncrBy ( $key, $date, 1 ); $key = "task.day.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "W", time () ); $key = "task.week.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "task.week.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 ); $date = date ( "m", time () ); $key = "task.mon.company" . $companyID; $redis->hIncrBy ( $key, $date, 1 ); $key = "task.mon.product" . $projectId; $redis->hIncrBy ( $key, $date, 1 );
			 */
			DB::commit ();
			return $taskId;
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids, $user) {
		DB::beginTransaction ();
		try {
			// 删除任务队列相关
			DB::delete ( "DELETE from auto_jobs where intExecTaskID in (
			select id from auto_task_execs where intTaskID in ($ids))" );
			DB::delete ( "delete from auto_task_execs where intTaskID in ($ids) and intTimerTaskID=0 and intCompanyID=$user->intCompanyID" );
			// 删除报告相关
			DB::delete ( "delete from auto_reports where intTaskID in ($ids) and intTaskType=1" );
			// 删除任务相关
			DB::delete ( "delete from auto_tasks where id in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::delete ( "delete from auto_task_relations where intTaskID in ($ids) and intCompanyID=$user->intCompanyID" );
			DB::commit ();
			$root = database_path ( "schemes/" );
			$ids = explode ( ",", $ids );
			foreach ( $ids as $id )
				FileHelper::resource_remove ( $root . $id, true, true );
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $task        	
	 * @param unknown $user        	
	 */
	public function update($taskId, $task, $user) {
		DB::beginTransaction ();
		try {
			DB::update ( "update auto_tasks set chrTaskName=?,intProjectID=?,intModifyID=? 
			where id=? and intCompanyID=$user->intCompanyID", [ 
					$task ["taskName"],
					$task ["projectId"],
					$user->id,
					$taskId 
			] );
			$schemes = $task ["schemes"];
			$oldSchemeIds = $task ["oldSchemeIds"];
			foreach ( $schemes as $idx => $scheme ) {
				if (($key = array_search ( $scheme, $oldSchemeIds )) === FALSE) {
					$auto_task_rel = new AutoTaskRelation ();
					$auto_task_rel->intTaskID = $taskId;
					$auto_task_rel->intExecOrder = $idx;
					$auto_task_rel->intSchemeID = $scheme;
					$auto_task_rel->intCreaterID = $auto_task_rel->intModifyID = $user->id;
					$auto_task_rel->intCompanyID = $user->intCompanyID;
					$auto_task_rel->save ();
				} else
					array_splice ( $oldSchemeIds, $key, 1 ); // 删除存在的
			}
			if (! empty ( $oldSchemeIds )) {
				$delIds = implode ( ',', $oldSchemeIds );
				DB::delete ( "delete from auto_task_relations where intTaskID=$taskId and intSchemeID in ($delIds) and intCompanyID=$user->intCompanyID" );
			}
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
}

?>