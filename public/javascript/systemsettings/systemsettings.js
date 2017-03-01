UserUtil = function(me) {
	return me = {
		updateUserOSDisplay : function(requestData) {
			CommonUtil.requestService("/sys/osetting", requestData, true,
					"post", function(response, status) {
						if (response.success) {// 成功
							CommonUtil.redirect("/desktop");
						} else {
						}
					}, function(error) {
					});
		}
	};
}();
FlowScriptUtil = function(me) {
	var attributeModal, alertModal, the_flow_id, _canvas;
	var zTree;
	var container, containerLeft, containerTop, floatLeft, floatTop
	return me = {
		initOwn : function() {
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
		},
		create : function() {
			CommonUtil.requestService("/design/flowprocess", "", true, "get",
					function(data, status) {
						if (data.success) {// 成功
							/* 步骤数据 */
							var processData = data.processData;
							the_flow_id = processData.flowid;
							/* 创建流程设计器 */
							_canvas = $("#flowdesign_canvas").Flowdesign({
								"processData" : processData,
								canvasMenus : {
									"cmAdd" : function(// 右键添加
									t) {
									},
									"cmSave" : function(// 右键保存
									t) {
										me.saveFlowScript();
									},
									"cmRefresh" : function(// 右键刷新
									t) {
										me.refresh();
									}
								},
								processMenus : {/* 步骤右键 */
									"pmDelete" : function(t) {
										if (confirm("你确定删除步骤吗？")) {
											me.delProcess();
										}
									},
									"pmAttribute" : function(// 步骤右键属性
									t) {
										me.openAttributeForm();
									}
								},
								fnDbClick : function() {
									me.openAttributeForm();
								}
							});
						} else {
						}
					}, function(error) {
					});
		},
		bindEvent : function() {
			/* 保存 */
			$("#leipi_save").bind('click', function() {
				me.saveFlowScript(_canvas);
			});
			/* 清除 */
			$("#leipi_clear").bind('click', function() {
				_canvas.clear();
			});
		},
		openAttributeForm : function() {
			var activeId = _canvas.getActiveId();// 右键当前的ID
		},
		saveFlowScript : function() {
			var requestData = {
				"flowprocess" : _canvas.getProcessInfo()
			};// 连接信息
			CommonUtil.requestService("/design/saveflowprocess", requestData,
					true, "post", function(data, status) {
						if (data.success) {// 成功
							me.refresh();
						} else {
						}
					}, function(error) {
					});
		},
		addProcess : function(requestData) {
			CommonUtil.requestService("/design/addprocess", requestData, true,
					"post", function(data, status) {
						if (data.success) {// 成功
							_canvas.addProcess(data.info);
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
			CommonUtil.requestService("/design/delprocess", requestData, true,
					"post", function(data, status) {
						if (data.success) {// 成功
							_canvas.delProcess(activeId);
							me.saveFlowScript();
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
			CommonUtil.requestService("/design/flowprocess", "", true, "get",
					function(data, status) {
						if (data.success) {// 成功
							var setting = {
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
									onRightClick : me.onRightClick,
									onDrop : me.onDrop
								}
							};
							var zNodes = [ {
								id : 1,
								pId : 0,
								name : "展开、折叠 自定义图标不同",
								open : true
							}, {
								id : 2,
								pId : 1,
								name : "叶子节点1",
								iconSkin : "icon01"
							}, {
								id : 3,
								pId : 1,
								name : "叶子节点2"
							}, {
								id : 4,
								pId : 3,
								name : "叶子节点22",
								iconSkin : "icon01"
							} ];
							$.fn.zTree.init($("#treeDemo"), setting, zNodes);
							zTree = $.fn.zTree.getZTreeObj("treeDemo");
							// 以下三个设置为不允许上下拖拽
							zTree.setting.edit.drag.prev = false;
							zTree.setting.edit.drag.inner = false;
							zTree.setting.edit.drag.next = false;
							me.bindRightClientMenu();
						} else {
						}
					}, function(error) {
					});
		},
		bindRightClientMenu : function() {
			return;
			// 添加脚本
			var pData = [ [ {
				text : "添加脚本",
				func : function() {
				}
			} ] ];
			$("span[isparent='true']").smartMenu(pData, {
				name : "zTreeParenRightMenu"
			});
		},
		onRightClick : function(event, treeId, treeNode) {
			if (!treeNode && event.target.tagName.toLowerCase() != "button"
					&& $(event.target).parents("a").length == 0) {
				zTree.cancelSelectedNode();
			} else if (treeNode && !treeNode.noR) {
				zTree.selectNode(treeNode);
			}
		},
		onDrop : function(event, treeId, treeNode) {
			if (!treeNode[0].isParent) {
				var mLeft = event.clientX;
				var mTop = event.clientY;
				if ((mLeft >= containerLeft && mLeft <= floatLeft)
						&& (mTop >= containerTop && mTop <= floatTop)) {
					var requestData = _canvas.getProcessInfo();// 连接信息
					var icon = "";
					if (requestData == "{}")
						icon = "icon-ok";
					var requestData = {
						"flowid" : the_flow_id,
						"processname" : the_flow_id,
						"icon" : icon,
						"style" : "left:" + mLeft + "px;top:" + mTop
								+ "px;color:#0e76a8;"
					};
					me.addProcess(requestData, _canvas);
				}
			}
		}
	}
}();
MenuUtil = function(me) {
	var tableId = "menulist";
	var menuRoot = "/sys/menu";
	return me = {
		initOwn : function() {
		},
		init : function() {
			me.initOwn();
			me.createList();
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "菜单名称",
				"data" : "menuname"
			}, {
				"sTitle" : "菜单顺序号",
				"data" : "menuasc"
			}, {
				"sTitle" : "菜单url",
				"data" : "menuargs"
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
			DataTableUtil.load(tableId, menuRoot + "/list", aoColumns, tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, menuRoot, "post",
						requestData, function() {
							callbackfn();
						});
			}
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, menuRoot + "/" + ids, "DELETE",
					"", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, menuRoot + "/" + id, "PUT",
						requestData, function() {
							callbackfn();
						}, true);
			}
			CommonUtil.requestService(menuRoot + "/" + id + "/edit", "", true,
					"get", function(response, status) {
						if (response.success) {
							me.openLayer(yes);
							var menu = response.menu;
							$("#parentId").val(menu.parentId);
							$("#menuAsc").val(menu.menuasc);
							$("#menuName").val(menu.menuname);
							$("#menuArgs").val(menu.menuargs);
							$("#memo").val(menu.memo);
						}
					}, function(ex) {
					});
		},
		openLayer : function(yes) {
			var form = $("#menuform");
			var width = form.width() + 30 + 'px';
			layer.open({
				type : 1,
				title : "菜单表单信息",
				area : [ width ], // 宽高
				offset : [ '50px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					var error = ValidateUtil.validate("menuform");
					if (!error) {
						var requestData = {
							"parentId" : $("#parentId").val(),
							"menuAsc" : $("#menuAsc").val(),
							"menuName" : $("#menuName").val(),
							"menuArgs" : $("#menuArgs").val(),
							"memo" : $("#memo").val()
						};
						yes(requestData, function() {
							layer.close(index);
							DataTableUtil.refresh(tableId);
						});
					}
				}
			});
		}
	};
}();
