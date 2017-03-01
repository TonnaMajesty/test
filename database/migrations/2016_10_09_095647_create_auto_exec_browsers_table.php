<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoExecBrowsersTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_exec_browsers', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrBrowserName', 30 );
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
		Schema::drop ( 'auto_exec_browsers' );
	}
}
