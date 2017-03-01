ReportDetailUtil = function(me) {
	return me = {
		openReportLog : function(keyId, taskType) {
			if (keyId) {
				var reportUrl = "/report/bill/" + keyId;
				var requestData = {
					"taskType" : taskType
				};
				parent.layer.open({
					type : 2,
					title : false,
					skin : '', // 加上边框
					area : [ "1000px", "650px" ], // 宽高
					scrollbar : false,
					maxmin : false,
					content : CommonUtil.getRootPath() + reportUrl
							+ "?taskType=" + taskType + "&keyId=" + keyId,
					success : function(layero, index) {
					}
				});
			} else
				layer.msg("报告未生成，暂时不能查看", {
					offset : [ '50px' ]
				});
		}
	};
}();
