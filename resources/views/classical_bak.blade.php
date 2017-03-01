 @extends('master') @section('mastercontent')
<link href="{{url('css/classical/classical.css')}}" rel="stylesheet">
<div id="wrapper">
	<div id="topWrapper"></div>
	<div id="leftWrapper"></div>
	<!--左侧导航结束-->
	<!--右侧部分开始-->
	<div id="page-wrapper" class="gray-bg dashbard-1">
		<div class="row content-tabs">
			<button class="roll-nav roll-left J_tabLeft">
				<i class="fa fa-backward"></i>
			</button>
			<nav class="page-tabs J_menuTabs">
				<div class="page-tabs-content">
					<a href="javascript:;" class="active J_menuTab"
						data-id="index_v1.html">首页</a>
				</div>
			</nav>
			<button class="roll-nav roll-right J_tabRight">
				<i class="fa fa-forward"></i>
			</button>
			<button class="roll-nav roll-right dropdown J_tabClose">
				<span class="dropdown-toggle" data-toggle="dropdown">关闭操作<span
					class="caret"></span></span>
				<ul role="menu" class="dropdown-menu dropdown-menu-right">
					<li class="J_tabShowActive"><a>定位当前选项卡</a></li>
					<li class="divider"></li>
					<li class="J_tabCloseAll"><a>关闭全部选项卡</a></li>
					<li class="J_tabCloseOther"><a>关闭其他选项卡</a></li>
				</ul>
			</button>
			<a href="{{url('/auth/logout')}}"
				class="roll-nav roll-right J_tabExit"><i class="fa fa fa-sign-out"></i>
				退出</a>
		</div>
		<div class="row J_mainContent" id="content-main">
			<iframe class="J_iframe" name="iframe0" width="100%" height="100%"
				src="index_v1.html?v=3.0" frameborder="0" data-id="index_v1.html"
				seamless></iframe>
		</div>
		<div class="footer">
			<div class="pull-right">
				&copy; yonyouup <a href="#" target="_blank">云测平台</a>
			</div>
		</div>
	</div>
	<!--右侧部分结束-->
</div>
<!-- 全局js -->
<script src="{{url('javascript/jquery/jquery-2.1.1.min.js')}}"></script>
<!-- 手风琴插件 -->
<script
	src="{{url('javascript/plugins/metisMenu/jquery.metisMenu.js')}}"></script>
<!-- 滚动条插件 -->
<script
	src="{{url('javascript/plugins/slimscroll/jquery.slimscroll.min.js')}}"></script>
<!-- 自定义js -->
<script src="{{url('javascript/classical/classical.min.js')}}"></script>
<script src="{{url('javascript/plugins/contabs/contabs.min.js')}}"></script>
<!-- 第三方插件  自动加载进度条-->
<!-- <script src="{{url('javascript/plugins/pace/pace.min.js')}}"></script> -->
@endsection
