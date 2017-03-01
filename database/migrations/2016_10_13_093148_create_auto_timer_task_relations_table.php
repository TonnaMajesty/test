<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTimerTaskRelationsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_timer_task_relations', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intTiTaskID' );
			$table->string ( 'intExecRateID' );
			$table->date ( 'dtExecDate' );
			$table->integer ( 'intExecTime' );
			$table->integer ( 'intExecCount' );
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
		Schema::drop ( 'auto_timer_task_relations' );
	}
}
