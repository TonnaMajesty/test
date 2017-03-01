<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTimerRelateTasksTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_timer_relate_tasks', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intTiTaskID' );
			$table->integer ( 'intTaskID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_timer_relate_tasks' );
	}
}
