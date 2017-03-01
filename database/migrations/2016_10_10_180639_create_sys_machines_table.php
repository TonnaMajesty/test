<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysMachinesTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_machines', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrMachName', 50 );
			$table->string ( 'chrIp', 30 );
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
		Schema::drop ( 'sys_machines' );
	}
}
