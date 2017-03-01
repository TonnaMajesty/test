ProjectUtil = function(me) {
	var tableId = "projectlist";
	var projectUrl = "/project/bill";
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
				"sTitle" : "项目名称",
				"data" : "projectName"
			}, {
				"sTitle" : "备注",
				"data" : "memo"
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
			DataTableUtil.load(tableId, projectUrl + "/list", aoColumns,
					tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, projectUrl, "post",
						requestData, function() {
							callbackfn();
						}, true);
			}
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, projectUrl + "/" + ids,
					"DELETE", "", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, projectUrl + "/" + id,
						"PUT", requestData, function() {
							callbackfn();
						}, true);
			}
			CommonUtil.requestService(projectUrl + "/" + id + "/edit", "",
					true, "get", function(response, status) {
						if (response.success) {
							me.openLayer(yes);
							var project = response.project;
							$("#projectName").val(project.projectName);
							$("#memo").val(project.memo);
						}
					}, function(ex) {
					});
		},
		resetProjectForm : function() {
			$("#projectName").val("");
			$("#memo").val("");
		},
		openLayer : function(yes) {
			me.resetProjectForm();
			var form = $("#projectform");
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
					var error = ValidateUtil.validate("projectform");
					if (!error) {
						var requestData = {
							"projectName" : $("#projectName").val(),
							"memo" : $("#memo").val()
						};
						yes(requestData, function() {
							layer.close(index);
						});
					}
				}
			});
		}
	};
}();

ProductUtil = function(me) {
	var productUrl = "/project/product";
	var treeId = "product";
	var treeNode;
	var zTree;
	return me = {
		initOwn : function() {
			/*
			 * $(".zTreeDemoBackground").width($(window).width() - 50);
			 * $(".ztree").width($(window).width() - 15);
			 * $(".zTreeDemoBackground").height(500);
			 */
			var winWidth = $(window).width();
			$("#projectItem").width(winWidth - 15);
			$("#product").width(winWidth - 40);
			$("#product").height($(window).height() - 100);
		},
		init : function() {
			me.initOwn();
			me.ztreeCreate();
		},
		ztreeCreate : function() {
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + productUrl + "/tree",
					autoParam : [ "id" ]
				},
				edit : {
					enable : true,// 允许编辑
					showRemoveBtn : false,// 删除
					showRenameBtn : true
				// 修改名称
				},
				data : {
					simpleData : {
						enable : true
					}
				},
				callback : {
					onClick : me.zTreeOnClick,
					beforeRename : me.edit
				}
			};
			$.fn.zTree.init($("#" + treeId), setting);
			zTree = $.fn.zTree.getZTreeObj(treeId);
			zTree.setting.edit.drag.isCopy = false;
			zTree.setting.edit.drag.isMove = false;
			// zTree.expandAll(true);
			$("#save").on("click", me.add);
			$("#delete").on("click", me.del);
		},
		zTreeOnClick : function(event, tId, tNode) {
			$(".btn-default").removeAttr("disabled");
			// $(".btn-default").removeClass("btn-default");
			// $("#save").addClass("btn-primary");
			// $("#delete").addClass("btn-danger");
			treeId = tId;
			treeNode = tNode;
		},
		edit : function(tId, tNode, nodeName) {
			if (tNode.name != nodeName) {
				var nodeData = {
					name : nodeName,
					id : tNode.id
				};
				CommonUtil.requestService(productUrl + "/" + tNode.id,
						nodeData, true, "PUT", function(response) {
							if (response.success) {

							} else
								layer.msg("新增失败", {
									offset : "50px"
								});
						}, function(error) {
						});
			}
		},
		add : function(event) {
			var nodes = zTree.getSelectedNodes(), treeNode = nodes[0];
			var nodeData = {
				pId : treeNode.id,
				name : treeNode.name + "子产品"
			};
			CommonUtil.requestService(productUrl, nodeData, true, "post",
					function(response) {
						if (response.success) {
							nodeData["id"] = response.nodeId;
							nodeData["isParent"] = true;
							nodeData["iconSkin"] = "project_node";
							treeNode = zTree.addNodes(treeNode, nodeData);
							zTree.editName(treeNode[0]);
						} else
							layer.msg(response.error, {
								offset : "50px"
							});
					}, function(error) {
					});
		},
		del : function(event) {
			layer.confirm('确定要删除该节点？', {
				offset : "50px",
				btn : [ '是', '否' ]
			}, function(index) {
				var nodes = zTree.getSelectedNodes(), tNode = nodes[0];
				CommonUtil.requestService(productUrl + "/" + tNode.id, "",
						true, "DELETE", function(response) {
							if (response.success) {
								zTree.removeNode(tNode, true);
								layer.close(index);
							} else
								layer.msg("删除失败", {
									offset : "50px"
								});
						}, function(error) {
						});
			});
		}
	};
}();
