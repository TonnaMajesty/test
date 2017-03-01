<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\SysMachine;
use Illuminate\Support\Facades\Log;

class MachineService {
	
	/**
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 * @return string
	 */
	public function getMachineList($secho, $iDisplayStart, $iDisplayLength) {
		$res = DB::select ( "select count(*) as allCount from sys_machines where intFlag=0" );
		$allcount = $res [0]->allCount;
		$machines = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$pagecount = $iDisplayStart; // ($iDisplayStart - 1) * $iDisplayLength; // 开始index
		$rows = DB::select ( 'select smac.id,smac.chrMachName machName,chrIp ip,smr.intHubMaxCount hubMaxCount,
				smr.intHubNowCount hubNowCount,u.chrUserName creUserName
				from sys_machines smac
				INNER JOIN sys_machine_relations smr on smr.intMachineID=smac.id
				INNER JOIN users u on u.id=smac.intCreaterID limit ?,?', [ 
				$pagecount,
				$iDisplayLength 
		] );
		$machines .= json_encode ( $rows );
		$machines .= "}";
		return $machines;
	}
	/**
	 *
	 * @param unknown $machine        	
	 * @param unknown $user        	
	 */
	public function insert($machine, $user) {
		DB::beginTransaction ();
		try {
			$mach_model = new SysMachine ();
			$mach_model->chrMachName = $machine ["machName"];
			$mach_model->chrIp = $machine ["ip"];
			$mach_model->intCreaterID = $mach_model->intModifyID = $user->id;
			$mach_model->save ();
			$machId = $mach_model->id;
			DB::insert ( "insert into sys_machine_relations (intMachineID,intHubPort,chrHub,intHubMaxCount,
					intCreaterID,intModifyID)values (?,?,?,?,?,?)", [ 
					$machId,
					$machine ["hubPort"],
					$machine ["hub"],
					$machine ["hubMaxCount"],
					$user->id,
					$user->id 
			] );
			
			foreach ( $machine ["selBrowsers"] as $selBrowser ) {
				DB::insert ( "insert into sys_machine_configs (intMachineID,intBrowserID,intCreaterID,intModifyID) values (?,?,?,?)", [ 
						$machId,
						$selBrowser,
						$user->id,
						$user->id 
				] );
			}
			
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $machine        	
	 * @param unknown $id        	
	 */
	public function update($machine, $id, $user) {
		DB::beginTransaction ();
		try {
			DB::update ( "update sys_machines set chrMachName=?,chrIp=?,intModifyID=? where id=?", [ 
					$machine ["machName"],
					$machine ["ip"],
					$user->id,
					$id 
			] );
			DB::update ( "update sys_machine_relations set intHubPort=?,chrHub=?,intHubMaxCount=?,
					intModifyID=? where intMachineID=?", [ 
					$machine ["hubPort"],
					$machine ["hub"],
					$machine ["hubMaxCount"],
					$user->id,
					$id 
			] );
			$oldBrowserIds = $machine ["oldBrowserIds"];
			foreach ( $machine ["selBrowsers"] as $selBrowser ) {
				if (($key = array_search ( $selBrowser, $oldBrowserIds )) === FALSE) {
					DB::insert ( "insert into sys_machine_configs (intMachineID,intBrowserID,intCreaterID,intModifyID) values (?,?,?,?)", [ 
							$id,
							$selBrowser,
							$user->id,
							$user->id 
					] );
				} else
					array_splice ( $oldBrowserIds, $key, 1 ); // 删除存在的
			}
			if (! empty ( $oldBrowserIds )) {
				$delIds = implode ( ',', $oldBrowserIds );
				DB::delete ( "delete from sys_machine_configs where intMachineID=$id and intBrowserID in ($delIds)" );
			}
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 *
	 * @param unknown $ids        	
	 */
	public function delete($ids) {
		DB::beginTransaction ();
		try {
			DB::delete ( "delete from sys_machine_configs where intMachineID in ($ids)" );
			DB::delete ( "delete from sys_machine_relations where intMachineID in ($ids)" );
			DB::delete ( "delete from sys_machines where id in ($ids)" );
			DB::commit ();
		} catch ( \Exception $e ) {
			DB::rollback ();
			throw $e;
		}
	}
	
	/**
	 * 查询单条记录
	 *
	 * @param unknown $id        	
	 */
	public function show($id) {
		$rows = DB::select ( "select smac.id,smac.chrMachName machName,smac.chrIp ip,smr.intHubPort hubPort,
				smr.chrHub hub,smr.intHubMaxCount hubMaxCount,smc.intBrowserID browserId from sys_machines smac
				inner join sys_machine_relations smr on smr.intMachineID=smac.id
				INNER JOIN sys_machine_configs smc on smc.intMachineID=smac.id
				where smac.id=$id" );
		$machine = array (
				"id" => $rows [0]->id,
				"machName" => $rows [0]->machName,
				"ip" => $rows [0]->ip,
				"hubPort" => $rows [0]->hubPort,
				"hub" => $rows [0]->hub,
				"hubMaxCount" => $rows [0]->hubMaxCount 
		);
		$browserIds = "";
		foreach ( $rows as $row ) {
			$browserIds .= $row->browserId . ";";
		}
		$machine ["browserIds"] = substr ( $browserIds, 0, - 1 );
		return $machine;
	}
}

?>