<?php


namespace App;

use Illuminate\Database\Eloquent\Model;

class Comment extends Model {
	
	//
	public function belongsToArticle() {
		$this->belongsTo ( 'App\Article', 'articleid', 'id' );
	}
}
