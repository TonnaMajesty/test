<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysDictsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_dicts', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrDictName', 50 );
			$table->string ( 'chrDictValue', 100 );
			$table->string ( 'chrDictValue1', 100 );
			$table->string ( 'chrDictValue2', 100 );
			$table->string ( 'chrDictValue3', 100 );
			$table->string ( 'chrDictValue4', 100 );
			$table->string ( 'chrDictValue5', 100 );
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
		Schema::drop ( 'sys_dicts' );
	}
}
