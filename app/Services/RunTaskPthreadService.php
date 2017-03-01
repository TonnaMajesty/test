<?php

namespace App\Services;

use Illuminate\Support\Facades\Log;

class RunTaskPthreadService extends \Thread {
	private $run;
	public function __construct($run) {
		$this->run = $run;
	}
	public function run() {
		exec ( "cmd /c $this->run", $ret, $status );
		if ($status == 0) {
		}
	}
}

?>