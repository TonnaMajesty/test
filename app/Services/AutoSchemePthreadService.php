<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use App\Utils\FileHelper;

class AutoSchemePthreadService extends \Thread {
	private $rows;
	private $root;
	public function __construct($rows) {
		$this->root = database_path ( "schemes" );
		$this->rows = $rows;
		var_dump ( $rows );
	}
	public function run() {
		$this->makeSchemePackage ();
	}
	/**
	 * 生成案例下载包
	 *
	 * @param unknown $id        	
	 */
	private function makeSchemePackage() {
		$endNodes = $this->getEndNode ( $this->rows );
		foreach ( $endNodes as $endNode ) {
			$endNodeId = $endNode->id;
			$line = array (
					$endNodeId 
			);
			$this->getReferNodes ( $endNodeId, $this->rows, $this->rows, 1, $line );
			$lines [] = array_filter ( $line );
		}
		$resource = $this->root . DIRECTORY_SEPARATOR . "easyTest";
		$dest = $this->root . DIRECTORY_SEPARATOR . $this->rows [0]->chrSchemeName;
		$resource = iconv ( 'UTF-8', 'GB2312', $resource );
		$dest = iconv ( 'UTF-8', 'GB2312', $dest );
		FileHelper::resource_copy ( $resource, $dest ); // 参照拷贝生成一份新的案例
		var_dump("12");
		foreach ( $lines as $line ) {
			// 修改子方案
			foreach ( $this->rows as $row ) {
				if ($line == $row->id) {
					// 修改配置文件
					break;
				}
			}
		}
	}
	
	/**
	 * 获取结束节点
	 *
	 * @param unknown $rows        	
	 */
	private function getEndNode(& $rows) {
		$endNodes = array ();
		foreach ( $rows as $key => $row ) {
			if (empty ( $row->chrProcessTo )) {
				$endNodes [] = $row;
				// unset ( $rows [$key] );
			}
		}
		return $endNodes;
	}
	
	/**
	 * 获取依赖节点
	 *
	 * @param unknown $line        	
	 */
	private function getReferNodes($cid, $rows, $models, $index, & $line) {
		try {
			foreach ( $rows as $key => $row ) {
				$fid = $row->id;
				$pto = $row->chrProcessTo;
				$ptos = explode ( ",", $pto );
				foreach ( $ptos as $pto ) {
					if ($cid == $pto) {
						$sekey = array_search ( $fid, $line );
						if ($sekey !== false) {
							array_splice ( $line, $sekey, 1 );
						}
						array_unshift ( $line, $fid );
					}
				}
				unset ( $rows [$key] );
				array_filter ( $rows );
				if (count ( $rows ) == 0 && $index < count ( $models )) {
					$index ++;
					$this->getReferNodes ( $line [0], $models, $models, $index, $line );
				}
			}
		} catch ( \Exception $e ) {
			throw $e;
		}
	}
}

?>