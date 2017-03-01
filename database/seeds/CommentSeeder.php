<?php
use Illuminate\Database\Seeder;
use App\Comment;
class CommentSeeder extends Seeder {
	public function run() {
		DB::table ( 'Comments' )->delete ();
		for($i = 0; $i < 10; $i ++) {
			Comment::create ( [ 
					'nickname' => '评论' . $i,
					'email' => '111' . $i . '@qq.com',
					'content' => '评论内容' . $i,
					'articleid' => 4 
			] );
		}
	}
}

?>