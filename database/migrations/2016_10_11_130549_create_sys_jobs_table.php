<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysJobsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_jobs', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intBrowser' );
			$table->text ( 'tPayload' );
			$table->tinyInteger ( 'tintState' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'sys_jobs' );
	}
}
