TimerTaskUtil = function(me) {
	var tableId = "titasklist";
	var titaskUrl = "/mytask/timer";
	var taskIds = [];
	var oldTaskIds = [];
	var projectId;
	return me = {
		initOwn : function() {
			$("#search").on(
					"click",
					function() {
						var searchReqData = {
							"search" : {
								"projectId" : $("#search_project").val(),
								"testType" : $("#search_testType").val(),
								"state" : $("#search_state").val(),
								"taskName" : $("#search_taskName").val(),
								"creater" : $("#search_creater").val()
							}
						};
						DataTableUtil.search(tableId, titaskUrl + "/list",
								searchReqData);
						return false;
					});
			$("#execDateTime .input-daterange").datepicker({
				keyboardNavigation : false,
				forceParse : false,
				autoclose : true
			});
			$(".clockpicker").clockpicker();
		},
		init : function() {
			me.initOwn();
			me.createList();
			me.createTaskList();
			BrowserChecksUtil.init();
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "定时任务名称",
				"data" : "tiTaskName"
			}, {
				"sTitle" : "所属项目",
				"data" : "projectName"
			}, {
				"sTitle" : "任务类型",
				"data" : "taskType"
			}, {
				"sTitle" : "执行次数",
				"data" : "execCount"
			}, {
				"sTitle" : "状态",
				"data" : "state"
			}, {
				"sTitle" : "创建人",
				"data" : "userName"
			}, {
				"sTitle" : "浏览器",
				"data" : "browserNames"
			} ];
			var tablekv = {
				"chk" : true,
				"iDisplayLength" : 15,
				"tabtool" : true,
				"addtool" : me.add,
				"deltool" : me.del,
				"opt" : {
					"edit" : {
						"display" : 1,
						"info" : "编辑",
						"func" : me.edit
					},
					"report" : {
						"display" : 1,
						"info" : "查看报告",
						"func" : me.report
					}
				}
			};
			DataTableUtil
					.load(tableId, titaskUrl + "/list", aoColumns, tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, titaskUrl, "post",
						requestData, function(reponse) {
							callbackfn();
						}, true);
			}
			projectId = 0;
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, titaskUrl + "/" + ids, "DELETE",
					"", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				requestData.oldTaskIds = oldTaskIds;
				DataTableUtil.optListForm(tableId, titaskUrl + "/" + id, "PUT",
						requestData, function(reponse) {
							callbackfn();
						}, true);
			}
			function setControllers(titask) {
				$("#titaskName").val(titask[0].titaskName);
				$("#titaskType").val(titask[0].titaskType);
				$("#execRate").val(titask[0].execRate);
				$("#execTime").val(titask[0].execTime);
				$("#execBeginDate").datepicker("setDate",
						titask[0].execBeginDate);
				$("#execEndDate").datepicker("setDate", titask[0].execEndDate);
				$("#emailReceivers").val(titask[0].emails);
				projectId = titask[0].projectId;
				for ( var tit in titask) {
					oldTaskIds.push(titask[tit].id);
					me.changeCheckedTask(titask[tit], 0);
				}
				var browsers = titask[0].execBrowserIds.split(";");
				for ( var bidx in browsers) {
					$("#browserChecks input[value='" + browsers[bidx] + "']")
							.iCheck("check");
				}
			}
			CommonUtil.requestService(titaskUrl + "/" + id + "/edit", "",
					false, "get", function(response, status) {
						if (response.success) {
							me.openLayer(yes);
							var titask = response.data;
							setControllers(titask);
						}
					}, function(ex) {
					});
		},
		openLayer : function(yes) {
			me.reloadTask();
			var form = $("#titaskform");
			var width = form.width() + 30 + 'px';
			layer.open({
				type : 1,
				title : "基本信息",
				skin : '', // 加上边框
				area : [ width ], // 宽高
				offset : [ '20px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					var error = ValidateUtil.validate("titaskform");
					if (!error) {
						var selBrowsers = BrowserChecksUtil.getSelBrowsers();
						if (selBrowsers.length > 0) {
							if (taskIds.length > 0) {
								var requestData = {
									"titaskName" : $("#titaskName").val(),
									"titaskType" : $("#titaskType").val(),
									"execRate" : $("#execRate").val(),
									"execTime" : $("#execTime").val(),
									"execBeginDate" : $("#execBeginDate")
											.datepicker({
												dateFormat : "dd-mm-yy"
											}).val(),
									"execEndDate" : $("#execEndDate")
											.datepicker({
												dateFormat : "dd-mm-yy"
											}).val(),
									"selBrowsers" : selBrowsers,
									"taskIds" : taskIds,
									"emails" : $("#emailReceivers").val(),
									"projectId" : projectId
								};
								yes(requestData, function() {
									layer.close(index);
								});
							} else {
								layer.msg("请选择任务", {
									offset : "50px"
								});
							}
						} else {
							layer.msg("请选择浏览器", {
								offset : "50px"
							});
						}
					}
				}
			});
		},
		report : function(id, row) {
			ReportDetailUtil.openReportLog(row.reportId, 2);
		},
		createTaskList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
			}, {
				"sTitle" : "任务名称",
				"data" : "taskName"
			}, {
				"sTitle" : "所属项目",
				"data" : "projectName"
			}, {
				"sTitle" : "创建人",
				"data" : "createUser"
			}, {
				"sTitle" : "任务状态",
				"data" : "state"
			} ];
			var tablekv = {
				"chk" : me.taskCheck,
				"iDisplayLength" : 5
			};
			DataTableUtil.load("tasklist", "/auto/web/task/list", aoColumns,
					tablekv);
		},
		taskCheck : function(event, ck) {
			var row = JSON.parse($(ck).attr("row"));
			switch (event.type) {
			case "ifChecked":// 选中
				me.changeCheckedTask(row, 0);
				break;
			case "ifUnchecked":// 取消选中
				me.changeCheckedTask(row, 1);
				break;
			}
		},
		reloadTask : function() {
			$("#titaskName").val("");
			$("#titaskType").val("");
			$("#execRate").val("");
			$("#execTime").val("");
			$("#execBeginDate").val('');
			$("#checkedTask").html("");
			$("#execBeginDate").datepicker("setDate",
					CommonUtil.DateFormat(new Date(), "yyyy-MM-dd"));
			$("#execEndDate").datepicker("setDate",
					CommonUtil.DateFormat(new Date(), "yyyy-MM-dd"));
			$("#emailReceivers").val("");
			$('#tasklist input').iCheck('uncheck');
			taskIds = [];
			oldTaskIds = [];
			BrowserChecksUtil.reset();
		},
		changeCheckedTask : function(row, opt) {
			var rowId = row.id;
			var conId = "check_" + rowId;
			var idx = $.inArray(rowId, taskIds);
			switch (opt) {
			case 0:// 选中
				if (!projectId || projectId == undefined
						|| projectId == row.projectId) {
					projectId = row.projectId;
					if (idx < 0) {
						taskIds.push(rowId);
						$("#checkedTask").append(
								"<span chk='task' id='" + conId + "'>"
										+ row.taskName + "<br/></span>");
					}
				} else
					layer.msg("同一定时任务不允许包含不同项目的任务", {
						offset : "50px"
					});
				break;
			case 1:// 取消选中
				if (idx >= 0) {
					taskIds.splice($.inArray(rowId, taskIds), 1);
					$("#" + conId).remove();
					if (taskIds.length == 0)
						projectId = 0;
				}
				break;
			}

		}
	};
}();
