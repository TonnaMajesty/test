OrganizeUtil = function(me) {
	var orgUrl = "/sys/org";
	var treeId = "org";
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
			$("#org").width(winWidth - 40);
			$("#org").height($(window).height() - 100);
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
					url : CommonUtil.getRootPath() + orgUrl + "/tree",
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
			zTree.expandAll(true);
			$("#save").on("click", me.add);
			$("#delete").on("click", me.del);
		},
		zTreeOnClick : function(event, tId, tNode) {
			treeId = tId;
			treeNode = tNode;
		},
		edit : function(tId, tNode, nodeName) {
			if (tNode.name != nodeName) {
				var nodeData = {
					name : nodeName,
					id : tNode.id
				};
				CommonUtil.requestService(orgUrl + "/" + tNode.id, nodeData,
						true, "PUT", function(response) {
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
				name : treeNode.name + "子机构"
			};
			CommonUtil.requestService(orgUrl, nodeData, true, "post", function(
					response) {
				if (response.success) {
					nodeData["id"] = response.nodeId;
					nodeData["isParent"] = true;
					nodeData["iconSkin"] = "project_node";
					treeNode = zTree.addNodes(treeNode, nodeData);
					zTree.editName(treeNode[0]);
				} else
					layer.msg("新增失败", {
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
				CommonUtil.requestService(orgUrl + "/" + tNode.id, "", true,
						"DELETE", function(response) {
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
