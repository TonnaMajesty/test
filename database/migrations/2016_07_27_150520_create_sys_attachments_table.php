<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateSysAttachmentsTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'sys_attachments', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->string ( 'chrFilePath' );
			$table->string ( 'chrFileName', 100 );
			$table->string ( 'chrFileType', 20 );
			$table->float ( 'fltFileSize' );
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
		Schema::drop ( 'sys_attachments' );
	}
}
