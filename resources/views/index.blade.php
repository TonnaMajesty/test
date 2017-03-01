 @extends('master') @section('mastercontent')
<link rel="stylesheet" href="{{url('css/classical/common.css')}}">
<link rel="stylesheet" href="{{url('css/classical/index.css')}}">
<script
	src="{{url('javascript/plugins/echarts/echarts.common.min.js')}}"></script>

<!--内容区域-->
<!--右侧内容区域-->

<div class="index-content case">
	<div class="list clearfix">
		<div class="title">
			<h3>任务执行情况</h3>
		</div>
		<ol class="clearfix">
			<li>
				<div class="clearfix tip">
					<h4 class="clearfix">Web自动化测试</h4>
					<span id="webTaskPieCount">0</span>
				</div>
				<div id="webTaskPie" style="width: 100%; height: 180px;"></div>
				<ul class="clearfix" id="webState">
					<li class="mission-not"><span></span>未执行<b>0</b></li>
					<li class="mission-ing"><span></span>执行中<b>0</b></li>
					<li class="mission-success"><span></span>执行成功<b>0</b></li>
					<li class="mission-fail"><span></span>执行失败<b>0</b></li>
				</ul>
			</li>
			<li>
				<div class="clearfix tip">
					<h4 class="clearfix">Web自动化测试</h4>
					<span id="webTaskPieCount">0</span>
				</div>
				<div id="webTaskPie" style="width: 100%; height: 180px;"></div>
				<ul class="clearfix" id="webState">
					<li class="mission-not"><span></span>未执行<b>0</b></li>
					<li class="mission-ing"><span></span>执行中<b>0</b></li>
					<li class="mission-success"><span></span>执行成功<b>0</b></li>
					<li class="mission-fail"><span></span>执行失败<b>0</b></li>
				</ul>
			</li>
			<li>
				<div class="clearfix tip">
					<h4 class="clearfix">Web自动化测试</h4>
					<span id="webTaskPieCount">0</span>
				</div>
				<div id="webTaskPie" style="width: 100%; height: 180px;"></div>
				<ul class="clearfix" id="webState">
					<li class="mission-not"><span></span>未执行<b>0</b></li>
					<li class="mission-ing"><span></span>执行中<b>0</b></li>
					<li class="mission-success"><span></span>执行成功<b>0</b></li>
					<li class="mission-fail"><span></span>执行失败<b>0</b></li>
				</ul>
			</li>
			<li>
				<div class="clearfix tip">
					<h4 class="clearfix">Web自动化测试</h4>
					<span id="webTaskPieCount">0</span>
				</div>
				<div id="webTaskPie" style="width: 100%; height: 180px;"></div>
				<ul class="clearfix" id="webState">
					<li class="mission-not"><span></span>未执行<b>0</b></li>
					<li class="mission-ing"><span></span>执行中<b>0</b></li>
					<li class="mission-success"><span></span>执行成功<b>0</b></li>
					<li class="mission-fail"><span></span>执行失败<b>0</b></li>
				</ul>
			</li>
		</ol>
	</div>
	<div class="trend cleafix">
		<div class="title">
			<h3>任务执行走势图</h3>
		</div>
		<ul id="taskExecCycle" class="cleafix"
			style="z-index: 10; position: absolute; right: 0; margin-right: 10px">
			<li cycle="day" class="active">天</li>
			<li cycle="week">周</li>
			<li cycle="month">月</li>
			<li cycle="year">年</li>
		</ul>
		<div class="trend-img" id="taskTrend" style="height: 220px;"></div>
	</div>
	<div class="trend clearfix">
		<div class="title">
			<h3>案例汇总信息</h3>
		</div>
		<ul id="schemeExecCycle" class="cleafix"
			style="z-index: 10; position: absolute; right: 0; margin-right: 10px">
			<li cycle="day" class="active">天</li>
			<li cycle="week">周</li>
			<li cycle="month">月</li>
			<li cycle="year">年</li>
		</ul>
		<div class="trend-img" id="schemeBarLine" style="height: 220px;"></div>
	</div>
	<!-- 
	<div class="case-detail clearfix">
		<div class="case-message">
			<div class="title">
				<h3>案例汇总信息</h3>
			</div>
			<div class="trend-img" id="schemeBar" style="height: 220px;"></div>
		</div>
		<div class="case-trends">
			<div class="title">
				<h3>案例执行走势</h3>
			</div>
			<div class="trend-img" id="schemeLine" style="height: 220px;"></div>
		</div>
	</div>
	 -->
	<div class="script cleafix">
		<div class="title">
			<h3>脚本汇总信息</h3>
		</div>
		<div class="count clearfix">
			<ul class="clearfix ">
				<li class="num"><span id="scriptCount">0</span>脚本数</li>
				<!-- <li class="send-img"><i></i></li>
				<li class="receive-img"><i></i></li>
				<li class="send"><b></b>推送: <span>22</span></li>
				<li class="receive"><b></b>接收: <span>8</span></li> -->
			</ul>
			<!-- <ul class="clearfix">
				<li class="num"><span>0</span>脚本数</li>
				<li class="send-img"><i></i></li>
				<li class="receive-img"><i></i></li>
				<li class="send"><b></b>推送: <span>22</span></li>
				<li class="receive"><b></b>接收: <span>8</span></li>
			</ul>
			<ul>
				<a href="javascript:void(0);" class="button">公共&业务 <span></span></a>
			</ul> -->
		</div>
	</div>
</div>

<!-- 全局js -->
<script src="{{url('javascript/jquery/jquery-2.1.1.min.js')}}"></script>
<!-- tab -->
<script src="{{url('javascript/plugins/contabs/contabs.min.js')}}"></script>
<script src="{{url('javascript/service/index.js')}}"></script>

<script type="text/javascript">
$(function(){
	IndexUtil.init();
})
</script>
@endsection
