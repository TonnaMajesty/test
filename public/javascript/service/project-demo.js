ProjectUtil = function(me) {
	var tableid = "projectlist";
	var projectRoot = "/project";
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
				"edit" : me.edit,
				"addtool" : me.add,
				"deltool" : me.del
			};
			DataTableUtil.load(tableid, projectRoot + "/list", aoColumns,
					tablekv);
		},
		add : function() {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(projectRoot, "post", requestData,
						function() {
							callbackfn();
						});
			}
			me.openLayer(yes);
		},
		del : function(ids) {
			Util.optListForm(projectRoot + "/" + ids, "DELETE", "", function() {
				DataTableUtil.refresh(tableid);
			});
		},
		edit : function(id) {
			function yes(requestData, callbackfn) {
				DataTableUtil.optListForm(projectRoot + "/" + id, "PUT",
						requestData, function() {
							callbackfn();
						});
			}
			CommonUtil.requestService(projectRoot + "/" + id + "/edit", "",
					true, "get", function(response, status) {
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
				title : "基本信息",
				skin : 'layui-layer-rim', // 加上边框
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
							DataTableUtil.refresh(tableid);
						});
					}
				}
			});
		}
	};
}();

ProductUtil = function(me) {
	var treeNode;
	return me = {
		init : function() {
			me.ztreeCreate();
		},
		ztreeCreate : function() {
			var setting = {
				async : {
					type:"get",
					enable : true,
					url : CommonUtil.getRootPath() + "/project/product/tree",
					autoParam : [ "id", "name", "level" ],
					otherParam : {
						"otherParam" : "zTreeAsyncTest"
					}
				},
				edit : {
					enable : true,// 允许拖拽
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
					onClick : me.zTreeOnClick
				}
			};
			//var zNodes = response.data;
			$.fn.zTree.init($("#product"), setting);//, zNodes
			zTree = $.fn.zTree.getZTreeObj("product");
			$("#save").on("click", function() {
			});

		},
		zTreeOnClick : function(event, treeId, node) {
			$(".btn-default").removeAttr("disabled");
			$(".btn-default").removeClass("btn-default");
			$("#save").addClass("btn-primary");
			$("#delete").addClass("btn-danger");
			treeNode = node;
		},
		add : function() {

		}
	};
}();
