<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysMachineRelationsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_machine_relations', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intMachineID' );
			$table->integer ( 'intHubPort' );
			$table->string ( 'chrHub' );
			$table->integer ( 'intHubMaxCount' );
			$table->integer ( 'intHubNowCount' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'sys_machine_relations' );
	}
}
