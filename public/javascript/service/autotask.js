AutoTaskUtil = function(me) {
	var tableId = "tasklist";
	var taskUrl = "/auto/web/task";
	var execUrl = taskUrl + "/exec";
	var schemeUrl = "/auto/web/scheme";
	var schTableId = "schemelist", projectId;
	var schemeIds = [];
	var oldSchemeIds = [];
	return me = {
		initOwn : function() {
			$("#search").on(
					"click",
					function() {
						var searchReqData = {
							"search" : {
								"projectId" : $("#search_project").val(),
								"state" : $("#search_state").val(),
								"taskName" : $("#search_taskName").val(),
								"creater" : $("#search_creater").val()
							}
						};
						DataTableUtil.search(tableId, taskUrl + "/list",
								searchReqData);
						return false;
					});
		},
		init : function() {
			me.initOwn();
			me.createList();
			me.createSchemeList();
			BrowserChecksUtil.init();
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
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
			}, {
				"sTitle" : "浏览器",
				"data" : "browserNames"
			} ];
			var request = CommonUtil.getRequest();
			var tablekv = {
				"chk" : true,
				"iDisplayLength" : 15,
				"tabtool" : true,
				"opt" : {
					"edit" : {
						"display" : 1,
						"info" : "编辑",
						"func" : me.edit
					},
					"exec" : {
						"display" : 1,
						"info" : "执行",
						"func" : me.exec
					},
					"report" : {
						"display" : 1,
						"info" : "查看报告",
						"func" : me.report
					}
				}
			};
			if (!request["my"]) {
				var tools = {
					"addtool" : me.add,
					"deltool" : me.del
				};
				$.extend(tablekv, tools);
			}
			DataTableUtil.load(tableId, taskUrl + "/list", aoColumns, tablekv);
		},
		refresh : function() {
			if (parent.refreshParent == 1) {
				DataTableUtil.refresh(tableId);
			}
		},
		add : function() {
			function yes(requestData, callbackfn) {
				if (schemeIds.length > 0) {
					requestData.schemes = schemeIds;
					DataTableUtil.optListForm(tableId, taskUrl, "post",
							requestData, function() {
								callbackfn();
							}, true);
				}
			}
			projectId = 0;
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, taskUrl + "/" + ids, "DELETE",
					"", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				if (schemeIds.length > 0) {
					requestData.schemes = schemeIds;// 新增+未删除的
					requestData.oldSchemeIds = oldSchemeIds;// 原有的
					DataTableUtil.optListForm(tableId, taskUrl + "/" + id,
							"PUT", requestData, function() {
								callbackfn();
							}, true);
				}
			}
			CommonUtil
					.requestService(taskUrl + "/" + id + "/edit", "", false,
							"get", function(response, status) {
								if (response.success) {
									me.openLayer(yes);
									var task = response.task;
									projectId = task.projectId;
									$("#taskName").val(task.taskName);
									for ( var scheme in task.schemes) {
										oldSchemeIds
												.push(task.schemes[scheme].id);
										me.changeCheckedScheme(
												task.schemes[scheme], 0);
									}
								}
							}, function(ex) {
							});
		},
		openLayer : function(yes) {
			me.reloadScheme();
			var form = $("#taskform");
			var width = form.width() + 30 + 'px';
			layer.open({
				type : 1,
				title : "基本信息",
				skin : '', // 加上边框
				area : [ width ], // 宽高
				offset : [ '50px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					var error = ValidateUtil.validate("taskform");
					if (!error) {
						var requestData = {
							"taskName" : $("#taskName").val(),
							"projectId" : projectId
						};
						yes(requestData, function() {
							layer.close(index);
						});
					}
				}
			});
		},
		createSchemeList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "案例名称",
				"data" : "schemeName"
			}, {
				"sTitle" : "项目名称",
				"data" : "projectName"
			}, {
				"sTitle" : "创建人",
				"data" : "createUser"
			} ];
			var tablekv = {
				"chk" : me.schemeCheck,
				"iDisplayLength" : 5
			};
			DataTableUtil.load(schTableId, schemeUrl + "/list", aoColumns,
					tablekv);
		},
		schemeCheck : function(event, ck) {
			var row = JSON.parse($(ck).attr("row"));
			switch (event.type) {
			case "ifChecked":// 选中
				me.changeCheckedScheme(row, 0);
				break;
			case "ifUnchecked":// 取消选中
				me.changeCheckedScheme(row, 1);
				break;
			}
		},
		reloadScheme : function() {
			$('#taskform input').iCheck('uncheck');
			// DataTableUtil.refresh(schTableId);
			$("#taskName").val("");
			$("#checkedScheme").html("");
			schemeIds = [];
			oldSchemeIds = [];
		},
		changeCheckedScheme : function(row, opt) {
			var conId = "check_" + row.id;
			var idx = $.inArray(row.id, schemeIds);
			switch (opt) {
			case 0:// 选中
				if (!projectId || projectId == undefined
						|| projectId == row.projectId) {
					projectId = row.projectId;
					if (idx < 0) {
						schemeIds.push(row.id);
						$("#checkedScheme").append(
								"<span chk='shceme' id='" + conId + "'>"
										+ row.schemeName + "<br/></span>");
					}
				} else
					layer.msg("同一任务不允许包含不同项目的案例", {
						offset : "50px"
					});
				break;
			case 1:// 取消选中
				if (idx >= 0) {
					schemeIds.splice(idx, 1);
					$("#" + conId).remove();
					if (schemeIds.length == 0)
						projectId = 0;
				}
				break;
			}

		},
		exec : function(id) {
			me.execReload();
			CommonUtil.requestService(execUrl + "/" + id, "", true, "get",
					function(response, status) {
						if (response.success) {
							me.execDetail(id, response.data);
						}
					}, function(ex) {
					});

		},
		execReload : function() {
			BrowserChecksUtil.reset();
			$('#browserChecks input').iCheck('uncheck');
			$("input[name='email']:first").iCheck('check');
			$("#emailReceiver").css({
				"display" : "none"
			});
			$("#emailReceivers").val('');
		},
		execDetail : function(id, detail) {
			var form = $("#execform");
			var width = form.width() + 30 + 'px';
			var sendEmail = false;
			layer.open({
				type : 1,
				title : "任务执行",
				skin : '', // 加上边框
				offset : [ '50px' ],
				area : [ width ], // 宽高
				content : form,
				btn : [ '确认执行', '取消' ],
				yes : function(index, layero) {
					var selBrowsers = BrowserChecksUtil.getSelBrowsers();
					if (selBrowsers.length > 0) {
						var requestData = {
							"selBrowsers" : selBrowsers,
							"emails" : (sendEmail ? $("#emailReceivers").val()
									: ""),
							"taskId" : id
						};
						DataTableUtil.optListForm(tableId, execUrl, "post",
								requestData, function(response) {
									layer.close(index);
								}, true);
					}
				}
			});

			$("input[name='email']").off("ifChecked");
			$("input[name='email']").on("ifChecked", function(event) {
				var option = $(this).val();
				var erCss = {
					"display" : "none"
				};
				sendEmail = false;
				if (option == "1") {
					erCss = {
						"display" : ""
					};
					sendEmail = true;
				}
				$("#emailReceiver").css(erCss);
			});
			if (detail) {// 编辑
				/*
				 * asynType = "PUT"; optUrl += "/" + id;
				 */
				var browserIds = detail.browserIds.split(";");
				for ( var broIdx in browserIds) {
					$(
							"#browserChecks input[value='" + browserIds[broIdx]
									+ "']").iCheck("check");
				}
				$("input[name='email'][value='" + detail.sendEmail + "']")
						.iCheck("check");
				$("#emailReceivers").val(detail.emails);
			}

		},
		report : function(id, row) {
			ReportDetailUtil.openReportLog(row.taskExecID, 1);
		}
	};
}();
