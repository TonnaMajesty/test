<?php

namespace App\Utils;

class StringUtil {
	
	/**
	 * 判断字符串开头
	 * startWith("abcdef",'a');
	 *
	 * @param unknown $string        	
	 * @param unknown $find        	
	 * @param string $cps        	
	 * @return boolean
	 */
	public static function startWith($string, $find, $cps = false) {
		if ($cps) // 区分大小写
			return strpos ( $string, $find ) === 0;
		return stripos ( $string, $find ) == 0;
	}
	
	/**
	 * 判断字符串结尾
	 * startWith("abcdef",'f');
	 *
	 * @param unknown $string        	
	 * @param unknown $find        	
	 * @param string $cps        	
	 * @return boolean
	 */
	public static function endWith($string, $find, $cps = false) {
		if ($cps) // 区分大小写
			return (($pos = strrpos ( $string, $find )) !== false && $pos == strlen ( $string ) - strlen ( $find ));
		return (($pos = strripos ( $string, $find )) !== false && $pos == strlen ( $string ) - strlen ( $find ));
	}
	
	/**
	 *
	 * @param unknown $string        	
	 */
	public static function iconv($string) {
		return iconv ( "UTF-8", "gbk", $string );
	}
	
	/**
	 *
	 * @param unknown $string        	
	 */
	public static function iconv_UTF($string) {
		return iconv ( "gbk", "UTF-8", $string );
	}
}

?>