EmployeeUtil = function(me) {
	var tableId = "userlist";
	var employRoot = "/sys/user";
	var zTree, treeId = "role", rightUrl = "/sys/role";
	var oldRoleIds = [];
	return me = {
		initOwn : function() {
			$(".jiegou h3").click(function() {
				$(this).find("span").toggleClass("active");
				$("#projectItem").toggle();
			})
		},
		init : function() {
			me.initOwn();
			me.createList();
			me.ztreeCreate();
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "员工编号",
				"data" : "userCode"
			}, {
				"sTitle" : "员工名称",
				"data" : "userName"
			}, {
				"sTitle" : "邮箱",
				"data" : "email"
			}, {
				"sTitle" : "手机",
				"data" : "tel"
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
			DataTableUtil.load(tableId, employRoot + "/list", aoColumns,
					tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, employRoot, "post",
						requestData, function() {
							callbackfn();
						});
			}
			$("div[name='pwd']").css("display", "");
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, employRoot + "/" + ids,
					"DELETE", "", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, employRoot + "/" + id,
						"PUT", requestData, function() {
							callbackfn();
						}, true);
			}
			CommonUtil.requestService(employRoot + "/" + id + "/edit", "",
					true, "get", function(response, status) {
						if (response.success) {
							$("div[name='pwd']").css("display", "none");
							me.openLayer(yes);
							var employees = response.data;
							$("#userCode").val(employees[0].userCode);
							$("#userName").val(employees[0].userName);
							$("#email").val(employees[0].email);
							$("#tel").val(employees[0].tel);
							$("#orgId").val(employees[0].orgId);
							$("#roleId").val(employees[0].roleId);
							$("#pwd").val(employees[0].pwd);
							for ( var idx in employees) {
								var roleId = employees[idx].roleId;
								if (roleId) {
									oldRoleIds.push(roleId);
									var node = zTree.getNodeByParam("id",
											roleId);
									zTree.checkNode(node);
								}

							}
							me.setCheckRoleValues();
						}
					}, function(ex) {
					});
		},
		resetForm : function() {
			oldRoleIds = [];
			$("#userCode").val("");
			$("#userName").val("");
			$("#email").val("");
			$("#tel").val("");
			$("#orgId").val("");
			$("#roleId").val("");
			$("#roleName").val("");
			$("#pwd").val("");
			zTree.checkAllNodes(false);
			$("#projectItem").css("display", "none");
		},
		openLayer : function(yes) {
			me.resetForm();
			var form = $("#userform");
			var width = form.width() + 30 + 'px';
			layer.open({
				type : 1,
				title : "员工表单信息",
				area : [ width ], // 宽高
				offset : [ '50px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					var error = ValidateUtil.validate("userform");
					if (!error) {
						var requestData = {
							"userCode" : $("#userCode").val(),
							"userName" : $("#userName").val(),
							"email" : $("#email").val(),
							"tel" : $("#tel").val(),
							"orgId" : $("#orgId").val(),
							"pwd" : $("#pwd").val(),
							"roleIds" : me.getCheckRoleIds(),
							"oldRoleIds" : oldRoleIds
						};
						yes(requestData, function() {
							layer.close(index);
							DataTableUtil.refresh(tableId);
						});
					}
				}
			});
		},
		ztreeCreate : function() {
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
					onCheck : me.zTreeOnCheck,
					onAsyncSuccess : function() {

					}
				}
			};
			$.fn.zTree.init($("#" + treeId), setting);
			zTree = $.fn.zTree.getZTreeObj(treeId);
			zTree.setting.edit.drag.isCopy = false;
			zTree.setting.edit.drag.isMove = false;
			zTree.setting.check.chkboxType = {
				"Y" : "",
				"N" : ""
			};
			zTree.expandAll(true);
		},
		getCheckRoleIds : function() {
			var roleIds = [];
			var nodes = zTree.getCheckedNodes(true), v = "";
			for ( var i = 0, l = nodes.length; i < l; i++) {
				roleIds.push(nodes[i].id);
			}
			return roleIds;
		},
		setCheckRoleValues : function() {
			var nodes = zTree.getCheckedNodes(true), v = "";
			for ( var i = 0, l = nodes.length; i < l; i++) {
				v += nodes[i].name + " ";
			}
			$("#roleName").val(v);
		},
		zTreeOnCheck : function(event, treeId, treeNode) {
			me.setCheckRoleValues();
		}
	};
}();
