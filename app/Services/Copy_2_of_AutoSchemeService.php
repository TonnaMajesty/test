<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class AutoSchemeService1 {
	
	/**
	 * 获取案例总数
	 */
	private function getSchemeCount() {
		$res = DB::select ( "select count(*) allcount from auto_schemes where intFlag=0" );
		return $res [0]->allcount;
	}
	
	/**
	 * 获取案例列表
	 *
	 * @param unknown $secho        	
	 * @param unknown $iDisplayStart        	
	 * @param unknown $iDisplayLength        	
	 * @return string
	 */
	public function getSchemeList($secho, $iDisplayStart, $iDisplayLength) {
		$allcount = $this->getSchemeCount ();
		$schemes = "{'sEcho': " . $secho . ",'iTotalRecords': " . $allcount . ",'iTotalDisplayRecords':" . $allcount . ",'aaData': ";
		$rows = DB::select ( "select aus.id,chrSchemeName schemeName,u.chrUserName createUser 
				from auto_schemes aus
				INNER JOIN users u on u.id=aus.intCreaterID
				where aus.intFlag=0 limit ?,?", [ 
				$iDisplayStart,
				$iDisplayLength 
		] );
		$schemes .= json_encode ( $rows );
		$schemes .= "}";
		return $schemes;
	}
	
	/**
	 *
	 * @param unknown $id        	
	 */
	private function getSchemeProcess($id) {
		$sql = "select sfp.id,ausr.intFlowID,chrProcessName,chrProcessStyle,chrProcessType,
		case when chrProcessTo is null then '' else chrProcessTo end chrProcessTo
		from auto_schemes aus
		INNER JOIN auto_scheme_relations ausr on ausr.intSchemeID=aus.id
		INNER JOIN sys_flow_processes sfp on sfp.intFlowID=ausr.intFlowID and sfp.intFlag=0
		where aus.id=$id";
		return DB::select ( $sql );
	}
	
	/**
	 *
	 * @param unknown $id        	
	 */
	public function getSchemeFlowProcess($id) {
		$rows = $this->getSchemeProcess ( $id );
		$index = 0;
		$processData = array ();
		foreach ( $rows as $row ) {
			$processData ["list"] [$index] = array (
					"id" => $row->id,
					"flow_id" => $row->intFlowID,
					"process_name" => $row->chrProcessName,
					"process_to" => $row->chrProcessTo,
					"icon" => ($row->chrProcessType ? "icon-star" : "icon-ok"),
					"style" => $row->chrProcessStyle 
			);
			$index ++;
		}
		$processData ["total"] = -- $index;
		$processData ["flowid"] = $rows [0]->intFlowID;
		return $processData;
	}
	
	/**
	 * 递归获取
	 *
	 * @param unknown $rows        	
	 * @param unknown $pfid        	
	 * @param unknown $line        	
	 */
	private function getSchemeScriptLines($rows, $pfid, & $line) {
		foreach ( $rows as $key => $row ) {
			$pto = $row->chrProcessTo;
			if ($pfid == $pto) {
				Log::info ( $pfid . "||" . $pto );
				$pid = $row->id;
				array_unshift ( $line, $pid );
				unset ( $rows [$key] );
				$this->getSchemeCount ( $rows, $pid, $line );
			}
		}
	}
	
	/**
	 *
	 * @param unknown $lines        	
	 */
	private function sortArrayByCount($lines) {
		$len = count ( $lines );
		for($i = 0; $i < $len; $i ++) {
			for($j = 0; $j < $len - $i - 1; $j ++) {
				$ilen = count ( $lines [$j] );
				$jlen = count ( $lines [$j + 1] );
				if ($jlen < $ilen) {
					$temp = $lines [$j];
					$lines [$j] = $lines [$j + 1];
					$lines [$j + 1] = $temp;
				}
			}
		}
		return $lines;
	}
	
	/**
	 * 获取开始节点
	 *
	 * @param unknown $rows        	
	 */
	private function getBeginNode($rows) {
		$beginLines = array ();
		foreach ( $rows as $row ) {
			$nodeId = $row->id;
			$begin = true;
			foreach ( $rows as $rowTo ) {
				$nodeTo = $rowTo->chrProcessTo;
				if (stripos ( $nodeTo, strval ( $nodeId ) ) !== false) {
					$begin = false;
					break;
				}
			}
			if ($begin) {
				$beginLines [] = $row;
			}
		}
		return $beginLines;
	}
	
	/**
	 *  获取单线流程
	 * @param unknown $beginLines
	 * @param unknown $fpto
	 * @param unknown $rows
	 * @param unknown $lines
	 */
	private function getLine($fpto, $rows, & $line) {
		
	}
	
	/**
	 * 生成案例下载包
	 *
	 * @param unknown $id        	
	 */
	public function makeSchemePackage($id) {
		$rows = $this->getSchemeProcess ( $id );
		$beginLines = $this->getBeginNode ( $rows );
		$lines = array ();
		foreach ( $beginLines as $beginLine ) {
			$line = array (
					$beginLine->id
			);
			$pto = $beginLine->chrProcessTo;
			$this->getLine ( $pto, $rows, $line );
			/* $ptos = explode(",", $pto);
			foreach ( $ptos as $pto ) {
				$line = array (
						$beginLine->id 
				);
				$this->getLine ( $pto, $rows, $line );
				$lines [] = array_filter($line);
			} */
		}
		Log::info($lines);
		/* $allLines = array ();
		foreach ( $rows as $key => $row ) {
			$pto = $row->chrProcessTo;
			$pfid = $row->id;
			$line = array (
					$pfid,
					$pto 
			);
			$this->getSchemeScriptLines ( $rows, $pfid, $line );
			$line = array_filter ( $line ); // 去空
			$line = implode ( ',', $line ); // 转字符串
			$line = explode ( ',', $line );
			$lines [] = $line;
			unset ( $rows [$key] );
		}
		foreach ( $lines as $key => $line ) {
			$allLines = array_merge ( $allLines, $line );
		} */
		/*
		 * Log::info ( $lines ); Log::info ( $this->sortArrayByCount ( $lines ) );
		 */
	}
}

?>