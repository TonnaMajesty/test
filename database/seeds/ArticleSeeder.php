<?php


use Illuminate\Database\Seeder;
use App\Article;

class ArticleSeeder extends Seeder {
	public function run() {
		DB::table ( 'articles' )->delete ();
		for($i = 0; $i < 10; $i ++) {
			Article::create ( [ 
					'title' => 'Article' . $i,
					'content' => '内容' . $i,
					'userid' => 1 
			] );
		}
	}
}
?>