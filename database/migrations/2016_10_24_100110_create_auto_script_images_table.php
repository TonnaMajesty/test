<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateAutoScriptImagesTable extends Migration {
	
	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up() {
		Schema::create ( 'auto_script_images', function (Blueprint $table) {
			$table->increments ( 'id' );
			$table->integer ( 'intScriptID' );
			$table->integer ( 'intAttID' );
			$table->timestamps ();
		} );
	}
	
	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down() {
		Schema::drop ( 'auto_script_images' );
	}
}
