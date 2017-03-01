var scriptUrl = "/auto/web/script";
var proTreeUrl = scriptUrl + "/tree";
AutoScriptUtil = function(me) {
	var treeId = "autoscript";
	var treeNode, zTree, searchReqData = {}, tableId = "scriptlist";
	var nowAttId;
	return me = {
		initOwn : function() {
			$("#search").on("click", function() {
				me.searchScriptList();
				return false;
			});
			$("#autoscript").height($("#projectItem").height() - 10);
		},
		init : function() {
			me.initOwn();
			me.ztreeCreate();
			me.createList();
			me.bindEvent();
		},
		ztreeCreate : function() {
			var oriWidth = $("#" + treeId).width();
			var setting = {
				async : {
					type : "get",
					enable : true,
					url : CommonUtil.getRootPath() + proTreeUrl,
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
					onClick : me.zTreeOnClick
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
				searchReqData = {
					"nodeId" : tNode.id,
					"isParent" : tNode.isParent
				};
				me.searchScriptList();
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
				"sTitle" : "所属项目",
				"data" : "projectName"
			}, {
				"sTitle" : "所属模块",
				"data" : "productName"
			}, {
				"sTitle" : "是否上传参数",
				"data" : "param"
			}, {
				"sTitle" : "是否上传附件",
				"data" : "files"
			}, {
				"sTitle" : "创建人",
				"data" : "userName",
				"sWidth" : "80px"
			}, {
				"sTitle" : "应用版本",
				"data" : "version"
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
					"view" : {
						"display" : 1,
						"info" : "查看",
						"func" : me.view
					},
					"param" : {
						"display" : 1,
						"info" : "上传参数文件",
						"func" : me.uploadParams
					},
					"uploadImgae" : {
						"display" : 1,
						"info" : "上传图片",
						"func" : me.uploadImages
					},
					"back" : {
						"display" : 1,
						"info" : "回滚",
						"func" : me.rollback
					},
					"backLog" : {
						"display" : 1,
						"info" : "日志",
						"func" : me.scriptBackLog
					}
				}
			};
			DataTableUtil
					.load(tableId, scriptUrl + "/list", aoColumns, tablekv);
		},
		bindEvent : function() {
			$(".jiegou h3").click(function() {
				$(this).find("span").toggleClass("active");
				$("#projectItem").toggle();
			})
		},
		searchScriptList : function() {
			var requestData = {
				"scriptName" : $("#search_scriptName").val(),
				"uploadArgs" : $("#search_uploadArgs").val(),
				"uploadNeeds" : $("#search_uploadNeeds").val(),
				"creater" : $("#search_creater").val()
			};
			$.extend(searchReqData, requestData);
			DataTableUtil.search(tableId, scriptUrl + "/list", {
				"search" : searchReqData
			});
		},
		add : function(id) {
			function yes(index, requestData) {
				if (searchId) {// 传入后台存储
					if (projectId) {
						requestData.productId = searchId;
						requestData.projectId = projectId;
						CommonUtil
								.requestService(scriptUrl, requestData, true,
										"post", function(response) {
											if (response.success) {
												layer.close(index);
												me.searchScriptList();
												AutoScriptDetailUtil
														.init("scriptform");
											} else {
												layer.msg(response.error, {
													offset : "50px"
												});
											}
										}, function(error) {
										});
					} else {
						layer.msg("项目不明确，不允许保存，请刷新后重新创建", {
							offset : "50px"
						});
					}
				} else
					layer.msg("请选择产品", {
						offset : [ '150px' ]
					});
			}
			function cancel() {
			}
			me.openUploadForm("scriptform", yes, [ "挂接", "取消" ]);
			AutoScriptDetailUtil.createAutozTree();
		},
		del : function(ids) {
			DataTableUtil.optListForm(tableId, scriptUrl + "/" + ids, "DELETE",
					"", function() {
						me.searchScriptList();
					}, false);
		},
		edit : function(id) {
			layer.open({
				type : 2,
				title : "编辑",
				skin : '', // 加上边框
				offset : [ '50px' ],
				area : [ "960px", "460px" ], // 宽高
				content : CommonUtil.getRootPath() + scriptUrl + "/" + id
						+ "/edit?readonly=0",
				btn : [ '保存', '取消' ],
				yes : function(index, layero) {
					// var body = layer.getChildFrame('body', index);
					var iframeWin = window[layero.find('iframe')[0]['name']];
					var code_editor = iframeWin.code_editor;
					var new_code = code_editor.getValue();
					if (iframeWin.old_code != new_code) {
						var requestData = {
							"code" : new_code,
							"productId" : searchId
						};
						DataTableUtil.optListForm(tableId,
								scriptUrl + "/" + id, "PUT", requestData,
								function() {
									layer.close(index);
									me.searchScriptList();
								}, false);
					} else
						layer.close(index);

				}
			});
		},
		view : function(id) {
			layer.open({
				type : 2,
				title : "查看",
				skin : '', // 加上边框
				offset : [ '50px' ],
				area : [ "930px", "460px" ], // 宽高
				content : CommonUtil.getRootPath() + scriptUrl + "/" + id
						+ "/edit?readonly=1"
			});
		},
		rollback : function(id, row) {
			layer.open({
				type : 1,
				title : "回滚",
				skin : '', // 加上边框
				area : [ "830px", "460px" ], // 宽高
				offset : [ '50px' ],
				content : $("#annalsform")
			});
			nowAttId = row.attId;
			var requestData = {
				"scriptId" : id,
				"attId" : nowAttId
			};
			me.createAnnalsList(requestData);
		},
		createAnnalsList : function(requestData) {
			var aoColumns = [ {
				"sTitle" : "脚本名称",
				"data" : "fileName"
			}, {
				"sTitle" : "创建人",
				"data" : "creUserName"
			}, {
				"sTitle" : "修改人",
				"data" : "modUserName"
			}, {
				"sTitle" : "版本日期",
				"data" : "created_at"
			}, {
				"sTitle" : "版本",
				"data" : "version",
			}, {
				"sTitle" : "备注",
				"data" : "backMemo",
				"width" : "100px"
			} ];
			var tablekv = {
				"chk" : false,
				"iDisplayLength" : 15,
				"opt" : {
					"beginRollBack" : {
						"display" : 1,
						"info" : "回滚",
						"func" : me.beginRollBack
					},
					"backLog" : {
						"display" : 1,
						"info" : "日志",
						"func" : me.scriptVerBackLog
					}
				}
			};
			DataTableUtil.load("annalslist", scriptUrl + "/annalslist",
					aoColumns, tablekv, requestData);
		},
		beginRollBack : function(id, row) {
			var rollBackId = row.id;
			var success = 0;
			layer.open({
				type : 2,
				title : false,
				skin : '', // 加上边框
				offset : [ '10px' ],
				area : [ "900px", "520px" ], // 宽高
				content : CommonUtil.getRootPath() + scriptUrl
						+ "/scriptdiff?attId=" + rollBackId + "&nowAttId="
						+ nowAttId,
				btn : [ '确定回滚', '取消' ],
				yes : function(index, layero) {
					$("#backMemo").val("");
					layer.open({
						type : 1,
						title : "备注",
						skin : '', // 加上边框
						area : [ "530px" ], // 宽高
						offset : [ '150px' ],
						content : $("#backLogform"),
						btn : [ '确定' ],
						yes : function(cIndex, layero) {
							var requestData = {
								"attId" : rollBackId,
								"nowAttId" : nowAttId,
								"scriptId" : row.scriptId,
								"backMemo" : $("#backMemo").val()
							};
							CommonUtil.requestService(scriptUrl + "/rollback",
									requestData, false, "post", function(
											response) {
										if (response.success) {
											nowAttId = rollBackId;
											var requestData = {
												"scriptId" : row.scriptId,
												"attId" : nowAttId
											};
											me.createAnnalsList(requestData);
											me.searchScriptList();
											layer.close(cIndex);
											layer.close(index);
										}
									}, function(error) {
									});
						}
					});
				}
			});
		},
		scriptBackLog : function(id) {
			var requestData = {
				"scriptId" : id
			};
			me.backLogList(requestData);
		},
		scriptVerBackLog : function(id, row) {
			var requestData = {
				"scriptRelateId" : row.relateId,
				"scriptId" : row.scriptId
			};
			me.backLogList(requestData);
		},
		backLogList : function(requestData) {
			var loglist = "backLoglist";
			var aoColumns = [ {
				"sTitle" : "备注",
				"data" : "backMemo",
				"width" : "100px"
			}, {
				"sTitle" : "回滚日期",
				"data" : "created_at",
				"width" : "80px"
			} ];
			var tablekv = {
				"chk" : false,
				"iDisplayLength" : 10
			};
			layer.open({
				type : 1,
				title : "回滚日志",
				skin : '', // 加上边框
				area : [ "830px", "510px" ], // 宽高
				offset : [ '20px' ],
				content : $("#backLogListform")
			});
			DataTableUtil.load(loglist, scriptUrl + "/backloglist", aoColumns,
					tablekv, requestData);
		},
		uploadParams : function(id) {
			function yes(index, requestData) {
				requestData.scriptId = id;
				CommonUtil.requestService(scriptUrl + "/params", requestData,
						true, "post", function(response) {
							layer.close(index);
							me.searchScriptList();
							AutoScriptDetailUtil.init("scriptParam");
						}, function(error) {
						});
			}
			me.openUploadForm("scriptParam", yes);
		},
		uploadImages : function(id) {
			function yes(index, requestData) {
				requestData.scriptId = id;
				CommonUtil.requestService(scriptUrl + "/images", requestData,
						true, "post", function(response) {
							layer.close(index);
							me.searchScriptList();
							AutoScriptDetailUtil.init("scriptImage");
						}, function(error) {
						});
			}
			me.openUploadForm("scriptImage", yes);
		},
		openUploadForm : function(optType, yes, btn) {
			AutoScriptDetailUtil.init(optType);
			var formCss = "";
			switch (optType) {
			case "scriptParam":
				formCss = {
					"display" : "none"
				};
				break;
			case "scriptImage":
				formCss = {
					"display" : "none"
				};
				break;
			default:
				formCss = {
					"display" : ""
				};
				break;
			}
			$("#scriptInfo").css(formCss);
			if (!btn)
				btn = [ '保存', '取消' ];
			layer.open({
				type : 1,
				title : "上传",
				skin : '', // 加上边框
				area : [ "830px", "460px" ], // 宽高
				offset : [ '50px' ],
				content : $("#scriptform"),
				btn : btn,
				yes : function(index, layero) {
					if (uploaderInfos.length > 0) {
						var requestData = {
							"scriptFiles" : uploaderInfos
						};
						yes(index, requestData);
					} else
						layer.msg("请选择上传文件", {
							offset : [ '150px' ]
						});
				},
				cancel : function(index, layero) {
					layer.close(index);
				}
			});
		}
	};
}();
var searchId, projectId;
AutoScriptDetailUtil = function(me) {
	var proTreeId = "productTree";
	var prozTree, proId = "product";
	var isShow = false, searchList = [];
	return me = {
		init : function(optType) {
			me.initUploader(optType);
			// me.createAutozTree();
		},
		initUploader : function(optType, $action) {
			CommonUtil.ajaxLoad("scriptUploader", scriptUrl
					+ "/uploader?index=1&uploaderServer=" + scriptUrl
					+ "/uploader&optType=" + optType + "&action=uploadfile");
			$("#" + proId).off();
			$("#" + proId).on("propertychange", me.searchNode).on("input",
					me.searchNode).on("focus", me.focusKey);
		},
		createAutozTree : function() {
			var oriWidth = $(".input-group").width();
			$("#" + proTreeId).width(oriWidth - 33);
			$(".dropdown-menu").width(oriWidth);
			$(".dropdown-menu").css("overflow", "auto");
			var setting = {
				view : {
					selectedMulti : false,
					fontCss : me.getFontCss
				},
				check : {
					enable : true,
					chkStyle : "radio",
					radioType : "all"// 整个数单选
				},
				data : {
					simpleData : {
						enable : true
					}
				},
				callback : {
					onClick : me.onClick,
					beforeCheck : me.beforeCheck,
					onCheck : me.onCheck
				}
			};
			CommonUtil.requestService(proTreeUrl, "", true, "get", function(
					zNodes) {
				$.fn.zTree.init($("#" + proTreeId), setting, zNodes);
				prozTree = $.fn.zTree.getZTreeObj(proTreeId);
				$("#productSelect").off("click");
				$("#productSelect").on("click", function() {
					$(".dropdown-menu").toggle();
				});
				$(".dropdown-menu").on("mouseleave", me.zTreeMouseLeave);
			}, function(error) {
			});
		},
		getFontCss : function(treeId, treeNode) {
			return (!!treeNode.highlight) ? {
				color : "#A60000",
				"font-weight" : "bold"
			} : {
				color : "#333",
				"font-weight" : "normal"
			};
		},
		getTopNodeId : function(treeNode) {
			var node = treeNode.getParentNode();
			if (node) {
				return me.getTopNodeId(node);
			} else
				return treeNode.id;
		},
		onClick : function(event, tId, tNode) {
			if (tNode.check_Child_State < 0) {
				var tn = tNode.getParentNode();
				if (tn) {
					projectId = me.getTopNodeId(tn);
					prozTree.checkNode(tNode, false, null, false);
					searchId = tNode.id;
					$("#" + proId).val(tNode.name);
					isShow = true;
					$(".dropdown-menu").toggle();
				}
			}
		},
		onCheck : function(event, tId, tNode) {
			me.onClick(event, tId, tNode);
		},
		zTreeMouseLeave : function() {
			/*
			 * if (isShow && searchId) { isShow = false;
			 * $(".dropdown-menu").hide(); }
			 */
		},
		focusKey : function() {
			/* $(".dropdown-menu").show(); */
		},
		searchNode : function() {
			me.updateNode(false);
			searchVal = $("#" + proId).val();
			if (searchVal === "")
				return;
			searchList = prozTree.getNodesByParamFuzzy("name", searchVal);
			me.updateNode(true);
		},
		updateNode : function(highlight) {
			for ( var i = 0, l = searchList.length; i < l; i++) {
				searchList[i].highlight = highlight;
				prozTree.updateNode(searchList[i]);
			}
		}
	};
}();
