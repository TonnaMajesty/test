<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoScriptRelationsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_script_relations', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intScriptID' );
			$table->integer ( 'intAttID' );
			$table->integer ( 'intFlag' )->default(0);
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_script_relations' );
	}
}
