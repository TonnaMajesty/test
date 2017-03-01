@extends('app') @section('content')
<link href="/css/plugins/clockpicker/clockpicker.css" rel="stylesheet">
<link href="/css/plugins/datapicker/datepicker.css" rel="stylesheet">
<form role="form" id="titaskform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="titaskName">任务名称</label>
						<div class="col-sm-4">
							<input class="form-control" id="titaskName" type="text"
								validate="required;len[1:50]" val-name="任务名称" />
						</div>
						<label class="col-sm-2 control-label" for="titaskType">任务类型</label>
						<div class="col-sm-4">
							<select id="titaskType" class="form-control">
								<option value="0"></option> @foreach($tasktypes as $tasktype)
								<option value="{{$tasktype->id}}">{{$tasktype->chrDictValue}}</option>
								@endforeach
							</select>
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="execRate">执行频率</label>
						<div class="col-sm-4">
							<select id="execRate" class="form-control">
								<option value="0"></option> @foreach($rates as $rates)
								<option value="{{$rates->id}}">{{$rates->chrDictValue}}</option>
								@endforeach
							</select>
						</div>
						<label class="col-sm-2 control-label">执行时间</label>
						<div class="col-sm-4">
							<div class="input-group clockpicker" data-autoclose="true">
								<input type="text" class="form-control" value="09:30"
									id="execTime"> <span class="input-group-addon"> <span
									class="fa fa-clock-o"></span>
								</span>
							</div>
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="execDateTime">执行日期范围</label>
						<div class="col-sm-4" id="execDateTime">
							<div class="input-daterange input-group">
								<input type="text" class="input-sm form-control" name="start"
									id="execBeginDate" validate="required;len[1:30]" /> <span
									class="input-group-addon">到</span> <input type="text"
									class="input-sm form-control" name="end" id="execEndDate"
									validate="required;len[1:30]" />
							</div>
						</div>
						<label class="col-sm-2 control-label" for="execBrowser">选择运行的浏览器</label>
						<div class="col-sm-4" id="browserChecks"></div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="emailReceivers">邮件接收人</label>
						<div class="col-sm-10">
							<input id="emailReceivers" type="text" placeholder="邮件之间通过;隔开"
								class="form-control">
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label">选择任务</label>
						<div class="col-sm-7">
							<table id="tasklist"
								class="table table-striped table-bordered table-hover dataTables-example"
								cellspacing="0">
								<thead>
								</thead>
							</table>
						</div>
						<div class="col-sm-3">
							<div class="panel panel-success">
								<div class="panel-heading">已选择任务</div>
								<div class="panel-body" id="checkedTask"></div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<div class="case task">
	<form>
		<ul class="clearfix">
			<li><label>所属项目</label><select id="search_project"
				class="form-control">
					<option value=""></option> @foreach($projects as $project)
					<option value="{{$project->id}}">{{$project->name}}</option>
					@endforeach
			</select></li>
			<li><label>任务类型</label><select id="search_testType"
				class="form-control">
					<option value=""></option> @foreach($tasktypes as $tasktype)
					<option value="{{$tasktype->id}}">{{$tasktype->chrDictValue}}</option>
					@endforeach
			</select></li>
			<li><label>任务状态</label><select id="search_state" class="form-control">
					<option value=""></option>@foreach($states as $state)
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
				<table id="titasklist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
			</div>
		</div>
	</div>
</div>
<!-- Clock picker -->
<script src="/javascript/plugins/clockpicker/clockpicker.js"></script>
<!-- Data picker -->
<script src="/javascript/plugins/datapicker/bootstrap-datepicker.js"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/sub/browsers.js')}}"></script>

<script src="/javascript/service/sub/report_detail.js"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/timertask.js')}}"></script>

<script type="text/javascript">
$(function(){
	TimerTaskUtil.init();
});
</script>
@endsection

