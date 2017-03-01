<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTaskRelationsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_task_relations', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intTaskID' );
			$table->integer ( 'intAttID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_task_relations' );
	}
}
