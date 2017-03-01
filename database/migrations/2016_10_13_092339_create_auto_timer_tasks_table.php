<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTimerTasksTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_timer_tasks', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrTiTaskName', 50 );
			$table->integer ( 'intCreaterID' );
			$table->integer ( 'intModifyID' );
			$table->integer ( 'intFlag' )->default ( 0 );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_timer_tasks' );
	}
}
