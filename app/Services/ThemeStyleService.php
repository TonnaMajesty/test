<?php

namespace App\Services;

use Illuminate\Support\Facades\DB;

class ThemeStyleService {
	protected $userId;
	
	/**
	 * 获取所有主题样式
	 * 数组返回值为：$themes,$styles
	 *
	 * @param unknown $userId
	 *        	当前用户ID
	 * @return multitype:string
	 */
	public function getThemeStyle($userId) {
		$this->userId = $userId;
		$themes = "[";
		$styles = "[";
		$res = DB::select ( 'select img.id,img.chrsmallbgpath,img.chrdisplaybgpath,img.chrimgname,
				img.intimgtypeid,img.intisshare,img.chrimgenname,img.intcreaterid,
				ts.id as styleid 
				from sys_img_details as img
				left join sys_theme_styles as ts on ts.intImgDetailID=img.id
				where intImgTypeID=4 or intImgTypeID=5' );
		foreach ( $res as $rows ) {
			if ($rows->intimgtypeid == 4) 			// 桌面背景图片
			{
				$themes .= "{";
				$themes .= "id:'" . $rows->id . "',";
				$themes .= "themeid:'" . $rows->chrimgenname . "',";
				$themes .= "smallBg:'" . $rows->chrsmallbgpath . "',";
				$themes .= "displayBg:'" . $rows->chrdisplaybgpath . "',";
				$themes .= "imgName:'" . $rows->chrimgname . "',";
				$themes .= "isShare:'" . $rows->intisshare . "',";
				$themes .= "creater:'" . $rows->intcreaterid . "'";
				$themes .= "},";
			} else if ($rows->intimgtypeid == 5) 			// 系统样式图片
			{
				$styles .= "{";
				$styles .= "id:'" . $rows->id . "',";
				$styles .= "themeid:'" . $rows->chrimgenname . "',";
				$styles .= "smallBg:'" . $rows->chrsmallbgpath . "',";
				$styles .= "displayBg:'" . $rows->chrdisplaybgpath . "',";
				$styles .= "imgName:'" . $rows->chrimgname . "',";
				$styles .= "isShare:'" . $rows->intisshare . "',";
				$styles .= "creater:'" . $rows->intcreaterid . "',";
				$styles .= "styleID:'" . $rows->styleid . "'";
				$styles .= "},";
			}
		}
		$themes = substr ( $themes, 0, - 1 );
		$styles = substr ( $styles, 0, - 1 );
		$themes .= "]";
		$styles .= "]";
		return array (
				"themes" => $themes,
				"styles" => $styles 
		);
	}
}