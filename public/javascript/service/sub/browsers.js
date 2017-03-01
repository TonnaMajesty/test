BrowserChecksUtil = function(me) {
	var browserUrl = "/auto/browser";
	var selBrowsers = [];
	return me = {
		initOwn : function() {
		},
		init : function() {
			me.createBrowserCheck();
		},
		createBrowserCheck : function() {
			CommonUtil.requestService(browserUrl, "", true, "get", function(
					response, status) {
				if (response.success) {
					var browsers = response.data;
					for ( var browser in browsers) {
						$("#browserChecks").append(
								"<label class='checkbox-inline i-checks'> <input type='checkbox' value='"
										+ browsers[browser].id + "'>"
										+ browsers[browser].browserName
										+ "</label>&nbsp;&nbsp;");
					}
					$('.i-checks').iCheck({
						checkboxClass : 'icheckbox_square-green',
						radioClass : 'iradio_square-green'
					});
				}
			}, function(ex) {
			});
			$("#browserChecks").on("ifChecked ifUnchecked",
					"input[type='checkbox']", function(event) {
						var val = $(this).val();
						switch (event.type) {
						case "ifChecked":// 选中
							if ($.inArray(val, selBrowsers) < 0)
								selBrowsers.push(val);
							break;
						case "ifUnchecked":// 取消选中
							selBrowsers.splice($.inArray(val, selBrowsers), 1);
							break;
						}
					});
		},
		getSelBrowsers : function() {
			return selBrowsers;
		},
		reset : function() {
			selBrowsers = [];
			$("#browserChecks input").iCheck("uncheck");
		}
	};
}();
