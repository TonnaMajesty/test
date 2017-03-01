<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysLogsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_logs', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intUserID' );
			$table->string ( 'chrUrlRoot' );
			$table->string ( 'chrRoute', 100 );
			$table->integer ( 'intAjax' );
			$table->string ( 'chrRequestType', 20 );
			$table->string ( 'chrRequestData' );
			$table->string ( 'chrAreaIP', 20 );
			$table->string ( 'chrUserAgent' );
			$table->string ( 'chrRequestResult' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'sys_logs' );
	}
}
