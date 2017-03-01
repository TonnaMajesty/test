ReportUtil = function(me) {
	var tableId = "reportlist";
	var reportRoot = "/report/bill";
	return me = {
		initOwn : function() {
			$("#search").on(
					"click",
					function() {
						var searchReqData = {
							"search" : {
								"projectId" : $("#search_project").val(),
								"reportType" : $("#search_reportType").val(),
								"state" : $("#search_state").val(),
								"taskName" : $("#search_taskName").val(),
								"creater" : $("#search_creater").val()
							}
						};
						DataTableUtil.search(tableId, reportRoot + "/list",
								searchReqData);
						return false;
					});
		},
		init : function() {
			me.initOwn();
			me.createList();
		},
		createList : function() {
			var aoColumns = [ {
				"sTitle" : "报告类型",
				"data" : "reportType"
			}, {
				"sTitle" : "任务名称",
				"data" : "taskName"
			}, {
				"sTitle" : "所属项目",
				"data" : "projectName"
			}, {
				"sTitle" : "执行状态",
				"data" : "state"
			}, {
				"sTitle" : "任务所属人",
				"data" : "userName"
			}, {
				"sTitle" : "报告生成时间",
				"data" : "created_at"
			} ];
			var tablekv = {
				"iDisplayLength" : 15,
				"tabtool" : true,
				"opt" : {
					"" : {
						"info" : ""
					},
					"report" : {
						"display" : 1,
						"info" : "查看报告",
						"func" : me.report
					}
				}
			};
			DataTableUtil.load(tableId, reportRoot + "/list", aoColumns,
					tablekv);
		},
		report : function(id, row) {
			ReportDetailUtil.openReportLog(row.id, 2);
		}
	};
}();
