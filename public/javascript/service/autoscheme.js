AutoSchemeUtil = function(me) {
	var tableId = "schemelist";
	var schemeUrl = "/auto/web/scheme";
	return me = {
		initOwn : function() {
			$("#search").on(
					"click",
					function() {
						var searchReqData = {
							"search" : {
								"projectId" : $("#search_project").val(),
								"state" : $("#search_state").val(),
								"schemeName" : $("#search_schemeName").val(),
								"creater" : $("#search_creater").val()
							}
						};
						DataTableUtil.search(tableId, schemeUrl + "/list",
								searchReqData);
						return false;
					});
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
				"sTitle" : "案例名称",
				"data" : "schemeName"
			}, {
				"sTitle" : "所属项目",
				"data" : "projectName"
			}, {
				"sTitle" : "创建人",
				"data" : "createUser"
			}, {
				"sTitle" : "执行状态",
				"data" : "state"
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
			DataTableUtil
					.load(tableId, schemeUrl + "/list", aoColumns, tablekv);
		},
		refresh : function() {
			if (parent.refreshParent == 1) {
				DataTableUtil.refresh(tableId);
			}
		},
		add : function() {
			layer.open({
				type : 1,
				title : "新建案例",
				skin : '', // 加上边框
				area : [ "830px" ], // 宽高
				offset : [ '50px' ],
				content : $("#schemeform"),
				btn : [ '确定', '取消' ],
				yes : function(index, layero) {
					parent.layer.open({
						type : 2,
						title : "添加",
						skin : '', // 加上边框
						area : [ "1000px", "600px" ], // 宽高
						scrollbar : false,
						maxmin : true,
						content : CommonUtil.getRootPath() + schemeUrl
								+ "/create?schemeName="
								+ $("#schemeName").val(),
						end : function() {
							me.refresh();
						},
						cancel : function() {
							DataTableUtil.optListForm(tableId, schemeUrl + "/"
									+ parent.schemeId, "DELETE", "",
									function() {
									}, false);
						}
					});
					layer.close(index);
				}
			});

		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, schemeUrl + "/" + ids, "DELETE",
					"", function() {
						// DataTableUtil.refresh(tableId);
					}, true);
		},
		edit : function(id) {
			parent.layer.open({
				type : 2,
				title : "编辑",
				skin : '', // 加上边框
				area : [ "1000px", "600px" ], // 宽高
				scrollbar : false,
				maxmin : true,
				content : CommonUtil.getRootPath() + schemeUrl + "/" + id
						+ "/edit",
				end : function() {
					me.refresh();
				}
			});
		},
		exec : function(id) {
			var form = $("#execform");
			var width = form.width() + 30 + 'px';
			var sendEmail = false;
			layer.open({
				type : 1,
				title : "浏览器",
				skin : '', // 加上边框
				offset : [ '50px' ],
				area : [ width ], // 宽高
				content : form,
				btn : [ '确认执行', '取消' ],
				yes : function(index, layero) {
					var selBrowsers = BrowserChecksUtil.getSelBrowsers();
					if (selBrowsers.length > 0) {
						CommonUtil.requestService(schemeUrl + "/exec/" + id, {
							"selBrowsers" : selBrowsers
						}, false, "get", function(response, status) {
							if (response.success) {// 成功
								DataTableUtil.refresh(tableId);
								layer.close(index);
							}
						}, function(error) {
						});
					}
				}
			});

		},
		report : function(id, row) {
			ReportDetailUtil.openReportLog(row.taskExecID, 1);
		}
	};
}();
AutoSchemeDetailUtil = function(me) {
	var schemeId, projectId;
	var attributeModal, alertModal, the_flow_id, _canvas, oldProcess;
	var treeId = "testcase";
	var zTree;
	var container, containerLeft, containerTop, floatLeft, floatTop
	var schemeUrl = "/auto/web/scheme";
	return me = {
		initOwn : function() {
			schemeId = $("#schemeId").val();
			parent.schemeId = schemeId;
			alertModal = $('#alertModal');
			attributeModal = $("#attributeModal");
			// 属性设置
			attributeModal.on("hidden", function() {
				$(this).removeData("modal");// 移除数据，防止缓存
			});
			container = $("#flowdesign_canvas");
			containerLeft = container.offset().left;
			containerTop = container.offset().top;
			floatLeft = container.width() + containerLeft;
			floatTop = container.height() + containerTop;

		},
		init : function() {
			me.initOwn();
			me.create();
			me.bindEvent();
			me.ztreeCreate();
			BrowserChecksUtil.init();
		},
		create : function() {
			CommonUtil.requestService(schemeUrl + "/flowprocess/" + schemeId,
					"", true, "get", function(data, status) {
						if (data.success) {// 成功
							/* 步骤数据 */
							var processData = data.processData;
							the_flow_id = processData.flowid;
							projectId = processData.projectId;
							/* 创建流程设计器 */
							_canvas = $("#flowdesign_canvas").Flowdesign({
								"processData" : processData,
								canvasMenus : {
									"cmAdd" : function(t) {// 右键添加
									},
									"cmSave" : function(t) {// 右键保存
										me.saveFlowScript(false, true);
									},
									"cmRefresh" : function(t) {// 右键刷新
										me.refresh();
									}
								},
								processMenus : {/* 步骤右键 */
									"pmDelete" : function(t) {
										if (confirm("你确定删除步骤吗？")) {
											me.delProcess();
										}
									}/*
										 * , "pmAttribute" : function(t) {//
										 * 步骤右键属性 me.openAttributeForm(); }
										 */
								},
								fnDbClick : function() {
									me.openAttributeForm();
								}
							});
							me.changeOldProcessInfo();
						} else {
						}
					}, function(error) {
					});
		},
		bindEvent : function() {
			/* 保存 */
			$("#saveScheme").bind('click', function() {
				me.saveFlowScript(true, true);
			});
			$("#downScheme").bind('click', function() {
				me.saveFlowScript(false, false, true);
			});
			/* 清除 */
			$("#clearConnect").bind('click', function() {
				_canvas.clear();
			});
		},
		openAttributeForm : function() {
			var activeId = _canvas.getActiveId();// 右键当前的ID
		},
		changeOldProcessInfo : function() {
			oldProcess = _canvas.getProcessInfo();
		},
		closeProcessForm : function(isClose) {
			if (isClose) {
				var winIndex = parent.layer.getFrameIndex(window.name);
				parent.layer.close(winIndex);
			}
		},
		saveFlowScript : function(isClose, aync, down) {
			var newProcess = _canvas.getProcessInfo();
			var opt = $("#opt").val();
			if (opt != 1 && newProcess == oldProcess) {
				me.closeProcessForm(isClose);
				if (down)// 下载
					CommonUtil.redirect(schemeUrl + "/download/" + schemeId
							+ "?down=1");
			} else {
				if (projectId) {
					var requestData = {
						"projectId" : projectId,
						"flowprocess" : newProcess,
						"selBrowsers" : [ 3 ]
					};// 连接信息
					CommonUtil.requestService(schemeUrl + "/saveflowprocess/"
							+ schemeId, requestData, aync, "post", function(
							data, status) {
						if (data.success) {// 成功
							parent.refreshParent = 1;
							me.closeProcessForm(isClose);
							layer.close(index);
						} else {
						}
					}, function(error) {
					});
					if (down)// 下载
						CommonUtil.redirect(schemeUrl + "/download/" + schemeId
								+ "?down=1");
				} else {
					layer.msg("项目不明确，不允许保存，请刷新后重新创建", {
						offset : "50px"
					});
				}
				/*
				 * var form = $("#execform"); var width = form.width() + 30 +
				 * 'px'; var sendEmail = false; layer.open({ type : 1, title :
				 * "浏览器", skin : '', // 加上边框 area : [ width ], // 宽高 content :
				 * form, btn : [ '确认', '取消' ], yes : function(index, layero) {
				 * var selBrowsers = BrowserChecksUtil.getSelBrowsers(); if
				 * (selBrowsers.length > 0) { var requestData = { "flowprocess" :
				 * newProcess, "selBrowsers" : selBrowsers };// 连接信息
				 * CommonUtil.requestService(schemeUrl + "/saveflowprocess/" +
				 * schemeId, requestData, aync, "post", function(data, status) {
				 * if (data.success) {// 成功 parent.refreshParent = 1;
				 * me.closeProcessForm(isClose); } else { } }, function(error) {
				 * }); if (down)// 下载 CommonUtil.redirect(schemeUrl +
				 * "/download/" + schemeId + "?down=1"); } layer.close(index); }
				 * });
				 */
			}
		},
		addProcess : function(requestData) {
			CommonUtil.requestService(schemeUrl + "/addprocess", requestData,
					true, "post", function(data, status) {
						if (data.success) {// 成功
							_canvas.addProcess(data.info);
							// me.changeOldProcessInfo();
						} else {
						}
					}, function(error) {
					});
		},
		delProcess : function() {
			var activeId = _canvas.getActiveId();
			var requestData = {
				"processid" : activeId
			};
			CommonUtil.requestService(schemeUrl + "/delprocess", requestData,
					true, "post", function(data, status) {
						if (data.success) {// 成功
							_canvas.delProcess(activeId);
							// me.changeOldProcessInfo();
							if (_canvas.getProcessInfo() == undefined)
								projectId = 0;
						} else {
						}
					}, function(error) {
					});
		},
		refresh : function() {
			location.reload();
		},
		// 消息提示
		mAlert : function(messages, s) {
			if (!messages)
				messages = "";
			if (!s)
				s = 2000;
			alertModal.find(".modal-body").html(messages);
			alertModal.modal('toggle');
			setTimeout(function() {
				alertModal.modal("hide")
			}, s);
		},
		ajaxModal : function(url, fn) {
			url += url.indexOf('?') ? '&' : '?';
			url += '_t=' + new Date().getTime();
			attributeModal.find(".modal-body").html(
					'<img src="Public/images/loading.gif"/>');
			attributeModal.modal({
				remote : url
			});
			// 加载完成执行
			if (fn) {
				attributeModal.on('shown', fn);
			}
		},
		ztreeCreate : function() {
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + "/auto/web/script/tree",
					autoParam : [ "id" ]
				},
				edit : {
					enable : true,// 允许拖拽
					showRemoveBtn : false,// 删除
					showRenameBtn : false
				// 修改名称
				},
				data : {
					simpleData : {
						enable : true
					}
				},
				callback : {
					onDrop : me.onDrop
				}
			};
			$.fn.zTree.init($("#" + treeId), setting);
			zTree = $.fn.zTree.getZTreeObj(treeId);
			/*
			 * zTree.setting.edit.drag.isCopy = false;
			 * zTree.setting.edit.drag.isMove = false;
			 */
			zTree = $.fn.zTree.getZTreeObj(treeId);
			// 以下三个设置为不允许上下拖拽
			zTree.setting.edit.drag.prev = false;
			zTree.setting.edit.drag.inner = false;
			zTree.setting.edit.drag.next = false;
		},
		getTopNodeId : function(treeNode) {
			var node = treeNode.getParentNode();
			if (node) {
				if (node.level == 1) {
					return node.pId;
				} else
					return me.getTopNodeId(node);
			}
			return 0;
		},
		onDrop : function(event, treeId, treeNode) {
			if (!treeNode[0].isParent) {
				var mLeft = event.clientX;
				var mTop = event.clientY;
				if ((mLeft >= containerLeft && mLeft <= floatLeft)
						&& (mTop >= containerTop && mTop <= floatTop)) {
					var topNodeId = me.getTopNodeId(treeNode[0]);
					if (!projectId || topNodeId == projectId) {
						projectId = topNodeId;
						var requestData = _canvas.getProcessInfo();// 连接信息
						var icon = "";
						if (requestData == "{}")
							icon = "icon-ok";
						var requestData = {
							"flowid" : the_flow_id,
							"processname" : treeNode[0].name,
							"icon" : icon,
							"style" : "left:" + mLeft + "px;top:" + mTop
									+ "px;color:#0e76a8;",
							"relationid" : treeNode[0].id
						};
						me.addProcess(requestData, _canvas);
					} else {
						layer.msg("同一案例不允许跨项目选择脚本", {
							offset : "50px"
						});
					}
				}
			}
		}
	}
}();
