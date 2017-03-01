<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTimerTaskRportsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_timer_task_rports', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intTiTaskID' );
			$table->integer ( 'intState' );
			$table->integer ( 'intCreaterID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_timer_task_rports' );
	}
}
