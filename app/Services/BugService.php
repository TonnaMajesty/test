<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\Utils\FileHelper;

class BugService {
	public $filter = ['id','title','newtitle','description','time','reportid'];

	public function add($data)
	{
		if (!isset($data['reportid'])) {
			return '{success:0,error:reportid必传}';
		}
		$data['time'] = date('Y-m-d H:i:s');
		$data = array_only($data, $this->filter);
		$result = DB::table('bug')->insertGetId($data);
		if ($result) {
			return '{success:1}';
		}
	}

	public function getBugByReportID($ReportID)
	{
		$result = json_encode(DB::select("SELECT * from bug where reportid=$ReportID"));
		return "{success:1,data:$result}";
	}

	public function update($data)
	{
		if (!isset($data['id'])) {
			return '{success:1,error:id必传}';			
		}
		$data['time'] = date('Y-m-d H:i:s');
		$result = DB::table('bug')->where('id', $data['id'])->update($data);
		if ($result) {
			return '{success:1}';
		}
	}
}

?>