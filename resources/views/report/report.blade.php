@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/service/sub/report_detail.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/report.js')}}"></script>
<div class="case task">
	<form>
		<ul class="clearfix">
			<li><label>所属项目</label><select id="search_project"
				class="form-control">
					<option value=""></option> @foreach($projects as $project)
					<option value="{{$project->id}}">{{$project->name}}</option>
					@endforeach
			</select></li>
			<li><label>报告类型</label><select id="search_reportType"
				class="form-control">
					<option value=""></option>
					<option value="0">运行案例</option>
					<option value="1">普通任务</option>
					<option value="2">定时任务</option>
			</select></li>
			<li><label>任务状态</label><select id="search_state" class="form-control">
					<option value="-1"></option>@foreach($states as $state)
					<option value="{{$state['id']}}">{{$state['state']}}</option>
					@endforeach
			</select></li>
			<li><label>任务名称</label><input id="search_taskName" type="text"></li>
			<li><label>任务所属人</label><input id="search_creater" type="text"></li>
			<button class="btnCommon" id="search">查询</button>
		</ul>
	</form>
</div>
<div class="row">
	<div class="col-sm-12">
		<div class="ibox float-e-margins">
			<div class="ibox-content">
				<table id="reportlist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
			</div>
		</div>
	</div>
</div>

<script type="text/javascript">
$(function(){
	ReportUtil.init();
});
</script>
@endsection

