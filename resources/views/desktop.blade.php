<!DOCTYPE html >
<html>
<head>
<title>我的控制台</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></meta>
<meta name="_token" content="{{ csrf_token() }}" charset="utf-8" />
<link href="{{url('/css/bootstrap/bootstrap.min.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{url('/css/powerFloat.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/smartMenu.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/desktop/desktop.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/desktop/themesetting.css')}}" rel="stylesheet"
	type="text/css">
<link id="trendsStyle" href="{{ $styletheme->usertheme}}"
	rel="stylesheet" />
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-1.8.2.min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-ui-1.8.24.custom.min.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/common.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-powerFloat-min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-smartMenu-min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-class.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/artDialog.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/iframeTools.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/layer/layer.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/validate.js')}}"></script>

</head>
<body>
	<script type="text/javascript"
		src="{{url('/javascript/interface.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/desktop/desktop.js')}}"></script>
	<div id="os_desktop">
		<div id="themeSetting_wrap" style="display: none;">
			<div id="themeSetting_head" class="themeSetting_head">
				<div id="themeSetting_tabTheme" class="themeSetting_tab current"
					style="display: block;">系统主题</div>
			</div>
			<div id="themeSetting_body" class="themeSetting_body">
				<div id="themeSetting_area" class="themeSetting_area"
					style="display: block;">
					<a href="###" themeid="theme_blue"
						class="themeSetting_settingButton" id="themeSetting_theme_blue">
						<div style="background: url(images/theme_blue.jpg) no-repeat;"
							class="themeSetting_settingButton_icon"></div>
						<div class="themeSetting_settingButton_text">梦幻光影</div>
					</a> <a href="###" themeid="theme_pinky_night"
						class="themeSetting_settingButton"
						id="themeSetting_theme_pinky_night">
						<div
							style="background: url(images/theme_pinky_night.jpg) no-repeat;"
							class="themeSetting_settingButton_icon"></div>
						<div class="themeSetting_settingButton_text">粉红之夜</div>
					</a> <a href="###" themeid="theme_green"
						class="themeSetting_settingButton" id="themeSetting_theme_green">
						<div style="background: url(images/theme_green.jpg) no-repeat;"
							class="themeSetting_settingButton_icon"></div>
						<div class="themeSetting_settingButton_text">青青世界</div>
					</a> <a href="###" themeid="theme_wood1"
						class="themeSetting_settingButton" id="themeSetting_theme_wood1">
						<div style="background: url(images/theme_wood1.jpg) no-repeat;"
							class="themeSetting_settingButton_icon"></div>
						<div class="themeSetting_settingButton_text">温馨木纹</div>
					</a> <a href="###" themeid="theme_wood2"
						class="themeSetting_settingButton" id="themeSetting_theme_wood2">
						<div style="background: url(images/theme_wood2.jpg) no-repeat;"
							class="themeSetting_settingButton_icon"></div>
						<div class="themeSetting_settingButton_text">黑色木纹</div>
					</a>
				</div>
				<div id="themeSetting_wallpaper" class="themeSetting_wallpaper"
					style="display: none;"></div>
			</div>
		</div>
		<div id="zoomWallpaperGrid" class="zoomWallpaperGrid"
			style="position: absolute; z-index: -10; left: 0pt; top: 0pt; overflow: hidden; height: 381px; width: 1440px;">
			<img id="zoomWallpaper" class="zoomWallpaper"
				style="position: absolute; top: 0pt; left: 0pt; height: 381px; width: 1440px;"
				src="{{$styletheme->userbg}}">
		</div>
		<div class="taskbar_start_menu_container" id="startMenuContainer"
			_olddisplay="block" style="display: none;">
			<div class="startMenuImg taskbar_start_menu_body"
				id="taskbar_start_menu_body">
				<div uin="0" class="taskbar_start_menu_selfinfo"
					id="startMenuSelfInfo">
					<div class="taskbar_start_menu_nick" id="startMenuSelfNick">
						欢迎，<a href="#">{{$username}}</a>
					</div>
					<a title="反馈" href="###"
						class="startMenuImg startMenuTopControl_support" cmd="support">&nbsp;</a>
					<a title="锁定" href="###"
						class="startMenuImg startMenuTopControl_lock" cmd="lock">&nbsp;</a>
				</div>
				<ul class="taskbar_start_menu">
					<li cmd="favorite"><a title="添加到收藏夹" href="###">添加到收藏夹</a></li>
					<li cmd="shortcut"><a title="保存桌面快捷方式" target="_blank" href="###">保存桌面快捷方式</a></li>
					<li cmd="download"><a title="下载客户端" href="###">下载客户端</a></li>
					<li title="关于Q+ Web" cmd="about" id="taskbar_helpButton"><a
						href="###">关于Web</a></li>
					<li cmd="helper"><a title="新手指导" href="###">新手指导</a></li>
				</ul>
				<a class="startMenuImg logout_botton" title="注销当前用户" cmd="logout"
					href="{{url('/auth/logout')}}"></a>
			</div>
		</div>
	</div>

</body>
<script type="text/javascript"
	src="{{url('/javascript/systemsettings/systemsettings.js')}}"></script>
</html>
