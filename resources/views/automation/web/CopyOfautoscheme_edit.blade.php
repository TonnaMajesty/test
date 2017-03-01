@extends('app') @section('mastercontent')
<link href="{{url('/css/site.css')}}" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css"
	href="{{url('/css/plugins/flowdesign/flowdesign.css')}}" />
<!--select 2-->
<link rel="stylesheet" type="text/css"
	href="{{url('/css/plugins/jquery.multiselect2side/jquery.multiselect2side.css')}}" />

<link rel="stylesheet"
	href="{{url('/css/plugins/ztree/ztree-app.css')}}" type="text/css">
<link rel="stylesheet" href="{{url('/css/plugins/ztree/ztree.css')}}"
	type="text/css">
<link href="{{url('/css/smartMenu/smartmenu.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/plugins/iCheck/icheck.css')}}" rel="stylesheet"
	type="text/css" />
<script type="text/javascript"
	src="{{url('/javascript/plugins/iCheck/icheck.min.js')}}"></script>
<input type="hidden" id="schemeId" value="{{$schemeid}}">
<input type="hidden" id="opt" value="{{$opt}}">
<div class="frame">
	<div id="leftFrame" name="leftFrame" class="leftFrame">
		<div class="zTreeDemoBackground left">
			<ul id="testcase" class="ztree"></ul>
		</div>
	</div>
	<div id="rightFrame" name="rightFrame" class="rightFrame">
		<div id="canvasMenu" style="display: none;">
			<!-- <ul>
				<li id="cmSave"><i class="icon-ok"></i>&nbsp;<span class="_label">保存设计</span></li>
				<li id="cmRefresh"><i class="icon-refresh"></i>&nbsp;<span
					class="_label">刷新 F5</span></li>
			</ul> -->
		</div>
		<div class="container mini-layout" id="flowdesign_canvas"></div>
		<!-- /container -->
		<!--contextmenu div-->
		<div id="processMenu" style="display: none;">
			<ul>
				<li id="pmDelete"><i class="icon-trash"></i>&nbsp;<span
					class="_label">删除</span></li>
			</ul>
		</div>
		<!--end div-->
		<div class="navbar-inverse">
			<div class="navbar-inner">
				<div class="container">
					<div class="pull-right">
						<button class="btn btn-primary" type="button" id="saveScheme">保存设计</button>
						<!-- <button class="btn btn-danger" type="button" id="clearConnect">清空连接</button> -->
						<button class="btn btn-primary" type="button" id="downScheme">下载案例</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<form role="form" id="execform"
	style="display: none; width: 600px; height: 100px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-4 control-label" for="execBrowser">请选择运行的浏览器</label>
						<div class="col-sm-8" id="browserChecks"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<script type="text/javascript"
	src="{{url('/javascript/plugins/jsplumb/jquery.jsPlumb-1.3.16-all-min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/jquery.contextmenu.r2/jquery.contextmenu.r2.js')}}"></script>
<!--select 2-->
<script type="text/javascript"
	src="{{url('/javascript/plugins/jquery.multiselect2side/jquery.multiselect2side.js')}}"></script>
<!--flowdesign-->
<script type="text/javascript"
	src="{{url('/javascript/plugins/flowdesign/flowdesign.v3.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/sub/browsers.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/autoscheme.js')}}"></script>

<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.core.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.exedit.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/jquery-smartMenu/jquery-smartMenu-min.js')}}"></script>

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
		var height = $(window).height();
		var width = $(window).width();
		$("#flowdesign_canvas").css("height", height - 42);
		AutoSchemeDetailUtil.init();
	});
	</script>
@endsection
