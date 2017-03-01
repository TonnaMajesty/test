var imgpath = "../";
var thisPage = 1;// 初始化当前页面
var count = 0;

var DATA;// 菜单数据

var leftMenu;// 左菜单数组 leftMenu变量要与sApp一致
// sApp的菜单应用数量可以大于leftMenu中的类别，如此leftMenu中的部分将不会显示

// ops变量要与app一致 app的菜单应用数量可以大于ops中的类别，如此app中的部分将不会显示
// 将桌面菜单分类划到某种类别下
var ops;// 桌面菜单数组
var themes;// 所有主题json
var osStyle;// 所有系统样式json
var deskTheme; // 用户桌面主题
var deskStyle;// 用户桌面萌样式

ContMenuData = function() {
	var menuJson = $("#menujson").val();
	var jsonObj = ParseToJson(menuJson);
	DATA = jsonObj.DATA;
	ops = jsonObj.ops;// ParseToJson(opsMenuJson);// 向桌面添加应用
	leftMenu = new Array(jsonObj.leftMenu);
	themes = jsonObj.themes;
	osStyle = jsonObj.osStyle;
	deskTheme = '../' + jsonObj.userDesk.displaybgpath;
	deskStyle = '../' + jsonObj.userDesk.themepath;

};

// 面板类
Panel = function() {
	return me = {
		hitTest : function(panel, x, y) {// 碰撞检测，检测坐标[x,y]是否落在panel里面
			var pl, pt;
			return !(x < (pl = panel.offset().left)
					|| y < (pt = panel.offset().top) || x > pl + panel.width() || y > pt
					+ panel.height());
		},
		getIdx : function(panel) {// 获取节点在panel是第几个儿子节点
			var ci = 0;
			while (panel = panel.prev()) {
				ci++;
			}
			return ci;
		},
		unSelecte : function() {// 清除选中
			return window.getSelection ? function() {
				window.getSelection().removeAllRanges();
			} : function() {
				document.selection.empty();
			};
		}()
	};
};

// BODY
Body = function(me) {
	return me = {
		init : function() {
			me.create();
			me.bindEvent();
		},
		create : function() {
			me.box = $('body');
			me.setStyle();
		},
		bindEvent : function() {// 清除选中
			function move(evt) {
				window.getSelection ? window.getSelection().removeAllRanges()
						: document.selection.empty();
			}
			function up(evt) {
				$(document).unbind('mousemove', move).unbind('mouseup', up);
			}
			$(document).bind('mousedown', function() {
				$(document).bind('mousemove', move).bind('mouseup', up);
			});
		},
		addPanel : function(panel) {
			me.box.append(panel);
		},
		setStyle : function() {
			me.box.css({
				backgroud : "none repeat scroll 0 0 transparent",
				display : "block",
				height : "500px"
			});

		}

	};
};
var themeSet = false;
var styleSet = false;
var removeMenu = false;
// 创建桌面最外层类
Desktop = function(me) {

	return me = {
		init : function() {
			me.create();
			me.setMenu();// 绑定右键
			return me;
		},
		create : function() {
			me.box = $("<div id='desktop' style='position: static;'></div>");
			bodyObj.addPanel(me.box);
		},
		addPanel : function(panel) {
			me.box.append(panel);
		},
		show : function() {
			me.box.show();
		},
		hide : function() {
			me.box.hide();
		},
		MenuData : function() {
			var MenuData;
			var menuopreate = [ {
				text : "显示桌面",
				func : function() {
					windowsObj.showWindowDesk();
				}
			}, {
				text : "关闭所有",
				func : function() {
					windowsObj.closeAllWindow();
				}
			} ], menutheme = [
					{
						text : "样式设置",
						func : function() {
							windowsObj.openSys({
								id : 'Setting',
								title : '样式设置',
								width : 650,
								height : 500,
								content : document
										.getElementById("styleSetting_wrap")
							});
						}
					},
					{
						text : "主题设置",
						func : function() {
							windowsObj.openSys({
								id : 'themSetting',
								title : '主题设置',
								width : 650,
								height : 500,
								content : document
										.getElementById("themeSetting_wrap")
							});
						}
					},
					{
						text : "图标设置",
						data : [ [
								{
									text : "大图标",
									func : function() {
										Deskpanel.desktopsContainer
												.removeClass("desktopSmallIcon");
									}
								},
								{
									text : "小图标",
									func : function() {
										Deskpanel.desktopsContainer
												.addClass("desktopSmallIcon");
									}
								} ] ]
					} ];

			var menuadd = {
				text : "添加菜单",
				func : function() {
					var url = getRootPath() + "/WebDesktop/AddMenu.html";
					Sys_OpenPage(url, '添加菜单', 800, 550);
				}
			}, menuremove = {
				text : "移除菜单",
				func : function() {
					// 删除
					$(".appButton_delete").each(function() {
						$(this).css("display", "block");
					})
					removeMenu = true;
					me.setMenu();
				}
			}, overremove = {
				text : "完成移除",
				func : function() {
					// 删除
					$(".appButton_delete").each(function() {
						$(this).css("display", "");
					})
					removeMenu = false;
					me.setMenu();
				}
			};
			var menulogout = [ {
				text : "注销",
				func : function() {
					alert('退出系统事件')
				}
			} ];
			if (!removeMenu) {
				// 动态数据，及时清除
				$.smartMenu.remove();
				MenuData = [ menuopreate, menutheme, [ menuadd, menuremove ],
						menulogout ];
			} else {
				// 动态数据，及时清除
				$.smartMenu.remove();
				MenuData = [ menuopreate, menutheme, [ menuadd, overremove ],
						menulogout ];
			}
			return MenuData;
		},
		setMenu : function() {
			var MenuData = me.MenuData();
			me.box.smartMenu(MenuData, {
				name : "image"
			});
		},
		updateMenu : function() {
			$(".smart_menu_a")[8].outerHTML = "<A class=smart_menu_a href=\"javascript:\" data-key=\"009334846723134316\" jQuery18207432287454710038=\"120\">完成移除</A>"
		}
	};
};

// 桌面内部面板
Deskpanel = function(me) {
	var desktopWrapper = "<div id='desktopWrapper'></div>";// 最外层容器
	var desktopsContainer = "<div id='desktopsContainer' class='desktopsContainer'	>";
	var desktopContainer = "<div class='desktopContainer' index='{index}' >";
	var desktopAppListener = "<div id='desktopPanel' class='appListContainer' customacceptdrop='{index}' index='{index}' _olddisplay='block' >";// 内部监听容器
	var defaultIndex = 0, defaultNum = DATA.menu.length, defautlSpace = {// 默认尺寸
		left : 0,
		top : 0,
		right : 0,
		bottom : 120
	}

	return me = {
		init : function(ops) {
			me.create();
			me.addIcons(ops);
			me.space(defautlSpace);
			me.refresh();
			me.bindEvent();
			me.addCurrnet(defaultIndex);
			return me;
		},
		reLoad : function() {
			GetMenuData();
			$("#desktopWrapper").remove();
			me.init(ops).refresh();
			Navbar.bindSwitchDesktopAnimate(thisPage, 1);
			arrowsObj.changeStyle(thisPage, 1);
		},
		create : function() {
			me.box = $(desktopWrapper);// 桌面外层面板
			me.desktopsContainer = $(desktopsContainer);
			me.createDesktopsContainer(defaultNum); // 创建桌面外层容器
			me.box.append(me.desktopsContainer);
			me.box.css({
				"left" : "73px",
				"right" : "0px",
				"top" : "0px"
			});
			me.desktopsContainer.css({
				"left" : 73
			});
			desktopObj.addPanel(me.box);
			me.Icon = [];
		},
		bindEvent : function() {

			// 桌面图标拖拽
			me.desktopsContainer.find(".appListContainer").each(function() {
				var desk = $(this);
				var index = desk.attr("index");
				desk.sortable({
					items : ".appButton",
					connectWith : ".dock_middle",
					opacity : "0.6",
					containment : 'parent',// 只允许在父窗体中拖拽
					start : function(event, ui) {

					},
					stop : function(event, ui) { // 拖拽动作停止事件

						var p = ui.item.parent();
						if (p.hasClass("dock_middle"))
							ui.item.removeAttr("style");// 落在侧边栏
						Deskpanel.switchCurrent(index);
						Deskpanel.refreshIcon();
					}
				}).disableSelection();
			});
			// 浏览器改变大小时 调用刷新方法重新绘制菜单布局
			$(window).resize(me.refresh);
		},
		createDesktopsContainer : function(n) {// 桌面外层容器 n创建几层桌面
			if (n && n != 0) {
				for ( var i = 1; i <= n; i++) {
					me.desktopsContainer.append(me.addContainer(i))// 填充容器
				}
			}
		},
		addContainer : function(i) { // 添加容器
			var c = me.createDesktopContainer(i);
			var a = me.createDesktopAppListener(i);
			c.append(a);
			return c;
		},
		createDesktopContainer : function(n) { // 容器项
			return $(Util.formatmodel(desktopContainer, {
				"index" : n - 1
			}));
		},
		createDesktopAppListener : function(n) {// 容器监听项
			return $(Util.formatmodel(desktopAppListener, {
				"index" : n - 1
			}));
		},
		addIcons : function(ops) {// 添加应用
			for ( var i in ops) {
				var key = i.replace("Icon", "");
				me.addIcon(ops[i], key);
			}
		},
		addIcon : function(icon, idx) {// 添加应用 idx 第几桌面
			if (icon) {
				if ($.isArray(icon)) {// 传入是数组
					$.each(icon, function() {
						me.addIcon(this.valueOf(), idx);// 添加应用程序
					});
					return me;
				}
				var Icon = typeof icon == 'string' ? appIcon_t1(icon) : icon;// 传入的是ID还是图标对象
				me.Icon.push(Icon);
				me.box
						.find(
								"div[customacceptdrop='" + parseInt(idx - 1)
										+ "']").append(Icon.box);
			}
		},
		addCurrnet : function(n) {// 根据index设置当前桌面样式
			me.desktopsContainer.find(".desktopContainer[index='" + n + "']")
					.addClass("desktop_current");
		},
		removeCurrent : function(n) {// 根据index移除当前桌面样式
			me.desktopsContainer.find(".desktopContainer[index='" + n + "']")
					.removeClass("desktop_current");
		},
		switchCurrent : function(n) {// 切换index桌面样式
			var dc = me.desktopsContainer;
			dc.find(".desktopContainer[index='" + n + "']").addClass(
					"desktop_current").siblings()
					.removeClass("desktop_current");
		},
		space : function(ops) {// 设置桌面各面板尺寸位置
			('top' in ops)
					&& (typeof ops.top == 'string' ? me.spaceTop += ops.top
							: me.spaceTop = +ops.top || 0);
			('left' in ops)
					&& (typeof ops.left == 'string' ? me.spaceLeft += ops.top
							: me.spaceLeft = +ops.left || 0);
			('right' in ops)
					&& (typeof ops.right == 'string' ? me.spaceRight += ops.top
							: me.spaceRight = +ops.right || 0);
			('bottom' in ops)
					&& (typeof ops.bottom == 'string' ? me.spaceBottom += ops.top
							: me.spaceBottom = +ops.bottom || 0);
			return me;
		},
		refresh : function() {// 刷新桌面

			var ww = $(window).width(), // 浏览器宽
			wh = $(window).height();// 浏览器高
			me.width = ww - me.spaceRight - me.spaceLeft;// 容器宽
			me.height = wh - me.spaceTop - me.spaceBottom;// 容器高
			var desktopContainer = me.desktopsContainer
					.find(".desktopContainer");
			var appContainer = desktopContainer.find(".appListContainer");

			$(desktopContainer).each(function(i) {// 容器宽高
				$(this).css({
					left : me.width * i,
					height : me.height - me.spaceBottom
				});
			})
			var a = ""
			$("#zoomWallpaperGrid,#zoomWallpaper").width(ww).height(wh);// 背景图片div

			var r = me.row = ~~(me.height / 112);// 行数

			me.desktopsContainer.css({// 设置应用容器样式和位置
				left : me.spaceLeft,
				top : me.spaceTop,
				width : me.width,
				height : me.height
			});

			appContainer.each(function() {
				$(this).css({
					width : me.width,
					height : me.height,
					"margin-left" : 28,
					"margin-top" : 6,
					display : "block"
				});
			});
			me.refreshIcon();
		},
		refreshIcon : function() {// 刷新应用

			var r = ~~(me.height / 112); // 0.111 取0 1.3 取1
			me.desktopsContainer.find(".appListContainer").each(function() {

				var icon = $(this).children();
				for ( var j = 0; j < icon.length; j++) {
					var leftI = ~~(j / r), topI = j % r;
					$(icon[j]).css({
						left : leftI * 142,
						top : topI * 112
					});
				}
				;
			});

		},
		moveIconTo : function(icon, idx2) {// 目标位置
			var ids = (Panel.getIdx(icon.box));
			if (idx > idx2) {// 往前移
				me.box.children(".appListContainer[index='1']").append(
						icon.box, idx2);
			} else if (idx < idx2) {// 往后移
				me.box.children(".appListContainer[index='1']").append(
						icon.box, idx2 + 1);
			}
			me.Icon.splice(idx, 1);
			me.Icon.splice(idx2, 0, icon);
			me.refresh();

		},
		removeIcon : function(icon) {
			var idx = (Panel.getIdx(icon.box));
			me.Icon.splice(idx, 1);
			icon.box.remove();
			me.refresh();
		},
		getIdx : function(ex, ey) {
			ex -= me.spaceLeft + me.spaceRight;
			ey -= me.spaceTop + me.spaceBottom;
			return (~~(ex / 142)) * me.row + (~~(ey / 112));
		}
	};

};

var themeList = new Array();// 主题数组，用于回传更新用户桌面信息 0 主题图片ID 1 主题样式ID
// 侧边栏
Sidebar = function(me) {
	var tool_list = "<div class='dock_tool_list' id='dockToolList' >";
	var tool_item = "<div class='dock_tool_item'></div>";
	var tool_a = "<a title='{title}' cmd='{cmd}'	class='dock_tool_icon dock_tool_{key}' href='javascript:void(0)'></a>";

	// 装载容器类
	var SideBox = $.Class({
		init : function(ops) {
			this.create(ops.location);
		},
		create : function(location) {
			this.box = $("<div id='" + location + "Bar'></div>");
			desktopObj.addPanel(this.box);
		},
		addPanel : function(sidebar) {
			this.box.append(sidebar.pbox);
		}
	});
	return me = {
		init : function(ops) {
			me.create(ops.location);
			me.addIcon(ops.Icon);
			me.addToolList();
			me.initDrag();

		},
		create : function(location) {// 创建
			// 创建上左右 侧边栏容器
			me.leftPanel = SideBox({
				location : 'left'
			});
			me.rightPanel = SideBox({
				location : 'right'
			});
			me.topPanel = SideBox({
				location : 'top'
			});

			me.box = $('<div class="dock_middle"></div>');
			me.pbox = $('<div id="dockContainer" class="dock_container " style="z-index: 10;"> </div>');
			// 创建父边栏容器
			me[location + 'Panel'].addPanel(me.pbox);
			me.location = location;
			me.Icon = [];
			me.pbox.addClass("dock_pos_" + location);
			me.pbox.append(me.box);
			me.leftPanel.box.append(me.pbox);
			desktopObj.addPanel(me.leftPanel.box);
			desktopObj.addPanel(me.rightPanel.box);
			desktopObj.addPanel(me.topPanel.box);
			me.createStartTool();
			me.createPinyinTool();
			me.createSoundTool();
			me.createSettingTool();
			me.createThemeTool();
		},
		addToolList : function() {// 添加工具栏
			var docklist = $(tool_list);
			var dockItem = $(tool_item);
			var dockItem2 = $(tool_item);
			var dockItem3 = $(tool_item);
			dockItem.append(me.email).append(me.sound);
			dockItem2.append(me.settingtool).append(me.theme);
			dockItem3.append(me.start);
			docklist.append(dockItem).append(dockItem2).append(dockItem3);
			me.box.append(docklist);
		},
		createStartTool : function() {// 开始设置
			me.start = $("<span title='点击这里开始' class='dock_tool_icon dock_tool_start'></span>");
			me.powerFloat(me.start);// 解决第一次不弹出浮动窗体
			me.start.mouseenter(function() {
				var _this = $(this);
				me.powerFloat(_this);
			})
		},
		powerFloat : function(_this) {
			var position = "";
			var offsets = {};
			var p = me.pbox.parent();
			var pid = p.attr("id");
			var key = pid.substring(0, pid.length - 3);
			if (key == "left") {
				position = "3-4";
				offsets = {
					x : 20,
					y : 5
				};
			} else if (key == "top") {
				position = "3-2";
				offsets = {
					x : 10,
					y : 20
				};
			} else {
				position = "4-3";
				offsets = {
					x : 25,
					y : 2
				};
			}
			_this.powerFloat({
				width : 185,
				eventType : "hover",// 事件类型，一般而言，此参数无非这几个：”hover”(默认), “click”,
				// “focus”以及null，其中”hover”表示鼠标悬停和移出事件，”click”表示点击事件，”focus”表示获得焦点事件，适用于表单元素，null表示无事件，也就是trigger绑定了powerFloat方法即触发，此参数在点击A元素，但是让B元素上显示提示上很有用
				offsets : offsets,
				position : position,
				target : $("#startMenuContainer"),
				showCall : function() {
				}
			});
		},
		createPinyinTool : function() { // 邮件（后续直接连接系统用户的邮件）
			me.email = $(Util.formatmodel(tool_a, {
				"cmd" : "Email",
				"title" : "邮件",
				"key" : "pinyin"
			}));
		},
		createSoundTool : function() {// 声音设置 （后续提醒）
			var sound = me.sound = $(Util.formatmodel(tool_a, {
				"cmd" : "Sound",
				"title" : "静音",
				"key" : "sound"
			}));
			sound.toggle(function() {
				$(this).addClass("dock_tool_sound_mute").attr("title", "取消静音");

			}, function() {
				$(this).removeClass("dock_tool_sound_mute")
						.attr("titile", "静音");
			});
		},
		createSettingTool : function() {// 样式设置
			me.settingtool = $(Util.formatmodel(tool_a, {
				"cmd" : "Setting",
				"title" : "样式设置",
				"key" : "setting"
			}));
			me.styleInit();
			me.bindStyle();
		},
		styleInit : function() { // 样式设置初始化（拼写系统样式html）
			var len = osStyle.length;
			var html = $("<div id=\"styleSetting_area\" class=\"themeSetting_area\" style=\"display: block;\"></div>");
			$("#styleSetting_body").html(''); // 清空themeSetting_body下的内容
			$("#styleSetting_body").append(html);
			for (itheme = 0; itheme < len; itheme++) {
				bg = "../" + osStyle[itheme].smallBg;
				html = "<a href=\"###\" theme=\"1\" xID=\""
						+ osStyle[itheme].id
						+ "\" isShare=\""
						+ osStyle[itheme].isShare
						+ "\" creater=\""
						+ osStyle[itheme].creater
						+ "\" themeid=\""
						+ osStyle[itheme].themeid
						+ "\" class=\"styleSetting_settingButton\" id=\"themeSetting_"
						+ osStyle[itheme].themeid
						+ "\" styleID=\""
						+ osStyle[itheme].styleID
						+ "\">"
						+ "<div style=\"background: url("
						+ bg
						+ ") no-repeat;\" class=\"styleSetting_settingButton_icon\"></div>"
						+ "<div class=\"themeSetting_settingButton_text\">"
						+ osStyle[itheme].imgName + "</div></a>"
				$("#styleSetting_area").append(html);
			}
			$("#styleSetting_body")
					.append(
							"<div id=\"styleSetting_wallpaper\" class=\"themeSetting_wallpaper\" style=\"display: none;\"></div>");
		},
		bindStyle : function() {
			var styleSetting = $("#styleSetting_wrap");
			me.settingtool.click(function() {

				windowsObj.openSys({
					id : 'Setting',
					title : '样式设置',
					width : 650,
					height : 500,
					content : document.getElementById("styleSetting_wrap")
				});
			});
			$("a", styleSetting).click(
					function() {
						styleSet = true;
						var a = $(this);
						var themeid = a.attr("themeid");
						var src = themeid;// themeid.substring(themeid.indexOf("_")
						// + 1, themeid.length);
						var h = $(window).height();
						var w = $(window).width();
						var stylePath = ("../public/desktopskin/css/skins/"
								+ themeid + ".css");
						IncludeLinkStyle(stylePath);
						var themeType = a.attr("theme");
						if (themeType == 1) {
							themeList[1] = a.attr("styleID");
						}
					});
		},
		createThemeTool : function() {// 主题设置
			var theme = me.theme = $(Util.formatmodel(tool_a, {
				"cmd" : "Theme",
				"title" : "主题设置",
				"key" : "theme"
			}));
			me.themeInit();
			me.bindTheme();
		},
		themeInit : function() { // 主题初始化（拼写主题html）
			var len = themes.length;
			var html = $("<div id=\"themeSetting_area\" class=\"themeSetting_area\" style=\"display: block;\"></div>");
			$("#themeSetting_body").html(''); // 清空themeSetting_body下的内容
			$("#themeSetting_body").append(html);
			for (itheme = 0; itheme < len; itheme++) {
				bg = "../" + themes[itheme].smallBg;
				html = "<a href=\"###\" theme=\"0\" xID=\""
						+ themes[itheme].id
						+ "\" isShare=\""
						+ themes[itheme].isShare
						+ "\" creater=\""
						+ themes[itheme].creater
						+ "\" themeid=\""
						+ themes[itheme].themeid
						+ "\" class=\"themeSetting_settingButton\" id=\"themeSetting_"
						+ themes[itheme].themeid
						+ "\">"
						+ "<div style=\"background: url("
						+ bg
						+ ") no-repeat;\" class=\"themeSetting_settingButton_icon\"></div>"
						+ "<div class=\"themeSetting_settingButton_text\">"
						+ themes[itheme].imgName + "</div></a>"
				$("#themeSetting_area").append(html);
			}
			$("#themeSetting_body")
					.append(
							"<div id=\"themeSetting_wallpaper\" class=\"themeSetting_wallpaper\" style=\"display: none;\"></div>");
		},
		bindTheme : function() {
			var themsSetting = $("#themeSetting_wrap");
			me.theme.click(function() {

				windowsObj.openSys({
					id : 'themSetting',
					title : '主题设置',
					width : 650,
					height : 500,
					content : document.getElementById("themeSetting_wrap")
				});
			});
			$("a", themsSetting).click(
					function() {
						themeSet = true;
						var a = $(this);
						var themeid = a.attr("themeid");
						var src = themeid;// themeid.substring(themeid.indexOf("_")
						// + 1, themeid.length);
						var h = $(window).height();
						var w = $(window).width();
						$("#zoomWallpaper").attr(
								"src",
								"../public/desktopskin/images/bg/" + src
										+ ".jpg").width(w).height(h);
						$("#zoomWallpaperGrid").width(w).height(h);
						$("a", themsSetting).removeClass(
								"themeSetting_selected");
						a.addClass("themeSetting_selected");
						var themeType = a.attr("theme");
						if (themeType == 0) {
							themeList[0] = a.attr("xID");
						}
					});

		},
		addIcon : function(icon, idx) {
			if (icon) {
				if ($.isArray(icon)) {// 传入的是数组
					$.each(icon, function() {
						me.addIcon(this.valueOf());
					});
					return me;
				}
				if (me.Icon.length == 6) {
					var last = me.Icon[5];
					me.Icon.length = 6;
					$(last.box).remove();
					return;
				}

				var Icon = typeof icon == 'string' ? appIcon_t2(icon) : icon;// 传入的是程序的fid还是Icon对象
				if (idx != undefined) {
					me.Icon.splice(idx, 0, Icon);
					me.box.append(Icon.box, idx);
				} else {
					me.Icon.push(Icon);
					me.box.append(Icon.box);
				}

			}
		},
		removeIcon : function(icon) {
			var idx = (Panel.getIdx(icon.box));
			me.Icon.splice(idx, 1);
			$(icon.box).remove();
		},
		getIdx : function(ex, ey) {// 获得位置
			var off = me.pbox.offset();
			switch (me.location) {
			case 'top':
				return ~~((ex - off.left) / 142);
			case 'left':
			case 'right':
				return ~~((ey - off.top) / 112);
			}
		},
		addStyle : function() {// 添加拖拽后的样式
			me.pbox.removeClass().addClass(
					"dock_container dock_pos_" + me.location);
			switch (me.location) {
			case "top":
				me.topPanel.box.css({
					"width" : "100%",
					"height" : "73px"
				}).show();
				me.leftPanel.box.css({
					"width" : "0",
					"height" : "0"
				}).hide();
				me.rightPanel.box.css({
					"width" : "0%",
					"height" : "0"
				}).hide();
				Deskpanel.box.css({
					"left" : 0,
					"right" : 0
				});
				Deskpanel.desktopsContainer.css("top", 73);
				break;
			case "left":
				me.leftPanel.box.css({
					"width" : "73px",
					"height" : "100%"
				}).show();
				me.topPanel.box.css({
					"width" : "0",
					"height" : "0"
				}).hide();
				me.rightPanel.box.css({
					"width" : "0%",
					"height" : "0"
				}).hide();
				Deskpanel.box.css({
					"left" : "73px",
					"right" : "0px"
				});
				Deskpanel.desktopsContainer.css("left", 73);
				break;
			case "right":
				me.rightPanel.box.css({
					"width" : "73px",
					"height" : "100%"
				}).show();
				me.leftPanel.box.css({
					"width" : "0",
					"height" : "0"
				}).hide();
				me.topPanel.box.css({
					"width" : "0",
					"height" : "0"
				}).hide();
				Deskpanel.box.css({
					"left" : 0,
					"right" : 73
				});
				deskpanelObj.desktopsContainer.css("top", 0);
				break;
			}

		},
		initDrag : function() {// 绑定元素拖拽
			var desk = deskpanelObj.desktopsContainer.find(".appListContainer");

			me.box.sortable({
				connectWith : desk,
				items : ".appButton",
				opacity : "0.6",
				scroll : true,
				containment : 'parent',// 只允许在父窗体中拖拽
				start : function(event, ui) {
				},
				stop : function(event, ui) {// 拖拽动作停止事件

					var item = ui.item;
					var p = item.parent();
					if (p.hasClass("appListContainer")) {
						item.css("position", "absolute");
					}
					deskpanelObj.refreshIcon();

				}

			}).disableSelection();
		}

	}

};

// 导航栏（上菜单导航）
Navbar = function(me) {

	var data = DATA.menu;
	var menu = "";
	for ( var i = 0; i < data.length; i++) {
		menu += "<a class=\"dock-item\" href=\"#\" id=\"desk_" + (i + 1)
				+ "\" name=\"desk_" + (i + 1) + "\">" + "<img src=\"" + imgpath
				+ data[i].icon + "\" /><span>" + data[i].name + "</span></a>";
	}
	var _box = "<div id='dock' class='dock'><div class='dock-container'>"
			+ menu + "</div></div>";

	return me = {
		init : function() {
			me.create();
			me.bindEvent();// 绑定导航按钮单击事件
			me.setPosition();
			me.changeStyle();// 初始化选中的桌面样式
		},
		bindEvent : function() {
			$("#dock a").click(function() {
				var page = $(this).attr("name");
				var _this = $(this);
				var index = parseInt(page.replace("desk_", ""));
				arrowsObj.changeStyle(index, thisPage);
				me.bindSwitchDesktopAnimate(index, thisPage);// 切换桌面
				NavbarStyle(_this);// 切换样式
			});
		},
		bindSwitchDesktopAnimate : function(t, c) {// 切换动画事件 t 目标桌面 c当前桌面
			if (t == c) {// 目标页数与当前页数相同时返回
				return;
			}
			var left = 0;
			var c = parseInt(c - 1);
			if (t < c) {// 往左移动
				left = -2000;
			} else {// 往右移动
				left = 2000;
			}
			var cdesk = deskpanelObj.desktopsContainer
					.find(".desktopContainer[index=" + c + "]"); // (thisPage
			// - 1)
			cdesk.removeClass("desktop_current");
			cdesk.stop().animate({
				left : left
			}, 'normal', function() {

			});
			var idesk = deskpanelObj.desktopsContainer
					.find(".desktopContainer[index=" + (t - 1) + "]");
			idesk.removeClass("desktop_current").addClass("desktop_current");
			idesk.stop().animate({
				left : 0
			}, 'normal', function() {

			});
			thisPage = t;
		},
		create : function() {// 创建导航
			me.box = $(_box);
			desktopObj.addPanel(me.box);
			init_dock();
		},
		setPosition : function() {// 设置位置
			var ww = $(window).width();
			var mw = me.box.width();
			me.box.css("left", parseInt(ww / 2) - parseInt(mw / 2));
		},
		changeStyle : function() {// 初始化选中的桌面样式
			var img = $("#desk_" + thisPage).children("img").attr("src");
			var png = img.substring(img.length - 4, img.length);
			img = img.substring(0, img.length - 4);
			img = img + png;// + "_thisMenu"
			$("#desk_" + thisPage).children("img").attr("src", img);
		}
	}
};

// 初始化分页箭头
Arrows = function() {

	var arrows_l = "<div id='arrows_l' class='arrows'><img src='../public/desktopskin/images/arrows_l_3.png' /></div>";
	var arrows_r = "<div id='arrows_r' class='arrows'><img src='../public/desktopskin/images/arrows_r_1.png' /></div>";
	return arrows = {
		init : function() {
			arrows.create();
			arrows.setPosition();
			arrows.bindEvent();
		},
		bindEvent : function() {
			mouseStyle();
			$("#arrows_l").click(function() {
				if (thisPage == 1) {
					return;
				} else {
					var t = parseInt(thisPage) - 1;
					arrows.changeStyle(t, thisPage);
					arrows.bindSwitchDesktopAnimate(t, thisPage);
					var desk_a = $("#desk_" + t);
					NavbarStyle(desk_a);// 切换样式
				}
			});
			$("#arrows_r").click(function() {
				if (thisPage == DATA.menu.length) {
					return;
				} else {
					var t = parseInt(thisPage) + 1;
					arrows.changeStyle(t, thisPage);
					arrows.bindSwitchDesktopAnimate(t, thisPage);
					var desk_a = $("#desk_" + t);
					NavbarStyle(desk_a);// 切换样式
				}
			});
		},
		bindSwitchDesktopAnimate : function(t, c) {
			var left = 0;
			var c = parseInt(c - 1);
			if (t < c) {// 往左移动
				left = -2000;
			} else {// 往右移动
				left = 2000;
			}
			var cdesk = deskpanelObj.desktopsContainer
					.find(".desktopContainer[index=" + (thisPage - 1) + "]");
			cdesk.removeClass("desktop_current");
			cdesk.stop().animate({
				left : left
			}, 'normal', function() {

			});
			var idesk = deskpanelObj.desktopsContainer
					.find(".desktopContainer[index=" + (t - 1) + "]");
			idesk.removeClass("desktop_current").addClass("desktop_current");
			idesk.stop().animate({
				left : 0
			}, 'normal', function() {

			});
			thisPage = t;
		},
		create : function() {
			desktopObj.addPanel(arrows_l);
			desktopObj.addPanel(arrows_r);
		},
		setPosition : function() {
			var wh = $(window).height();
			var ah = 112 / 2;
			$("#arrows_l").css({
				"top" : ((wh / 2) - ah) + "px",
				"left" : "80px"
			});
			$("#arrows_r").css({
				"top" : ((wh / 2) - ah) + "px",
				"right" : "80px"
			});
			$("#arrows_l img").css("cursor", "");
			$("#arrows_r img").css("cursor", "pointer");
		},
		changeStyle : function(t, c) {
			// 还原原来的icon
			var img = $("#desk_" + c).children("img").attr("src");
			img = img.replace("_thisMenu", "");
			$("#desk_" + c).children("img").attr("src", img);
			// 切换后的icon
			var this_img = $("#desk_" + t).children("img").attr("src");
			var png = this_img.substring(this_img.length - 4, this_img.length);
			this_img = this_img.substring(0, this_img.length - 4);
			this_img = this_img + png;// + "_thisMenu"
			$("#desk_" + t).children("img").attr("src", this_img);
			if (t > 1 && t < DATA.menu.length) {
				$("#arrows_l img").attr("src",
						"../public/desktopskin/images/arrows_l_1.png");
				$("#arrows_r img").attr("src",
						"../public/desktopskin/images/arrows_r_1.png");
				$("#arrows_l img").css("cursor", "pointer");
				$("#arrows_r img").css("cursor", "pointer");
			}
			if (t == 1) {
				$("#arrows_l img").attr("src",
						"../public/desktopskin/images/arrows_l_3.png");
				$("#arrows_r img").attr("src",
						"../public/desktopskin/images/arrows_r_1.png");
				$("#arrows_l img").css("cursor", "");
				$("#arrows_r img").css("cursor", "pointer");
			}
			if (t == DATA.menu.length) {
				$("#arrows_l img").attr("src",
						"../public/desktopskin/images/arrows_l_1.png");
				$("#arrows_r img").attr("src",
						"../public/desktopskin/images/arrows_r_3.png");
				$("#arrows_l img").css("cursor", "pointer");
				$("#arrows_r img").css("cursor", "");
			}
		}
	}
};

// 拖拽效果容器
dockEffectBox = function(me) {
	var _tbox = "<div id='docktop' class='dock_drap_effect dock_drap_effect_top ' style='display: none;' _olddisplay='block'></div>";
	var _lbox = "<div id='dockleft' class='dock_drap_effect dock_drap_effect_left' style='display: none;'></div>";
	var _rbox = "<div id='dockright' class='dock_drap_effect dock_drap_effect_right' style='display: none;'></div>";
	var _proxybox = "<div class='dock_drap_proxy' style='display: none; left: -79px; top: -260px;'></div>";
	var _maskbox = "<div id='dockmask' class='dock_drap_mask' style='display: none;'>"
			+ "<div class='dock_drop_region_top' cmd='region'name='top'></div>"
			+ "<div class='dock_drop_region_left' cmd='region' name='left'></div>"
			+ "<div class='dock_drop_region_right' cmd='region' name='right'></div>"
			+ "</div>";
	return me = {
		init : function() {
			me.create();
		},
		create : function() {
			me.tbox = $(_tbox);
			me.lbox = $(_lbox);
			me.rbox = $(_rbox);
			me.proxybox = $(_proxybox);
			me.maskbox = $(_maskbox);
			me.addDesktop();
		},
		addDesktop : function() {
			desktopObj.addPanel(me.tbox);
			desktopObj.addPanel(me.lbox);
			desktopObj.addPanel(me.rbox);
			desktopObj.addPanel(me.proxybox);
			desktopObj.addPanel(me.maskbox);
		},
		show : function() {
			me.tbox.show();
			me.lbox.show();
			me.rbox.show();
			me.maskbox.show();
		},
		hide : function() {
			me.tbox.hide();
			me.lbox.hide();
			me.rbox.hide();
			me.maskbox.hide();
		}

	}
};
// 底部文件夹菜单
Filelist = function() {
	var _folder = "<div id=\"folder\"><a href=\"#\">"
			+ "<div id=\"folder_content\">"
			+ "<div id=\"min_icon_folder\">"
			+ "<img width=\"32\" height=\"32\" border=\"0\" src=\"../public/desktopskin/icon/min/folder_o.png\" />"
			+ "</div>" + "<div id=\"min_font_folder\">文件夹</div>" + "</div>"
			+ "</a></div>";

	var _sonfolder = "<div id=\"filelist\" class=\"filelist\"></div>";

	return file = {
		init : function() {
			file.create();
			file.bindStyle();
			file.bindEvent();
		},
		create : function() {
			desktopObj.addPanel(_folder);
			desktopObj.addPanel(_sonfolder);
		},
		bindEvent : function() {// 加载事件
			$("#folder a").powerFloat({// 初始化
				width : 112,
				eventType : "click",
				targetMode : null,
				target : $("#filelist"),
				showCall : function() {

				}
			});
		},
		bindStyle : function() {
			$("#folder")
					.mouseenter(
							function() {
								$("#folder")
										.css(
												{
													"background-image" : "url(../public/desktopskin/images/bg_task_group_t_over.png)"
												});
							});
			$("#folder")
					.mouseleave(
							function() {
								$("#folder")
										.css(
												{
													"background-image" : "url(../public/desktopskin/images/bg_task_group_t_msg.png)"
												});
							});

		}
	}
};
// 底部栏容器类
BottomBar = function(me) {

	var _box = "<div id='bottomBar' class='bottomBar' style='z-index: 12;'></div>";
	var _NextBox = "<div id='taskNextBox' class='taskNextBox' _olddisplay='' style='display: none;'><a id='taskNext' class='taskNext' hidefocus='true' href='#'></a></div>";
	var _PreBox = "<div id='taskPreBox' class='taskPreBox' _olddisplay='' style='display: none;'><a id='taskPre' class='taskPre' hidefocus='true' href='#'></a></div>";
	var _taskContainner = "<div id='taskContainer' class='taskContainer' style=''></div>";
	var bottonbarbg = "<div class='bottomBarBg'></div>";
	var bottomBarBgTask = "<div class='bottomBarBgTask'></div>";

	return me = {
		init : function() {
			me.create();
			desktopObj.addPanel(me.box);
			desktopObj.addPanel(bottonbarbg);
			desktopObj.addPanel(bottomBarBgTask);
		},
		create : function() {
			var box = me.box = $(_box);
			me.innerbox = $("<div id='taskContainerInner' class='taskContainerInner' style=''></div>");
			me.taskContainner = $(_taskContainner);
			me.taskContainner.append(me.innerbox);
			box.append(_NextBox);
			box.append(me.taskContainner);
			box.append(_PreBox);
		},
		addItem : function(item) {// 像底部任务栏添加任务项
			me.innerbox.append(item);
			var len = me.innerbox.children().length;
			var id = item.attr("id");
			var w = item.width() * len + 20;
			me.taskContainner.width(w);
			me.innerbox.css({
				"margin-right" : 0,
				"width" : (w)
			});
			me.setCurrent(id);
		},
		getItem : function(id) {// 根据ID查询底部任务栏
			return me.innerbox.find("a[tid='" + id + "']");
		},
		getItemNum : function() {// 得到当前任务数
			return me.innerbox.children().size();
		},
		setCurrent : function(id) {
			me.addCurrent(id);
			me.removeItemSibling(id);
		},
		addCurrent : function(id) {// 设置当前任务栏样式
			me.innerbox.find("#" + id).addClass("taskCurrent");
		},
		removeItemSibling : function(id) {// 移除当前任务同类样式
			me.innerbox.find("#" + id).siblings().removeClass("taskCurrent");
		},
		getALLItemID : function() {// 得到当前任务栏所有任务ID
			var items = me.innerbox.children();
			var idArray = [];
			items.each(function() {
				var id = $(this).attr("id");
				id = id.substring(id.lastIndexOf("_") + 1, id.length);
				idArray.push(id);
			})
			return idArray;
		}

	}

};

var panelObj;
var bodyObj;
var desktopObj;
var deskpanelObj;
var sidebarObj;
var navbarObj;
var arrowsObj;
var dockEffectBoxObj;
var filelistObj;
var bottomBarObj;
var windowsObj;
var elsePanelObj;

$(function() {
	// alert(msnue);
	// 调用类方法
	ContMenuData();
	panelObj = Panel();
	bodyObj = Body();
	desktopObj = Desktop();
	deskpanelObj = Deskpanel();
	sidebarObj = Sidebar();
	navbarObj = Navbar();
	arrowsObj = Arrows();
	dockEffectBoxObj = dockEffectBox();
	filelistObj = Filelist();
	bottomBarObj = BottomBar();
	windowsObj = Windows();
	elsePanelObj = ElsePanel();

	init_event();// 初始化事件
	bodyObj.init();
	desktopObj.init();
	navbarObj.init();// 初始化导航条
	deskpanelObj.init(ops).refresh();
	sidebarObj.init({
		location : 'left',// 初始化sidebar的位置为左侧
		Icon : leftMenu
	});
	arrowsObj.init();// 初始化分页箭头
	bottomBarObj.init();// 初始化下部栏
	filelistObj.init();// 初始化底部文件夹
	// ElsePanel.init();//初始化其他面板

	$("#zoomWallpaper").attr('src', deskTheme);// 桌面主题背景
	IncludeLinkStyle(deskStyle);

});
// 初始化菜单
function init_dock() {
	$('#dock').Fisheye({
		maxWidth : 80,
		items : 'a',
		itemsText : 'span',
		container : '.dock-container',
		itemWidth : 40,
		proximity : 90,
		halign : 'center'
	})
}

// 初始化事件
init_event = function() {
	document.oncontextmenu = function() {// 屏蔽浏览器右键事件
		return false;
	};
	var isIE = navigator.appName;
	// 判断是否是IE浏览器
	if (isIE == "Microsoft Internet Explorer") {
		// 添加IE右击事件
		$("body").bind("mousedown", function(event) {
			if (event.which == 3) {
				var md = desktopObj.MenuData();
				$("body").smartMenu(md, {
					name : "image"
				});
			}
		});
	}
	$(document).bind('mousemove', function(e) {
		var area = $(window).width() - 50;
		if (e.pageX > area) {
			e.pageX = area;
		}
	});

}
// 工具类
Util = {
	formatmodel : function(str, model) {
		for ( var k in model) {
			var re = new RegExp("{" + k + "}", "g");
			str = str.replace(re, model[k])
		}
		return str
	}
}

mouseStyle = function() {// 箭头样式
	$("#arrows_l").mouseenter(
			function() {
				if (thisPage == 1) {
					return;
				} else {
					$("#arrows_l img").attr("src",
							"../public/desktopskin/images/arrows_l_2.png");
				}
			});
	$("#arrows_r").mouseenter(
			function() {
				if (thisPage == DATA.menu.length) {
					return;
				} else {
					$("#arrows_r img").attr("src",
							"../public/desktopskin/images/arrows_r_2.png");
				}
			});
	$("#arrows_l").mouseleave(
			function() {
				if (thisPage == 1) {
					$("#arrows_l img").attr("src",
							"../public/desktopskin/images/arrows_l_3.png");
				} else {
					$("#arrows_l img").attr("src",
							"../public/desktopskin/images/arrows_l_1.png");
				}
			});
	$("#arrows_r").mouseleave(
			function() {
				if (thisPage == DATA.menu.length) {
					$("#arrows_r img").attr("src",
							"../public/desktopskin/images/arrows_r_3.png");
				} else {
					$("#arrows_r img").attr("src",
							"../public/desktopskin/images/arrows_r_1.png");
				}
			});
}

// 任务类
Task = $.Class({
	init : function(op) {
		this.create(op);
		this.rightMenu();
	},
	create : function(op) {
		var task = $("<div>", {
			"class" : "taskGroup taskGroupAnaWidth",
			id : "taskGroup_" + op.id + "_" + op.id
		});
		var taskItemIcon = $("<div>", {
			"class" : "taskItemIcon"
		});
		$(
				"<img src='../public/desktopskin/icon/min/" + op.icon
						+ "'/><div class='taskItemIconState'></div>").appendTo(
				taskItemIcon);// 图片路径---------------------------------
		var taskItemTxt = $("<div>", {
			"class" : "taskItemTxt",
			text : op.title
		});
		var taskItemBox = $("<div>", {
			"class" : "taskItemBox"
		});
		var taskA = $("<a>", {
			"class" : "taskItem fistTaskItem",
			"href" : "#",
			id : "taskItem_" + op.id,
			"title" : op.title,
			"tid" : op.id,
			"appid" : op.id + "_" + op.id
		});
		taskA.append(taskItemIcon).append(taskItemTxt);
		taskItemBox.append(taskA);
		task.append(taskItemBox);
		this.box = task;
	},
	rightMenu : function() {
		var taskmenu = [ [ {
			text : "显示桌面",
			func : function() {
				windowsObj.showWindowDesk();
			}
		} ], [ {
			text : "关闭全部",
			func : function() {
				windowsObj.closeAllWindow();
			}
		} ], [ {
			text : "关闭其他",
			func : function() {
				var id = $(this).attr("id");
				wid = id.substring(id.lastIndexOf("_") + 1, id.length);
				windowsObj.closeElseWindow(wid);
			}
		} ], [ {
			text : "关闭",
			func : function() {
				var id = $(this).attr("id");
				wid = id.substring(id.lastIndexOf("_") + 1, id.length);
				art.dialog.list[wid].close();
				$("#" + id).remove();
			}
		} ] ]
		this.box.smartMenu(taskmenu, {
			name : "taskmenu",
			offsetX : -100,
			offsetY : -100
		});
	}
});

// 图标基类
appIcon_amg = $.Class({
	create : function(t) {
		this.box = $("<div type='" + t
				+ "' class='appButton amg_folder_appbutton' ></div>");
	}
});
// 图标类t0
appIcon_t0 = $.Class({
	create : function(t) {
		this.box = $("<div type='" + t + "' class='appButton'></div>");
		this.setRightMenu();
	},
	setRightMenu : function() {
	}
});

// 来至桌面的图标（桌面菜单导航）
appIcon_t1 = appIcon_t0
		.extend({
			init : function(fid) {
				this.fid = fid;
				this.app = DATA.app[fid];
				this.tx = 1;
				this.create(fid);
				this.bindEvent();
			},
			create : function(fid) {
				this._super(1);
				this.box.attr({
					id : "icon_app_" + this.app.appid + "_" + this.app.asc,
					appid : this.app.appid,
					fileid : this.app.appid,
					title : this.app.name,
					url : this.app.url,
					trendFn : this.app.func,// zhangfj
					trendArgs : this.app.args,
					sonMenu : this.app.sonMenu,
					uid : "app_" + this.app.appid,
					fid : fid
				});

				var appIcon = $("<div>", {
					id : "icon_app_" + this.app.appid + "_" + this.app.asc
							+ "_icon_div",
					"class" : "appButton_appIcon"
				});
				appIcon.append($("<img>", {
					alt : this.app.name,
					src : imgpath + this.app.icon, // '../public/desktopskin/icon/'
					// +
					// this.app.icon,//图片路径-------------------------------------------------------------------------------------------
					"class" : "appButton_appIconImg",
					id : 'icon_app_' + this.app.appid + '_' + this.app.asc
							+ '_img'

				}));
				var nameDiv = $("<div class='appButton_appName'></div>");
				// --------------------------- 菜单名
				// ---------------------------------
				/*
				 * var name_inner = $("<div>",{
				 * "class":'appButton_appName_inner',
				 * id:'icon_app_'+this.app.appid+'_'+this.app.asc+'_name',
				 * text:this.app.name }); var name_right =$("<div
				 * class='appButton_appName_inner_right'></div>");
				 * nameDiv.append(name_inner).append(name_right);
				 */
				// ---------------------------- 改
				// ---------------------------------
				/*
				 * alert(this.app.name.length); var thisAppName = "";
				 * if(this.app.name.length>4){ thisAppName =
				 * this.app.name.substring(0,4) + "..."; }else{ thisAppName =
				 * this.app.name; }
				 */
				var name_table = $("<table height=\"20\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\">"
						+ "<tr><td class=\"appButton_appName_table_left\">"
						+ this.app.name
						+ "</td>"
						+ "<td class=\"appButton_appName_table_right\" width=\"10\"></td></tr></table>");
				nameDiv.append(name_table);
				// ---------------------------------------------------------------------
				var notify = $("<div>", {
					"class" : 'appButton_notify',
					id : 'icon_app_' + this.app.appid + '_' + this.app.asc
							+ '_notify'
				});
				$("<span class='appButton_notify_inner'></span>").appendTo(
						notify);

				var deleteDiv = $("<div>", {
					title : '卸载应用',
					delMenuID : this.app.appid,
					id : 'icon_app_' + this.app.appid + '_' + this.app.asc
							+ '_delete',
					"class" : 'appButton_delete'
				});
				deleteDiv
						.click(function(e) {
							// alert('移除' + $(this).attr("delMenuID"));
							var delMenuID = $(this).attr("delMenuID");
							var displayDesktop = 0;
							if (ManageDesktopMenu(delMenuID, displayDesktop)) {
								var menuele = $(this).attr("id").replace(
										"_delete", "");
								$("#" + menuele).remove();// 移除菜单元素
							}
							e.stopPropagation(); // 阻止冒泡 阻止继续向dom上层传递
						})

				this.box.append(appIcon).append(nameDiv).append(notify).append(
						deleteDiv);
			},
			bindEvent : function() {// 绑定事件
				this.box.click(function(e) {
					e.preventDefault();
					e.stopPropagation();
					var _this = $(this);
					var id = _this.attr("appid");
					var title = $.trim(_this.text());
					var url = _this.attr("url");
					// var icon = _this.find("img").attr("src").split("/")[1];
					var icons = _this.find("img").attr("src").split("/");
					var icon = icons[icons.length - 1];
					var sonMenu = _this.attr("sonMenu");// 获取子菜单
					// var jsonSonMenu = eval("(" + sonMenu +
					// ")");//将json格式的字符串转换为json

					var trendFn = _this.attr("trendFn");
					var trendArgs = _this.attr("trendArgs");
					windowsObj.openApp(id, title, url, icon, sonMenu, 700, 500,
							trendFn, trendArgs);
				});
			}
		});
// 来至侧边框的图标（左菜单导航）
appIcon_t2 = appIcon_t0
		.extend({
			init : function(fid) {
				this.fid = fid;
				this.sApp = DATA.sApp[fid];
				this.tx = 2;
				this.create();
				this.bindEvent();
			},
			create : function() {
				this._super(2);
				this.box.attr({
					id : "icon_app_" + this.sApp.appid + "_" + this.sApp.asc,
					appid : this.sApp.appid,
					fileid : this.sApp.appid,
					title : this.sApp.name,
					url : this.sApp.url,
					sonMenu : this.sApp.sonMenu,
					uid : "app_" + this.sApp.appid
				});
				var appIcon = $("<div>", {
					id : "icon_app_" + this.sApp.appid + "_" + this.sApp.asc
							+ "_icon_div",
					"class" : "appButton_appIcon"
				});
				appIcon.append($("<img>", {
					alt : this.sApp.name,
					src : imgpath + this.sApp.icon,// '../public/desktopskin/icon/'
					// + this.sApp.icon,
					"class" : "appButton_appIconImg",
					id : 'icon_app_' + this.sApp.appid + '_' + this.sApp.asc
							+ '_img'

				}));
				var nameDiv = $("<div class='appButton_appName'></div>");
				var name_inner = $("<div>", {
					"class" : 'appButton_appName_inner',
					id : 'icon_app_' + this.sApp.appid + '_' + this.sApp.asc
							+ '_name',
					text : this.sApp.name
				});
				var name_right = $("<div class='appButton_appName_inner_right'></div>");
				nameDiv.append(name_inner).append(name_right);
				var deleteDiv = $("<div", {
					title : '卸载应用',
					id : 'icon_app_' + this.sApp.appid + '_' + this.sApp.asc
							+ '_delete',
					"class" : 'appButton_delete'
				});

				this.box.append(appIcon).append(nameDiv).append(deleteDiv);
			},
			bindEvent : function() {// 绑定事件
				this.box.click(function(e) {

					e.preventDefault();
					e.stopPropagation();
					var _this = $(this);
					var id = _this.attr("appid");
					var title = $.trim(_this.text());
					var url = _this.attr("url");
					// var icon = _this.find("img").attr("src").split("/")[1];
					var icons = _this.find("img").attr("src").split("/");
					var icon = icons[icons.length - 1];
					var sonMenu = _this.attr("sonMenu");
					// if (sonMenu == undefined || sonMenu == "") {
					// sonMenu = "[]";
					// }
					// var jsonSonMenu = eval("(" + sonMenu +
					// ")");//将json格式的字符串转换为json

					var trendFn = _this.attr("trendFn");
					var trendArgs = _this.attr("trendArgs");
					url = getRootPath() + url;// 拼接具体Url路径
					windowsObj.openApp(id, title, url, icon, sonMenu, 700, 500,
							trendFn, trendArgs);
				});
			}
		});

// 桌面窗体类 集成
Windows = function(me) {
	return me = {
		showWindow : function(id) {// art弹出
			var array = art.dialog.list;
			var taskIds = bottomBarObj.getALLItemID();
			var taskLen = taskIds.length;
			var api = array[id];
			var wrap = api.DOM.wrap;
			var $wrap = $(wrap);
			if (taskLen > 1) {// 判断任务个数 显示切换和焦点切换
				if ($wrap.is(":hidden")) {
					api.show();
				} else {
					if (!$wrap.hasClass("aui_state_focus")) {
						api.focus();
					} else {
						api.hide();
					}
				}

			} else {
				if ($wrap.is(":visible")) {
					api.hide();
				} else {
					api.show();
				}
			}
		},
		openSys : function(op) {// 打开系统窗体
			art.dialog({
				id : op.id,
				title : op.title,
				width : op.width,
				height : op.height,
				max : false,
				min : false,
				content : op.content,
				close : function() {
					if (themeSet) {// 更新主题
						themeSet = false;
						UpdateThemeStyle(themeList);
					}
					if (styleSet) {// 更新样式
						styleSet = false;
						UpdateThemeStyle(themeList);
					}
				}
			});

		},
		bindStyle : function() {
			$(".sonfile")
					.mouseenter(
							function() {
								$(this)
										.css(
												{
													"background-image" : "url(../public/desktopskin/images/bg_task_group_t_over.png)"
												});
							});
			$(".sonfile")
					.mouseleave(
							function() {
								$(this)
										.css(
												{
													"background-image" : "url(../public/desktopskin/images/bg_task_group_t.png)"
												});
							});
		},
		bindEvent : function(id) {
			$(".sonMenuList")
					.bind(
							"mouseenter",
							function() {
								$(this)
										.css(
												{
													"background-image" : "url(../public/desktopskin/images/appbutton_mouseover_bg3.png)"
												});
							});
			$(".sonMenuList").bind("mouseleave", function() {
				$(this).css({
					"background-image" : "none"
				});
			});
			$(".sonMenuList").click(
					function() {

						var _this = $(this);
						var id = _this.attr("appid");
						var title = $.trim(_this.text());
						var url = _this.attr("url");
						// var icon =
						// _this.find("img").attr("src").split("/")[1];
						var icons = _this.find("img").attr("src").split("/");
						var icon = icons[icons.length - 1];
						var sonMenu = "[]"
						// var jsonSonMenu = eval("(" + sonMenu +
						// ")");//将json格式的字符串转换为json

						var trendFn = _this.attr("trendFn");
						var trendArgs = _this.attr("trendArgs");
						windowsObj.openApp(id, title, url, icon, sonMenu, 700,
								500, trendFn, trendArgs);
					});
			$("#sonfile_a" + id).click(function() {
				var wrap = art.dialog.list[id].DOM.wrap;
				var $wrap = $(wrap);
				if ($wrap.is(":hidden")) {
					art.dialog.list[id].show();
					art.dialog.list[id].focus();
				} else {
					if (!$wrap.hasClass("aui_state_focus")) {
						art.dialog.list[id].focus();
					} else {
						art.dialog.list[id].show();
					}
				}
			});
		},

		openApp : function(id, title, url, icon, jsonSonMenu, width, height,
				trendFn, trendArgs) {// 打开应用窗体-------------------------------------------------------------------------
			var taskInner = bottomBarObj.innerbox;
			var taskItem = bottomBarObj.getItem(id);// 从最小化图标中获取
			if (jsonSonMenu == undefined || jsonSonMenu == "")
				jsonSonMenu = "[]"
			jsonSonMenu = eval("(" + jsonSonMenu + ")");
			if (taskItem.length == 1) { // 若当前窗体已是最小化 直接最大化就可以
				var wrap = art.dialog.list[id].DOM.wrap;
				var $wrap = $(wrap);
				if ($wrap.is(":hidden")) {
					art.dialog.list[id].show();
					art.dialog.list[id].focus();
				} else {
					if (!$wrap.hasClass("aui_state_focus")) {
						art.dialog.list[id].focus();
					} else {
						art.dialog.list[id].show();
					}
				}
				return;
			} else { // 若当前窗体未打开
				var len = bottomBarObj.getItemNum();// 任务图标集合 大于7 不让添加
				var taskLength = (len + 1) * 114 + 20;// 任务栏长度
				if (len > 30 && len != 0) {
					art.dialog({
						title : "系统提示",
						width : 255,
						height : 80,
						max : false,
						min : false,
						content : "任务过多，请关闭其他任务！",
						button : [ {
							name : "手动关闭"
						}, {
							name : "关闭所有",
							callback : function() {
								windowsObj.closeAllWindow();
							}
						} ]
					});
					return false;
				}
				var task = Task({// 创建最小化任务图标
					"id" : id,
					"title" : title,
					"icon" : icon
				});
				bottomBarObj.addItem(task.box);
				task.box.click(function() {
					me.showWindow(id);
					bottomBarObj.setCurrent(task.box.attr("id"));
				});
				var sonfile = "<a id=\"sonfile_a"
						+ id
						+ "\" href=\"#\">"
						+ "<div id=\"sonfile_"
						+ id
						+ "\" class=\"sonfile\">"
						+ "<div class=\"min_icon_sonfolder\">"
						+ "<img width=\"32\" height=\"32\" border=\"0\" src=\"../public/desktopskin/icon/min/"
						+ icon + "\" />" + "</div>"
						+ "<div class=\"min_font_sonfolder\">" + title
						+ "</div>" + "</div></a>";
				if (jsonSonMenu.length > 0) {
					var sonlist = "";
					var properties = "";
					for ( var i = 0; i < jsonSonMenu.length; i++) {
						properties = "appid=\"" + jsonSonMenu[i].appid
								+ "\" url=\"" + jsonSonMenu[i].url + "\"";
						sonlist += "<div id=\""
								+ jsonSonMenu[i].appid
								+ "\" "
								+ properties
								+ " class=\"sonMenuList\" align=\"center\">"
								+ "<a href=\"#\"><div class=\"sonMenuListIocn\">"
								+ "<img width=\"64\" height=\"64\" src=\"../public/desktopskin/icon/"
								+ jsonSonMenu[i].icon + "\" />" + "</div>"
								+ "<div class=\"sonMenuListTitle\">"
								+ jsonSonMenu[i].name + "</div></a>" + "</div>";
					}
					var _box = "<div id=\"sonMenu_box"
							+ id
							+ "\" class=\"sonMenuListBox\"><div class=\"sonMenu_line\">"
							+ "<span class=\"sonMenu_font\">应用</span></div>"
							+ sonlist + "</div>";

					art.dialog({
						"id" : id,
						padding : 15,
						title : title,
						width : 700,
						height : 490,
						max : true,
						min : true,
						content : _box,
						close : function() {
							windowsObj.closeMinTask(id);
							$("#sonfile_a" + id).remove();
							if ($("#filelist a").size() == 0) {
								$("#folder").hide();
							}
						}
					});

				} else {
					if (url != "") { // 主要针对左菜单以及用户自定义地址
						// art.dialog.open(url,/** 弹出ART窗体*/
						// {
						// "id": id,
						// title: title,
						// width: 980,//设置窗口宽度自动适应width
						// height: height,
						// close: function () {
						// Windows.closeMinTask(id);
						// $("#sonfile_a" + id).remove();
						// if ($(window).width() <= taskLength) {
						// $("#folder").hide();
						// }
						// if (count > BottomBar.getItemNum()) {
						// $("#folder").hide();
						// }
						// }
						// }
						// );
						TrendsFn('Sys_OpenPage', url, id);
					} else
						TrendsFn(trendFn, trendArgs, id);
				}
				// 创建文件夹
				var ww = $(window).width() - 100;
				if (ww <= taskLength) {
					$("#filelist").append(sonfile);
				}
				me.bindStyle();
				me.bindEvent(id); // windows 窗体
				if ($(window).width() <= taskLength) {
					$("#folder").show();
					count = bottomBarObj.getItemNum()
				}
			}
		},
		closeElseWindow : function() { // 关闭其他窗体
			var list = art.dialog.list;
			for ( var i in list) {
				if (i != id) {
					list[i].close();
				}
			}
			;
		},
		closeAllWindow : function() {// 关闭所有窗体
			var list = art.dialog.list;
			for ( var i in list) {
				list[i].close();
			}
			;
		},
		closeMinTask : function(id) {// 关闭任务
			$("#taskGroup_" + id + "_" + id).remove();
		},
		hideWindow : function(id) {// 隐藏
			art.dialog.list[id].hide();
		},
		showWindowDesk : function() {// 显示桌面
			var list = art.dialog.list;
			for ( var i in list) {
				list[i].hide();
			}
			;
		},
		closeWindowBack : function() {
			windowsObj.closeMinTask(id);
			$("#sonfile_a" + id).remove();
			if ($(window).width() <= taskLength) {
				$("#folder").hide();
			}
			if (count > bottomBarObj.getItemNum()) {
				$("#folder").hide();
			}
		}
	}

};

// 动态调用桌面窗体弹出方法
var args1, args2, args3, args4, args5, args6, args7, args8, args9, args10, args11;
var xID;
function TrendsFn(trendFn, trendArgs, id) {
	if (trendFn != undefined && trendFn != "") { // 窗体弹出时函数
		if (trendArgs != undefined && trendArgs != "") // 带参数的窗体弹出时函数
		{
			var args = "";
			trendArgs = trendArgs.split(';');
			var len = trendArgs.length;
			args1 = [ trendArgs[0], id ];
			args2 = len - 1 <= 0 ? '' : trendArgs[1];
			args3 = len - 2 <= 0 ? '' : trendArgs[2];
			args4 = len - 3 <= 0 ? '' : trendArgs[3];
			args5 = len - 4 <= 0 ? '' : trendArgs[4];
			args6 = len - 5 <= 0 ? '' : trendArgs[5];
			args7 = len - 6 <= 0 ? '' : trendArgs[6];
			args8 = len - 7 <= 0 ? '' : trendArgs[7];
			args9 = len - 8 <= 0 ? '' : trendArgs[8];
			args10 = len - 9 <= 0 ? '' : trendArgs[9];
			args11 = len - 10 <= 0 ? '' : trendArgs[10];
			trendFn = eval(trendFn);
			trendFn(args1, args2, args3, args4, args5, args6, args7, args8,
					args9, args10, args11);
		} else
			// 不带参数的窗体弹出时函数
			trendFn();
	}
}

// 其他面板(注释)
ElsePanel = function(me) {
	// var mome ="<div id=\"mome\"><div class=\"infotitl\">备忘录</div></div>";
	// var inform="<div id=\"inform\"><div class=\"infotitl\">通知</div></div>";
	// var _msgBox = "<div id=\"msg\"><div id=\"msg_close\"><a
	// href=\"#\">关闭</a></div></div>";
	// return ep = {
	// init:function(){
	// ep.create();
	// ep.bindEvent();
	// },
	// create:function(){
	// Desktop.addPanel(mome);
	// Desktop.addPanel(inform);
	// //右下角弹出消息框
	// Desktop.addPanel(_msgBox);
	// },
	// bindEvent:function(){
	// $("#mome").draggable({containment:"#desktop",start:function(){
	// var zindex = $("#inform").css("z-index");
	// var z = parseInt(zindex)+1;
	// $("#mome").css({"z-index":z});
	// }});
	// $("#inform").draggable({containment:"#desktop",start:function(){
	// var zindex = $("#mome").css("z-index");
	// var z = parseInt(zindex)+1;
	// $("#inform").css({"z-index":z});
	// }});
	// $("#mome").click(function (){
	// var zindex = $("#inform").css("z-index");
	// var z = parseInt(zindex)+1;
	// $("#mome").css({"z-index":z});
	// });
	// $("#inform").click(function (){
	// var zindex = $("#mome").css("z-index");
	// var z = parseInt(zindex)+1;
	// $("#inform").css({"z-index":z});
	// });
	// $("#msg_close a").click(function(){
	// $("#msg").slideUp();
	// });
	// }
	// }
};
// 导航样式(注释)
NavbarStyle = function(_this) {
	var id = _this.attr("id");
	for ( var i = 1; i <= DATA.menu.length; i++) {
		var temp_id = "desk_" + i;
		if ($.trim(temp_id) != $.trim(id)) {
			var img = $("#" + temp_id).children("img").attr("src");
			if (img.indexOf("_thisMenu") != -1) {
				img = img.replace("_thisMenu.png", ".png");
				$("#" + temp_id).children("img").attr("src", img);
			}
		}
	}
	var this_img = _this.children("img").attr("src");
	var is_thisImg = this_img.indexOf("_thisMenu");
	if (is_thisImg != -1) {
		return;
	} else {
		var png = this_img.substring(this_img.length - 4, this_img.length);
		this_img = this_img.substring(0, this_img.length - 4);
		this_img = this_img + "_thisMenu" + png;//
		_this.children("img").attr("src", this_img);
	}
}
// 显示右下角消息框
msgShow = function() {
	$("#msg").slideDown();
};
// 隐藏右下角消息框
msgHide = function() {
	$("#msg").slideUp();
};