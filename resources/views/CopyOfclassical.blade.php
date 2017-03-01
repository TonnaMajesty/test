@extends('app') @section('content')
<link href="{{url('/css/classical/classical.css')}}" rel="stylesheet"
	type="text/css" />
<script type="text/javascript"
	src="{{url('/javascript/classical/classical.js')}}"></script>
<div id="os_classical">
	<div id="topFrame" name="topFrame" class="topFrame">
		<div class="topleft">
			<a href="#" target="_parent"><img src="" alt="系统首页" title="系统首页" /></a>
		</div>
		<ul class="nav">
		</ul>
		<div class="topright">
			<ul>
				<li><a id="osetting" href="#"><img src="" title="切换主题"
						class="helpimg" /><span>切换主题</span></a></li>
				<li><a href="#">关于</a></li>
				<li><a href="{{url('/auth/logout')}}" target="_parent" onclick="">退出</a></li>
			</ul>
			<div class="user">
				<span>{{$username}}</span>
			</div>
		</div>
	</div>
	<div id="leftFrame" name="leftFrame" class="leftFrame"></div>
	<div id="rightFrame" name="rightFrame" class="rightFrame">
		<!-- http://localhost:8088/laravel2/ https://www.baidu.com/-->
		<!-- frameborder 内嵌帧边框 是否显示边缘；填”1″表示”是”，填”0″表示”否”
		marginwidth：帧内文本的左右页边距
		marginheight：帧内文本的上下页边距
		allowtransparency：是否允许透明 -->
	</div>
</div>
@endsection

