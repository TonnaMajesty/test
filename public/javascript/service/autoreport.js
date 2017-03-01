AutoReportUtil = function(me) {
	var reportUrl = "/report/bill";
	var oldClass = "";
	return me = {
		initOwn : function() {
		},
		init : function() {
			me.initOwn();
			me.reportLoad();
			me.bindEvent();
		},
		reportLoad : function() {
			var requestData = {
				"taskType" : $("#taskType").val()
			};
			CommonUtil.requestService(reportUrl + "/" + $("#keyId").val()
					+ "/edit", requestData, true, "get", function(response,
					status) {
				if (response.success) {
					me.reportLog(response.data);
				}
			}, function(ex) {
			});
		},
		bindEvent : function() {
			$(".popup-content .tab li").click(function() {
				$(this).addClass("cur").siblings().removeClass("cur")
			})
			$(".popup-content .step .tabs li").click(function() {
				$(this).addClass("cur").siblings().removeClass("cur");
				$(this).addClass("cur").siblings().each(function() {
					var tab = $(this).attr("href");
					$(tab).css("display", "none");
				});
				var tab = $(this).attr("href");
				$(tab).css("display", "");
			})
			$("#carousel_item").on("click", ".mignifier", function() {
				me.openImgLayer($(this));
			});
		},
		openImgLayer : function(obj) {
			var imgObj = new Image();
			imgObj.src = src = obj.attr("src");
			var windowWidth = $(window).width();
			var windowHeight = $(window).height();
			var w;
			var h;
			if (imgObj.width < windowWidth)
				w = imgObj.width;
			else
				w = windowWidth;
			if (imgObj.height < windowHeight)
				h = imgObj.height;
			else
				h = windowHeight;
			me.autoResizeImage(w, h, imgObj);
			var imgHtml = "<div><img width=" + imgObj.width + "px height="
					+ imgObj.height + "px src=" + src + " /></div>";
			parent.layer.open({
				type : 1,
				title : false,
				maxmin : false,
				shadeClose : true, // 点击遮罩关闭层
				area : [ imgObj.width, imgObj.height ],
				content : imgHtml
			});
		},
		autoResizeImage : function(maxWidth, maxHeight, objImg) {
			var hRatio;
			var wRatio;
			var Ratio = 1;
			var w = objImg.width;
			var h = objImg.height;
			wRatio = maxWidth / w;
			hRatio = maxHeight / h;
			if (maxWidth == 0 && maxHeight == 0) {
				Ratio = 1;
			} else if (maxWidth == 0) {// if (hRatio < 1) Ratio =
				hRatio;
			} else if (maxHeight == 0) {
				if (wRatio < 1)
					Ratio = wRatio;
			} else if (wRatio < 1 || hRatio < 1) {
				Ratio = (wRatio <= hRatio ? wRatio : hRatio);
			}
			if (Ratio < 1) {
				w = w * Ratio;
				h = h * Ratio;
			}
			objImg.height = h;
			objImg.width = w;
		},
		reportLog : function(logs) {
			var fails = [ "ERROR" ];
			var browserName = "", browserHtml = "", errorBrowserHtml = "", scriptName = "", scriptHtml, errorScirptHtml;
			for ( var idx in logs) {
				var log = logs[idx];
				if (log.scriptName
						&& (!scriptName || scriptName != log.scriptName)) {
					scriptName = log.scriptName;
					errorScirptHtml = scriptHtml = "<li class='o' style='color:#32b5cb;'><span></span>脚本："
							+ scriptName + "</li>";
				} else
					scriptHtml = "";
				var stepItem = parseInt(idx) + 1;
				if ($.inArray(log.chrResult, fails) >= 0) {
					$("#step_fail").append(
							errorBrowserHtml + errorScirptHtml
									+ "<li class='xx' stepItem='" + stepItem
									+ "'><span></span>步骤" + log.intOrderNo
									+ "：" + log.chrDescription + "</li>");
					errorScirptHtml = "";
					errorBrowserHtml = "";
				}
				if (idx == 0)
					continue;
				if (log.browserName
						&& (!browserName || browserName != log.browserName)) {
					browserName = log.browserName;
					errorBrowserHtml = browserHtml = "<li class='o' style='color:#1ab394;'><span></span>浏览器："
							+ browserName + "</li>";
				} else
					browserHtml = "";
				if ($.inArray(log.chrResult, fails) >= 0) {
					$("#step_all").append(
							browserHtml + scriptHtml
									+ "<li class='xx' stepItem='" + stepItem
									+ "'><span></span>步骤" + log.intOrderNo
									+ "：" + log.chrDescription + "</li>");
				} else
					$("#step_all").append(
							browserHtml + scriptHtml + "<li stepItem='"
									+ stepItem + "'><span></span>步骤"
									+ log.intOrderNo + "：" + log.chrDescription
									+ "</li>");
			}
			$("#prev").on("click", function() {
				var index = $("#carousel_item").attr("stepItem");
				if (index == 1)
					return;
				else
					index--;
				me.reportChangeStep(index, logs);
			});
			$("#next").on("click", function() {
				var index = $("#carousel_item").attr("stepItem");
				if (index == logs.length)
					return;
				else
					index++;
				me.reportChangeStep(index, logs);
			});
			$("#tab-step").on("click", "li", function() {
				var index = $(this).attr("stepItem");
				me.reportChangeStep(index, logs);
			})
		},
		reportChangeStep : function(index, logs) {
			var log = logs[index - 1];
			// $("[stepItem]:not(span)").attr("stepItem", index);
			$("#carousel_item").attr("stepItem", index);
			$("#carousel_item img").attr("src", log.chrImage);
			$("li[stepItem]").removeClass("focus");
			$("#step_fail li[stepItem='" + index + "']").addClass("focus");
			// $("#step_fail div[stepItem='" + index + "']").scrollTop = 100;
			var step = $("#step_all li[stepItem='" + index + "']");
			step.addClass("focus");
			var scroll_pane = $(".detail");
			scroll_pane.scrollTop(step.height() * index - 10);
			$("#stepDetail").empty();
			$("#stepDetail").append(
					"<div class='explain clearfix'><h6>执行命令</h6><p>"
							+ log.chrDescription + "【" + log.chrCmd
							+ "】</p></div>"
							+ "<div class='explain clearfix'><h6>耗时</h6><p>"
							+ log.fltDuring + "</p></div>"
							+ "<div class='explain clearfix'><h6>参数</h6><p>"
							+ log.chrCmdParam + "</p></div>"
							+ "<div class='explain clearfix'><h6>错误详情</h6><p>"
							+ log.chrErrorMessage + "</p></div>");
		}
	};
}();
