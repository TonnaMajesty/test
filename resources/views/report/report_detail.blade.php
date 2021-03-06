@extends('master') @section('mastercontent')
<link href="{{url('/css/classical/classical.css')}}" rel="stylesheet"
	type="text/css" />
<link rel="stylesheet" href="{{url('css/classical/common.css')}}">
<link rel="stylesheet" href="{{url('css/classical/index.css')}}">
<input type="hidden" id="taskType" value="{{$taskType}}">
<input type="hidden" id="keyId" value="{{$keyId}}">
<div class="formbody form-horizontal">
	<div class="tabs-container popup-content">
		<div class="tab clearfix">
			<ul class="clearfix">
				<li class="cur"><a data-toggle="tab" href="#tab-func"
					aria-expanded="true">功能测试结果</a></li>
				<!-- <li><a href="javascript:void(0);">功能测试结果</a></li>
				<li><a href="javascript:void(0);">性能测试结果</a></li> -->
			</ul>
		</div>
		<div class="tab-content">
			<div id="tab-func" class="tab-pane active">
				<div class="panel-body">
					@if(!empty($step))
					<div class="interface">
						<h2>操作界面</h2>
						<div class="carousel slide" id="carousel">
							<div class="carousel-inner" id="carousel_content">
								<div class="item active" id="carousel_item" stepItem="1">
									<img alt="image" class="img-responsive mignifier"
										src="{{$step->chrImage}}">
								</div>
							</div>
							<a id="prev" class="left carousel-control"> <span
								class="icon-prev"></span></a> <a id="next"
								class="right carousel-control"> <span class="icon-next"></span>
							</a>
						</div>
						<h2>操作结果详细说明</h2>
						<div id="stepDetail" stepItem="1">
							<div class="explain clearfix">
								<h6>执行命令</h6>
								<p>{{$step->chrDescription}}【{{$step->chrCmd}}】</p>
							</div>
							<div class="explain clearfix">
								<h6>耗时</h6>
								<p>{{$step->fltDuring}}</p>
							</div>
							<div class="explain clearfix">
								<h6>参数</h6>
								<p>{{$step->chrCmdParam}}</p>
							</div>
							<div class="explain clearfix">
								<h6>错误详情</h6>
								<p>{{$step->chrErrorMessage}}</p>
							</div>
						</div>
					</div>

					<div class="step">
						<ul class="clearfix tabs">
							<li class="cur" href="#step_all"><span></span>完整步骤</li>
							<li href="#step_fail"><span></span>失败步骤</li>
						</ul>
						<div class="detail" style="height: 480px; overflow: auto;">
							<div class="list" id="tab-step">
								<ul id="step_all">
									<li class="o focus" stepItem="1"><span></span>步骤{{$step->intOrderNo}}：{{$step->chrDescription}}</li>
								</ul>
								<ul id="step_fail" style="display: none;">
								</ul>
							</div>
						</div>
					</div>

					@else
					<div>尚未产生报告明细</div>
					@endif
				</div>
			</div>
		</div>
		<!-- <div id="tab-perf" class="tab-pane">
			<div class="panel-body">
				<div class="ibox float-e-margins">
					<div class="ibox-content"></div>
				</div>
			</div>
		</div>
		<div id="tab-time" class="tab-pane">
			<div class="panel-body">
				<div class="ibox float-e-margins">
					<div class="ibox-content"></div>
				</div>
			</div>
		</div>
		<div id="tab-log" class="tab-pane">
			<div class="panel-body">
				<div class="ibox float-e-margins">
					<div class="ibox-content"></div>
				</div>
			</div>
		</div> -->
	</div>
</div>
</div>
<script type="text/javascript"
	src="{{url('/javascript/service/autoreport.js')}}"></script>
<script type="text/javascript">
$(function(){
	AutoReportUtil.init();
});
</script>
@endsection
