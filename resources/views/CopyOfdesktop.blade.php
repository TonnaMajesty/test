<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Desktop</title>

<link
	href="{{URL::asset('/desktopskin/css/jquery-ui-1.8.24.custom.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{URL::asset('/desktopskin/css/main.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{URL::asset('/desktopskin/css/themesetting.css')}}"
	rel="stylesheet" type="text/css">
<link href="{{URL::asset('/desktopskin/css/powerFloat.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{URL::asset('/desktopskin/css/smartMenu.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{URL::asset('/desktopskin/css/style.css')}}"
	rel="stylesheet" type="text/css" />

<script type="text/javascript"
	src="{{URL::asset('/javaScript/jquery-1.8.2.min.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/jquery-ui-1.8.24.custom.min.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/jquery-powerFloat-min.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/jquery-smartMenu-min.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/jquery-class.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/interface.js')}}"></script>

<script type="text/javascript"
	src="{{URL::asset('/javaScript/CommonDialog.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/iframeTools.js')}}"></script>


<script src="{{URL::asset('/javaScript/SystemCommon.js')}}"></script>
<script type="text/javascript"
	src="{{URL::asset('/javaScript/desktop.js')}}"></script>

<style type="text/css">
.RunForm_opreateBtn {
	width: 100%;
	margin-top: 2px;
	margin-bottom: 0px;
	text-align: center;
	vertical-align: bottom;
}

.RunForm_opreateBtn input {
	border-width: 0;
	border-style: solid;
	width: 60px;
	height: 25px;
	cursor: pointer;
	margin-left: 20px;
}

.RunForm_opreateBtn .btn-common {
	background: #0866c6;
	border-color: #0a6bce;
	color: #fff;
}

.RunForm_opreateBtn .btn-cancle {
	color: #333333;
	width: 60px;
}

body {
	font-size: 12px;
}
</style>
</head>
<body>
	<input id="menujson" type="hidden" value="{{$menujson}}">
	<div id="themeSetting_wrap" style="display: none;">
		<div id="themeSetting_head" class="themeSetting_head">
			<div id="themeSetting_tabTheme" class="themeSetting_tab current"
				style="display: block;">经典主题</div>

			<div id="themeSetting_tabTheme2" class="themeSetting_tab current"
				style="display: block;">系统样式</div>
		</div>
		<div id="themeSetting_body" class="themeSetting_body"></div>
	</div>
	<div id="styleSetting_wrap" style="display: none;">
		<div id="styleSetting_head" class="themeSetting_head">
			<div id="styleSetting_tabTheme" class="themeSetting_tab current"
				style="display: block;">经典样式</div>
		</div>
		<div id="styleSetting_body" class="themeSetting_body"></div>
	</div>

	<div id="ideaSetting_wrap" style="display: none;">
		<div>
			<span style="font-style: italic;">给我们提出宝贵的意见或建议！</span>
		</div>
		<div id="ideaSetting_body">
			<textarea id="ideaInfo"
				style="width: 100%; height: 220px; overflow: auto; line-height: 20px;"></textarea>
		</div>
		<div class="RunForm_opreateBtn">
			<input id="saveIdea" class="btn-common" type="button" value="保存" /> <input
				id="cancel" class="btn-cancle" type="button" value="取消" />
		</div>
	</div>

	<div id="zoomWallpaperGrid" class="zoomWallpaperGrid"
		style="position: absolute; z-index: -10; left: 0pt; top: 0pt; overflow: hidden; height: 581px; width: 1440px;">
		<img id="zoomWallpaper" class="zoomWallpaper"
			style="position: absolute; top: 0pt; left: 0pt; height: 581px; width: 1440px;"
			src="">
	</div>
	<div class="taskbar_start_menu_container" id="startMenuContainer"
		_olddisplay="block" style="display: none;">
		<div class="startMenuImg taskbar_start_menu_body"
			id="taskbar_start_menu_body">
			<div uin="0" class="taskbar_start_menu_selfinfo"
				id="startMenuSelfInfo">
				<div class="taskbar_start_menu_nick" id="startMenuSelfNick"></div>
				<span title="意见反馈" class="startMenuImg startMenuTopControl_support"
					cmd="support" onclick="SubmitIdeas();">&nbsp;</span> <span
					title="用户详情" class="startMenuImg startMenuTopControl_lock"
					cmd="lock">&nbsp;</span>
			</div>
			<ul class="taskbar_start_menu">
				<li cmd="favorite"><span title="表单设计器">表单设计器</span></li>
				<li cmd="shortcut"><span title="列表构建器"
					onclick="return OpenListStructure();">列表构建器</span></li>
				<li cmd="download"><span title="下载工具客户端">下载工具客户端</span></li>
				<li title="关于U8ZDHFrame" cmd="about" id="taskbar_helpButton"><span>关于框架</span>
				</li>
				<li cmd="helper"><span title="指导手册">指导手册</span></li>
			</ul>
			<a class="startMenuImg logout_botton" title="注销当前用户" cmd="logout"
				href="###"></a>
		</div>
	</div>


</body>
</html>
