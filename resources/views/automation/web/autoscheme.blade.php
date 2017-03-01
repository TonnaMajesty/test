@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/service/sub/browsers.js')}}"></script>
<script src="/javascript/service/sub/report_detail.js"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/autoscheme.js')}}"></script>
<form role="form" id="schemeform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="taskName">案例名称</label>
						<div class="col-sm-10">
							<input class="form-control" id="schemeName" type="text"
								validate="required;len[1:50]" val-name="案例名称" />
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<div class="case task">
	<form target="#">
		<ul class="clearfix">
			<li><label>所属项目</label><select id="search_project"
				class="form-control">
					<option value=""></option> @foreach($projects as $project)
					<option value="{{$project->id}}">{{$project->name}}</option>
					@endforeach
			</select></li>
			<li><label>任务状态</label><select id="search_state" class="form-control">
					<option value="-1"></option>@foreach($states as $state)
					<option value="{{$state['id']}}">{{$state['state']}}</option>
					@endforeach
			</select></li>
			<li><label>案例名称</label><input id="search_schemeName" type="text"></li>
			<li><label>创建人</label><input id="search_creater" type="text"></li>
			<button class="btnCommon" id="search">查询</button>
		</ul>
	</form>
</div>
<div class="row">
	<div class="col-sm-12">
		<div class="ibox float-e-margins">
			<div class="ibox-content">
				<table id="schemelist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
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

<script type="text/javascript">
$(function(){
	AutoSchemeUtil.init();
});
</script>
@endsection

