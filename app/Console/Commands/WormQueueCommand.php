<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Input\InputArgument;
use App\Services\WormQueueService;
use Illuminate\Support\Facades\Log;

class WormQueueCommand extends Command {
	
	/**
	 * The console command name.
	 *
	 * @var string
	 */
	protected $name = 'queue:worm';
	
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
		$this->runWormer ( $connection, $queue, $delay, $memory, $daemon, $tries );
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
	protected function runWormer($connection, $queue, $delay, $memory, $daemon, $tries) {
		$wqService = new WormQueueService ();
		if ($daemon) { // 持续监听
			$sleep = 3;
			while ( true ) {
				$jobs = $wqService->getQueueJobs ();
				if (empty ( $jobs )) {
					sleep ( $sleep );
				} else {
					$ret = $wqService->dispachAutoTask ( $jobs, $connection, $queue, $delay, $memory, $daemon, $tries );
					if (! $ret) { // 有错误 说明有job未处理 则需要等待 避免频繁访问数据库
						sleep ( $sleep );
					}
				}
			}
		}
		// 只监听一次
		$jobs = $wqService->getQueueJobs ();
		return $wqService->dispachAutoTask ( $jobs, $connection, $queue, $delay, $memory, $daemon, $tries );
	}
	
	/**
	 *
	 * @param unknown $connection        	
	 * @param unknown $queue        	
	 * @param unknown $delay        	
	 * @param unknown $memory        	
	 * @param unknown $daemon        	
	 * @param unknown $tries        	
	 */
	public function daemon($connection, $queue, $delay, $memory, $daemon, $tries) {
		while ( true ) {
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
