<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoLogsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_logs', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrResult', 20 );
			$table->string ( 'chrCmd', 100 );
			$table->string ( 'chrCmdParam' );
			$table->string ( 'chrErrorMessage' );
			$table->float ( 'fltDuring' );
			$table->string ( 'chrImage' );
			$table->string ( 'chrElementAlias', 150 );
			$table->string ( 'chrDescription', 50 );
			$table->integer ( 'intLineNo' );
			$table->integer ( 'intLevel' );
			$table->integer ( 'intScriptID' );
			$table->integer ( 'intSchemeID' );
			$table->integer ( 'intTaskID' );
			$table->integer ( 'intTrmerTaskID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_logs' );
	}
}
