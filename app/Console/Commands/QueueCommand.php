<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Input\InputArgument;
use App\Services\WormQueueService;
use Illuminate\Support\Facades\Log;
use App\Services\AutoLogService;
use App\Utils\RedisHelper;

class QueueCommand extends Command {
	
	/**
	 * The console command name.
	 *
	 * @var string
	 */
	protected $name = 'queue:autolog';
	
	/**
	 * The console command description.
	 *
	 * @var string
	 */
	protected $description = 'Command description.';
	
	/**
	 * Create a new command instance.
	 *
	 * @return void
	 */
	public function __construct() {
		parent::__construct ();
	}
	
	/**
	 * Execute the console command.
	 *
	 * @return mixed
	 */
	public function fire() {
		//
		$connection = $this->argument ( 'connection' );
		$queue = $this->option ( 'queue' );
		$delay = $this->option ( 'delay' );
		$memory = $this->option ( 'memory' );
		$daemon = $this->option ( 'daemon' );
		$tries = $this->option ( 'tries' );
		$this->runQueuer ( $connection, $queue, $delay, $memory, $daemon, $tries );
	}
	
	/**
	 *
	 * @param unknown $connection        	
	 * @param unknown $queue        	
	 * @param unknown $delay        	
	 * @param unknown $memory        	
	 * @param string $daemon        	
	 * @param number $tries        	
	 */
	protected function runQueuer($connection, $queue, $delay, $memory, $daemon, $tries) {
		while ( true ) {
			$this->exec ();
		}
	}
	function exec() {
		$redis = RedisHelper::getInstance ();
		$logs = $redis->brPop ( "autolog", 10 );
		if (count ( $logs ) > 1) {
			$logs = json_decode ( $logs [1], true );
			$scriptId = $logs ["scriptId"]; // 脚本ID
			$schemeId = $logs ["schemeId"]; // 案例ID
			$args = json_decode ( $logs ["uniqueCode"], true ); // log详细信息
			$jobId = $args ["jobId"]; // 工作队列ID
			$reportId = $args ["reportId"];
			$payload = $args ["payload"];
			$browsers = $args ["browsers"];
			$execTaskId = $payload ["execTaskId"]; // 执行任务ID
			$wqService = new WormQueueService ();
			$wqService->moveLogImage ( $logs, $jobId ); // 移动日志图片
			$alogService = new AutoLogService ();
			// 插入日志记录
			$alogService->insert ( $logs, $scriptId, $schemeId, $execTaskId, $jobId, $reportId, $payload, $browsers );
			// 根据回传的日志 更新队列任务以及任务状态
			$wqService->receive ( $jobId, $reportId, $payload, $browsers, $schemeId, $logs ["status"] );
		}
	}
	function getArguments() {
		/*
		 * return [ [ 'example', InputArgument::REQUIRED, 'An example argument.' ] ];
		 */
		return array (
				array (
						'connection',
						InputArgument::OPTIONAL,
						'The name of connection',
						null 
				) 
		);
	}
	
	/**
	 * Get the console command options.
	 *
	 * @return array
	 */
	protected function getOptions() {
		return array (
				array (
						'queue',
						null,
						InputOption::VALUE_OPTIONAL,
						'The queue to listen on' 
				),
				
				array (
						'daemon',
						null,
						InputOption::VALUE_NONE,
						'Run the worker in daemon mode' 
				),
				
				array (
						'delay',
						null,
						InputOption::VALUE_OPTIONAL,
						'Amount of time to delay failed jobs',
						0 
				),
				
				array (
						'force',
						null,
						InputOption::VALUE_NONE,
						'Force the worker to run even in maintenance mode' 
				),
				
				array (
						'memory',
						null,
						InputOption::VALUE_OPTIONAL,
						'The memory limit in megabytes',
						128 
				),
				
				array (
						'sleep',
						null,
						InputOption::VALUE_OPTIONAL,
						'Number of seconds to sleep when no job is available',
						3 
				),
				
				array (
						'tries',
						null,
						InputOption::VALUE_OPTIONAL,
						'Number of times to attempt a job before logging it failed',
						1 
				) 
		);
	}
}
