<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoTaskExecsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_task_execs', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intTaskID' );
			$table->string ( 'chrBrowserIDs' );
			$table->string ( 'chrEmails' );
			$table->integer ( 'intCreaterID' );
			$table->integer ( 'intState' )->default ( 0 ); // 0 未执行 1 执行中 2 执行成功 3 执行失败
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_task_execs' );
	}
}
