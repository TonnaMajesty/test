<?php

namespace App\Services;

use App\SysAttachment;

class AttachmentService {
	
	/**
	 *
	 * @param unknown $file        	
	 */
	public function insert(array $file, $user) {
		$sysAtt = new SysAttachment ();
		$sysAtt->chrFile = $file ['file'];
		$sysAtt->chrFileName = $file ['fileName'];
		$sysAtt->chrFileType = $file ['fileType'];
		$sysAtt->fltFileSize = $file ['fileSize'];
		$sysAtt->intCompanyID = $user->intCompanyID;
		$sysAtt->save ();
		return $sysAtt->id;
	}
}

?>