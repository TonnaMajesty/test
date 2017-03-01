RoleUtil = function(me) {
	var tableId = "rolelist";
	var roleRoot = "/sys/role";
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
				"sTitle" : "角色名称",
				"data" : "roleName"
			}, {
				"sTitle" : "角色描述",
				"data" : "roleDesc"
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
			DataTableUtil.load(tableId, roleRoot + "/list", aoColumns, tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, roleRoot, "post",
						requestData, function() {
							callbackfn();
						});
			}
			me.openLayer(yes);
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, roleRoot + "/" + ids, "DELETE",
					"", function() {
					}, true);
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(tableId, roleRoot + "/" + id, "PUT",
						requestData, function() {
							callbackfn();
						}, true);
			}
			CommonUtil.requestService(roleRoot + "/" + id + "/edit", "", true,
					"get", function(response, status) {
						if (response.success) {
							me.openLayer(yes);
							var role = response.data;
							$("#roleName").val(role.roleName);
							$("#desc").val(role.roleDesc);
						}
					}, function(ex) {
					});
		},
		openLayer : function(yes) {
			var form = $("#roleform");
			var width = form.width() + 30 + 'px';
			layer.open({
				type : 1,
				title : "角色表单信息",
				area : [ width ], // 宽高
				offset : [ '50px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					var error = ValidateUtil.validate("roleform");
					if (!error) {
						var requestData = {
							"roleName" : $("#roleName").val(),
							"desc" : $("#desc").val()
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
