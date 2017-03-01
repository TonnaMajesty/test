@extends('app') @section('content')
<link rel="stylesheet"
	href="{{url('/css/plugins/ztree/ztree-app.css')}}" type="text/css">
<link rel="stylesheet" href="{{url('/css/plugins/ztree/ztree.css')}}"
	type="text/css">
<script type="text/javascript"
	src="{{url('/javascript/service/autoscript.js')}}"></script>
<!-- display: none; -->
<form role="form" id="scriptform"
	style="width: 800px; display: none; overflow: hidden;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<div id="scriptInfo">
							<label class="col-sm-2 control-label" for="menuAsc">所属产品</label>
							<div class="col-sm-8">
								<div class="input-group">
									<input type="text" class="form-control" id="product">
									<div class="input-group-btn">
										<button class="btn btn-white " type="button"
											id="productSelect">
											选择 <span class="caret"></span>
										</button>
									</div>
									<!-- <div class="dropdown-menu">
										<ul id="productTree" class="ztree"></ul>
									</div> -->
									<div class="dropdown-menu nav-uls projectTree "
										style="height: 200px; margin-left: 0px; border: 1px solid #57c7da;">
										<ul id="productTree" class="ztree"></ul>
									</div>
								</div>
							</div>
						</div>
						<div id="scriptUploader"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<form role="form" id="annalsform"
	style="width: 800px; display: none; overflow: hidden;">
	<table id="annalslist"
		class="table table-striped table-bordered table-hover dataTables-example"
		cellspacing="0">
		<thead>
		</thead>
	</table>
</form>
<form role="form" id="backLogListform"
	style="display: none; width: 800px;">
	<table id="backLoglist"
		class="table table-striped table-bordered table-hover dataTables-example"
		cellspacing="0">
		<thead>
		</thead>
	</table>
</form>
<form role="form" id="backLogform" style="display: none; width: 500px;">
	<div class="row">
		<div class="ibox float-e-margins">
			<div class="ibox-content">
				<div class="form-group">
					<label class="col-sm-2 control-label" for="backMemo">备注</label>
					<div class="col-sm-10">
						<textarea class="form-control" id="backMemo" rows="3"
							validate="required;len[1:500]" val-name="备注"></textarea>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<div class="case task">
	<form>
		<ul class="clearfix">
			<li><label>脚本名称</label><input id="search_scriptName" type="text"></li>
			<li><label>上传参数</label><select id="search_uploadArgs"
				class="form-control">
					<option value=""></option>
					<option value="0">否</option>
					<option value="1">是</option>
			</select></li>
			<li><label>上传附件</label><select id="search_uploadNeeds"
				class="form-control">
					<option value=""></option>
					<option value="0">否</option>
					<option value="1">是</option>
			</select></li>
			<li><label>创建人</label><input id="search_creater" type="text"></li>
			<button class="btnCommon" id="search">查询</button>
			<div class="script">
				<div class="jiegou">
					<h3>
						项目模块结构<span class="icon active"></span>
					</h3>
				</div>
			</div>
		</ul>
	</form>
	<div id="projectItem" class="nav-uls projectTree">
		<ul id="autoscript" class="ztree"></ul>
	</div>
</div>

<div class="row">
	<div class="col-sm-12">
		<div class="ibox float-e-margins">
			<div class="ibox-content">
				<table id="scriptlist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
			</div>
		</div>
	</div>
</div>

<!-- Diff march patch -->
<script
	src="{{url('/javascript/plugins/diff_match_patch/diff_match_patch.js')}}"></script>
<!-- jQuery pretty text diff -->
<script
	src="{{url('/javascript/plugins/preetyTextDiff/jquery.pretty-text-diff.min.js')}}"></script>

<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.core.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.exedit.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.excheck.js')}}"></script>


<script type="text/javascript">
$(function(){
	AutoScriptUtil.init();
	var height = $(window).height();
	var width = $(window).width();
	$(".frame").css("height", height - 12);
	AutoScriptDetailUtil.init();
});
</script>
@endsection
