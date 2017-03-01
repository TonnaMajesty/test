<?php

namespace App\Services;

use App\SysFlowProcess;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class FlowProcessService {
	
	/**
	 * 获取流程步骤信息
	 *
	 * @param unknown $flowid        	
	 */
	public function getFlowProcess($flowid) {
		$sql = "select id,chrProcessName,case when chrProcessTo is null then '' else chrProcessTo end chrProcessTo,
		chrProcessStyle,chrProcessType from sys_flow_processes where intFlowID=$flowid and intFlag=0";
		$rows = DB::select ( $sql );
		$index = 0;
		$processData = array ();
		foreach ( $rows as $row ) {
			$processData ["list"] [$index] = array (
					"id" => $row->id,
					"flow_id" => $flowid,
					"process_name" => $row->chrProcessName,
					"process_to" => $row->chrProcessTo,
					"icon" => ($row->chrProcessType ? "icon-star" : "icon-ok"),
					"style" => $row->chrProcessStyle 
			);
			$index ++;
		}
		$processData ["total"] = -- $index;
		$processData ["flowid"] = $flowid;
		return $processData;
	}
	
	/**
	 * 添加步骤
	 *
	 * @param unknown $process        	
	 */
	public function addProcess($process, $user) {
		$process ['processtype'] = "1";
		if ($process ['icon'] == "icon-ok")
			$process ['processtype'] = "0";
		$flowprocess = new SysFlowProcess ();
		$flowprocess->intFlowID = $process ['flowid'];
		$flowprocess->chrProcessName = $process ['processname'];
		$flowprocess->chrProcessType = $process ['processtype'];
		$flowprocess->chrProcessStyle = $process ['style'];
		$flowprocess->intCreaterID = $user->id;
		$flowprocess->intRelationID = $process ['relationid'];
		$flowprocess->intCompanyID = $user->intCompanyID;
		$flowprocess->save ();
		$processId = $flowprocess->id;
		$processinfo = array (
				"flow_id" => $process ['flowid'],
				"icon" => $process ['icon'],
				"id" => $flowprocess->id,
				"process_name" => $process ['processname'],
				"process_to" => "",
				"style" => $process ['style'] 
		);
		return $processinfo;
	}
	
	/**
	 * 删除流程步骤
	 *
	 * @param unknown $stepid        	
	 */
	public function delProcess($processId, $user) {
		DB::beginTransaction ();
		try {
			DB::update ( "update sys_flow_processes set chrProcessTo=REPLACE(chrProcessTo, '$processId', '') 
			where intCompanyID=$user->intCompanyID" );
			DB::delete ( "delete from sys_flow_processes where id=$processId and intCompanyID=$user->intCompanyID" );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 * 更新流程步骤
	 *
	 * @param unknown $process        	
	 */
	public function updateProcess($process, $processid, $user) {
		DB::update ( "update sys_flow_processes set chrProcessTo=?,chrProcessStyle=? where id=? and intCompanyID=?", [ 
				$process ['processTo'],
				$process ['style'],
				$processid,
				$user->intCompanyID 
		] );
	}
}

?>