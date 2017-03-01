AllotRightUtil = function(me) {
	var allotRightUrl = "/sys/allotright";
	var rightUrl = "/sys/right";
	var roleUrl = "/sys/role";
	var treeId = "role";
	var perTreeId = "permissions";
	var perDataTreeId = "dataPermissions";
	var treeNode;
	var zTree, zPermTree, oldCheckNodes = [], zDataPermTree, oldDataCheckNodes = [];
	return me = {
		initOwn : function() {
			var winWidth = $(window).width();
			var item = 300;
			var treeHeight = $(window).height() - 100;
			$("#projectItem").width(item);
			$("#" + treeId).width(item);
			$("#" + treeId).height(treeHeight);
			var permWidth = winWidth - 450;
			$("#permItem").width(permWidth);
			$("#" + perTreeId).width(permWidth - 25);
			$("#" + perTreeId).height(treeHeight - 25);
			$("#" + perDataTreeId).width(permWidth - 25);
			$("#" + perDataTreeId).height(treeHeight - 25);
			$("#save").on("click", function() {
				me.save();
			});
			$("#myTab li").click(function() {
				$(this).addClass("active").siblings().removeClass("active");
				$(this).addClass("active").siblings().each(function() {
					var tab = $(this).attr("href");
					$(tab).css("display", "none");
				});
				var tab = $(this).attr("href");
				$(tab).css("display", "");
			})
		},
		init : function() {
			me.initOwn();
			me.ztreeCreate();
			me.ztreePermCreate();
			me.ztreeDataPermCreate();
		},
		ztreeCreate : function() {
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + roleUrl + "/tree",
					autoParam : [ "id" ]
				},
				edit : {
					enable : false,// 允许编辑
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
					beforeClick : me.zTreeBeforeClick,
					onClick : me.zTreeOnClick,
					beforeRename : me.edit
				}
			};
			$.fn.zTree.init($("#" + treeId), setting);
			zTree = $.fn.zTree.getZTreeObj(treeId);
			zTree.setting.edit.drag.isCopy = false;
			zTree.setting.edit.drag.isMove = false;
			zTree.expandAll(true);
		},
		zTreeBeforeClick : function(treeId, treeNode, clickFlag) {
		},
		zTreeOnClick : function(event, tId, tNode) {
			if (!treeNode || treeNode.id != tNode.id) {
				treeNode = tNode;
				zPermTree.checkAllNodes(false);
				zDataPermTree.checkAllNodes(false);
				CommonUtil.requestService(allotRightUrl + "/" + tNode.id, "",
						true, "get", function(response) {
							if (response.success) {
								var pvis = response.data;
								// 功能权限
								for ( var idx in pvis) {
									var node = zPermTree.getNodeByParam("id",
											pvis[idx].pvId);
									if (node)
										zPermTree.checkNode(node);
									else {
										node = zDataPermTree.getNodeByParam(
												"id", pvis[idx].pvId);
										if (node)
											zDataPermTree.checkNode(node);
									}
								}
								me.setOldPermChecks();
								// 数据权限
							}
						}, function(error) {
						});
			}
		},
		ztreePermCreate : function() {
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + rightUrl + "/tree",
					autoParam : [ "id" ]
				},
				check : {
					enable : true
				},
				edit : {
					enable : false,// 允许编辑
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
					onAsyncSuccess : function() {

					}
				}
			};
			$.fn.zTree.init($("#" + perTreeId), setting);
			zPermTree = $.fn.zTree.getZTreeObj(perTreeId);
			zPermTree.setting.edit.drag.isCopy = false;
			zPermTree.setting.edit.drag.isMove = false;
			zPermTree.setting.check.chkboxType = {
				"Y" : "ps",
				"N" : "s"
			};
			zPermTree.expandAll(true);
		},
		ztreeDataPermCreate : function() {
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + rightUrl + "/dtree",
					autoParam : [ "id" ]
				},
				check : {
					enable : true
				},
				edit : {
					enable : false,// 允许编辑
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
					onAsyncSuccess : function() {

					}
				}
			};
			$.fn.zTree.init($("#" + perDataTreeId), setting);
			zDataPermTree = $.fn.zTree.getZTreeObj(perDataTreeId);
			zDataPermTree.setting.edit.drag.isCopy = false;
			zDataPermTree.setting.edit.drag.isMove = false;
			zDataPermTree.setting.check.chkboxType = {
				"Y" : "ps",
				"N" : "ps"
			};
			zDataPermTree.expandAll(true);
		},
		setOldPermChecks : function() {
			oldCheckNodes = [];
			oldDataCheckNodes = [];
			var checkNodes = zPermTree.getCheckedNodes(true);
			if (checkNodes.length > 0) {
				for ( var idx in checkNodes) {
					oldCheckNodes.push(checkNodes[idx].id);
				}
			}
			checkNodes = zDataPermTree.getCheckedNodes(true);
			if (checkNodes.length > 0) {
				for ( var idx in checkNodes) {
					oldDataCheckNodes.push(checkNodes[idx].id);
				}
			}
		},
		save : function() {
			if (treeNode) {
				var checkNodes = zPermTree.getCheckedNodes(true);
				var checkDataNodes = zDataPermTree.getCheckedNodes(true);
				if (checkNodes.length > 0) {
					var nodePerm = [];
					for ( var idx in checkNodes) {
						var node = {
							"id" : checkNodes[idx].id,
							"type" : checkNodes[idx].type
						};
						nodePerm.push(node);
					}
					var nodeDataPerm = [];
					for ( var idx in checkDataNodes) {
						var node = {
							"id" : checkDataNodes[idx].id,
							"type" : checkDataNodes[idx].type
						};
						nodeDataPerm.push(node);
					}
					CommonUtil.requestService(allotRightUrl, {
						"roleId" : treeNode.id,
						"funcPerm" : {
							"node" : nodePerm,
							"oldNode" : oldCheckNodes
						},
						"dataPerm" : {
							"node" : nodeDataPerm,
							"oldNode" : oldDataCheckNodes
						}
					}, false, "post", function(response) {
						if (response.success) {
							me.setOldPermChecks();
							layer.msg("保存成功", {
								offset : "50px"
							});
						} else
							layer.msg("保存失败", {
								offset : "50px"
							});
					}, function(error) {
					});
				}
			}
		}
	};
}();
