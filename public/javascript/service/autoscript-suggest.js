AutoScriptUtil = function(me) {
	var scriptUrl = "/auto/web/script";
	var treeId = "autoscript";
	var treeNode;
	var zTree;
	var tableId = "scriptlist";
	return me = {
		init : function() {
			me.initUploader();
			me.ztreeCreate();
			me.createList();
			me.createSuggest();
		},
		initUploader : function() {
			var uploaderUrl = CommonUtil.getRootPath() + scriptUrl
					+ "/uploader";
			$("#uploader").load(
					uploaderUrl + "?index=1&uploaderServer=" + scriptUrl
							+ "/uploader&action=uploadfile");
			$("#uploaderNext").on("click", function() {
				if (uploaderStatus.length > 0) {
					$("#uploader").hide();
				}
			});
		},
		createSuggest : function() {
			var taobaoBsSuggest = $("#product")
					.bsSuggest(
							{
								indexId : 1,
								indexKey : 0,
								allowNoKeyword : true,
								multiWord : true,
								separator : ",",
								getDataMethod : "url",
								effectiveFieldsAlias : {
									Id : "序号",
									Keyword : "产品"
								},
								showHeader : true,
								url : "http://localhost:8088/testworm/public/auto/web/script/tree?kw=",
								dataType : "text",
								processData : function(response) {
									var suggestData = {
										value : []
									};
									if (!response || response.length == 0) {
										return false
									}
									var len = response.length;
									for ( var kIndex = 0; kIndex < len; kIndex++) {
										suggestData.value.push({
											"Id" : response[kIndex].id,
											"Keyword" : response[kIndex].name
										})
									}
									return suggestData;
								}
							});
		},
		ztreeCreate : function() {
			var oriWidth = $("#" + treeId).width();
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + scriptUrl + "/tree",
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
					onClick : me.zTreeOnClick,
					onExpand : function(event, tId, tNode) {
						zTree.changezTreeStyle(tId);
					},
					onCollapse : function(event, tId, tNode) {
						zTree.changezTreeStyle(tId, oriWidth);
					}
				}
			};
			$.fn.zTree.init($("#" + treeId), setting);
			zTree = $.fn.zTree.getZTreeObj(treeId);
			zTree.setting.edit.drag.isCopy = false;
			zTree.setting.edit.drag.isMove = false;
			zTree.expandAll(true);
		},
		zTreeOnClick : function(event, tId, tNode) {
			if ((!treeNode || treeNode.id != tNode.id) && tNode.isParent) {
				treeId = tId;
				treeNode = tNode;
				var requestData = {
					"nodeId" : tNode.id,
					"isParent" : tNode.isParent
				};
				me.searchScriptList(requestData);
			}
		},
		createList : function() {
			var aoColumns = [ { // <input type='checkbox'>
				"sTitle" : "",
				"data" : "id",
				"sClass" : "text-center"
			}, {
				"sTitle" : "脚本名称",
				"data" : "scriptName"
			}, {
				"sTitle" : "所属产品",
				"data" : "projectName"
			}, {
				"sTitle" : "创建人",
				"data" : "userName",
				"sWidth" : "80px"
			} ];
			var tablekv = {
				"chk" : true,
				"iDisplayLength" : 15,
				"tabtool" : true,
				"edit" : me.edit,
				"addtool" : me.add,
				"deltool" : me.del
			};
			DataTableUtil
					.load(tableId, scriptUrl + "/list", aoColumns, tablekv);
		},
		searchScriptList : function(requestData) {
			DataTableUtil.search(tableId, scriptUrl + "/list", requestData);
		},
		add : function(id) {
			layer.open({
				type : 1,
				title : "上传",
				skin : '', // 加上边框
				area : [ width ], // 宽高
				offset : [ '50px' ],
				content : form,
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {

				}
			});
		},
		del : function(ids) {
		},
		edit : function(id) {
		}
	};
}();
