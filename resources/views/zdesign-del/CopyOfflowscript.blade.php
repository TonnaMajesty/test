<!DOCTYPE HTML>
<html>
<head>
<title>流程设计</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="_token" content="{{ csrf_token() }}" charset="utf-8" />
<link href="{{url('/css/bootstrap/bootstrap.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/site.css')}}" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css"
	href="{{url('/css/flowdesign/flowdesign.css')}}" />
<!--select 2-->
<link rel="stylesheet" type="text/css"
	href="{{url('/css/jquery.multiselect2side/jquery.multiselect2side.css')}}" />

<link rel="stylesheet" href="{{url('/css/ztree/demo.css')}}"
	type="text/css">
<link rel="stylesheet" href="{{url('/css/ztree/ztree.css')}}"
	type="text/css">
<link href="{{url('/css/smartMenu.css')}}" rel="stylesheet"
	type="text/css" />
<style type="text/css">
.leftFrame {
	margin-left: 0;
	margin-top: 0px;
	width: 220px;
	overflow: visible;
	float: left;
	background-color: white;
	height: 100%;
}

.rightFrame {
	/* margin: 0;
	float: left; */
	margin: 0 0 0 220px;
	overflow: auto;
	text-align: center;
	background-color: blue;
	height: 100%;
}
</style>
</head>
<body>
	<div id="leftFrame" name="leftFrame" class="leftFrame">
		<span id="abcd"
			style="width: 200px; height: 20px; background-color: blue;"
			script_id="89">abcdddd</span>
		<div class="zTreeDemoBackground left">
			<ul id="treeDemo" class="ztree"></ul>
		</div>
	</div>
	<div id="rightFrame" name="rightFrame" class="rightFrame">
		<!-- http://localhost:8088/laravel2/ https://www.baidu.com/-->
		<!-- frameborder 内嵌帧边框 是否显示边缘；填”1″表示”是”，填”0″表示”否”
		marginwidth：帧内文本的左右页边距
		marginheight：帧内文本的上下页边距
		allowtransparency：是否允许透明 -->
		<!-- fixed navbar -->
		<div class="navbar-inverse">
			<div class="navbar-inner">
				<div class="container">
					<div class="pull-right">
						<button class="btn btn-info" type="button" id="leipi_save">保存设计</button>
						<button class="btn btn-danger" type="button" id="leipi_clear">清空连接</button>
					</div>
				</div>
			</div>
		</div>
		<div id="canvasMenu" style="display: none;">
			<ul>
				<li id="cmSave"><i class="icon-ok"></i>&nbsp;<span class="_label">保存设计</span></li>
				<li id="cmRefresh"><i class="icon-refresh"></i>&nbsp;<span
					class="_label">刷新 F5</span></li>
			</ul>
		</div>
		<div class="container mini-layout" id="flowdesign_canvas"></div>
		<!-- /container -->
		<!--contextmenu div-->
		<div id="processMenu" style="display: none;">
			<ul>
				<li id="pmAttribute"><i class="icon-cog"></i>&nbsp;<span
					class="_label">属性</span></li>
				<li id="pmDelete"><i class="icon-trash"></i>&nbsp;<span
					class="_label">删除</span></li>
			</ul>
		</div>
		<!--end div-->
	</div>

	<script type="text/javascript"
		src="{{url('/javascript/jquery/jquery-1.8.2.min.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/bootstrap/bootstrap.min.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/jquery/jquery-ui-1.8.24.custom.min.js')}}"></script>
	<script type="text/javascript" src="{{url('/javascript/common.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/jsplumb/jquery.jsPlumb-1.3.16-all-min.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/jquery.contextmenu.r2.js')}}"></script>
	<!--select 2-->
	<script type="text/javascript"
		src="{{url('/javascript/jquery.multiselect2side/jquery.multiselect2side.js')}}"></script>
	<!--flowdesign-->
	<script type="text/javascript"
		src="{{url('/javascript/flowdesign/flowdesign.v3.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/systemsettings/systemsettings.js')}}"></script>

	<script type="text/javascript"
		src="{{url('/javascript/ztree/jquery.ztree.core.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/ztree/jquery.ztree.exedit.js')}}"></script>
	<script type="text/javascript"
		src="{{url('/javascript/jquery/jquery-smartMenu-min.js')}}"></script>

	<div id="scriptAttribute" style="display: none;">
		<ul class="nav nav-tabs">
			<li class="active"><a href="#home" data-toggle="tab">Home</a></li>
			<li><a href="#ios" data-toggle="tab">iOS</a></li>
		</ul>
		<div class="tab-content">
			<div class="tab-pane fade in active" id="home">home</div>
			<div class="tab-pane fade" id="ios">ios</div>
		</div>
	</div>

	<script type="text/javascript">
	$(function(){
		FlowScriptUtil.init();
		/* $('#myTab li:eq(1) a').tab('show'); */
		var height = $(window).height();
		var width = $(window).width();
		$("#flowdesign_canvas").css("height", height - 42);
	});
	</script>
</body>




</html>