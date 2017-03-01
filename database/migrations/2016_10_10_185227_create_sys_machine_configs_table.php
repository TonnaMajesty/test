<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysMachineConfigsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_machine_configs', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intMachineID' );
			$table->integer ( 'intBrowserID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'sys_machine_configs' );
	}
}
