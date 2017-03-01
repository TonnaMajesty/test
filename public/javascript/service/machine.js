MachineUtil = function(me) {
	var tableId = "machinelist";
	var machRoot = "/pc/machine";
	return me = {
		initOwn : function() {
		},
		init : function() {
			me.initOwn();
			me.createList();
			BrowserChecksUtil.init();
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "机器名称",
				"data" : "machName"
			}, {
				"sTitle" : "机器IP",
				"data" : "ip"
			}, {
				"sTitle" : "最大运行实例数",
				"data" : "hubMaxCount"
			}, {
				"sTitle" : "当前实例数",
				"data" : "hubNowCount"
			}, {
				"sTitle" : "创建人",
				"data" : "creUserName"
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
					}
				}
			};
			DataTableUtil.load(tableId, machRoot + "/list", aoColumns, tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, machRoot, "post",
						requestData, function() {
							callbackfn();
						});
			}
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, machRoot + "/" + ids, "DELETE",
					"", function() {
					}, true);
		},
		edit : function(id) {
			var browserIds;
			function yes(requestData, callbackfn) {
				requestData.oldBrowserIds = browserIds;
				DataTableUtil.optListForm(tableId, machRoot + "/" + id, "PUT",
						requestData, function() {
							callbackfn();
						}, true);
			}
			CommonUtil.requestService(machRoot + "/" + id + "/edit", "", false,
					"get", function(response, status) {
						if (response.success) {
							me.openLayer(yes);
							var machine = response.data;
							$("#machName").val(machine.machName);
							$("#ip").val(machine.ip);
							$("#hubPort").val(machine.hubPort);
							$("#hub").val(machine.hub);
							$("#hubMaxCount").val(machine.hubMaxCount);
							browserIds = machine.browserIds.split(';');
							for ( var idx in browserIds) {
								$(
										"#browserChecks input[value='"
												+ browserIds[idx] + "']")
										.iCheck('check');
							}
						}
					}, function(ex) {
					});
		},
		resetForm : function() {
			$("#machName").val('');
			$("#ip").val('');
			$("#hubPort").val('4444');
			$("#hub").val('/wd/hub');
			$("#hubMaxCount").val('');
			BrowserChecksUtil.reset();
		},
		openLayer : function(yes) {
			me.resetForm();
			var form = $("#machineform");
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
					var error = ValidateUtil.validate("machineform");
					if (!error) {
						var selBrowsers = BrowserChecksUtil.getSelBrowsers();
						if (selBrowsers.length > 0) {
							var requestData = {
								"machName" : $("#machName").val(),
								"ip" : $("#ip").val(),
								"hubPort" : $("#hubPort").val(),
								"hub" : $("#hub").val(),
								"hubMaxCount" : $("#hubMaxCount").val(),
								"selBrowsers" : selBrowsers
							};
							yes(requestData, function() {
								layer.close(index);
								DataTableUtil.refresh(tableId);
							});
						}
					}
				}
			});
		}
	};
}();
