<!DOCTYPE html >
<html>
<head>
<title>UpCAT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></meta>
<style type="text/css">
table {
	font-family: verdana, arial, sans-serif;
	font-size: 14px;
	color: #333333;
	border-width: 1px;
	border-color: #666666;
	border-collapse: collapse;
}

th {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #666666;
	background-color: #dedede;
}

td {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #666666;
	background-color: #ffffff;
}
</style>
</head>
<body>
	<p>{{$user["name"]}},您好：</p>
	<p>
		您的任务“{{$rlist["taskName"]}}”已经执行完毕，执行结果：<span style="color: red;">{{$state}}</span>！
	</p>
	<p>
		以下为任务执行情况汇总信息，详细执行步骤信息请进入UpCat查看，<a href="{{$sysUrl}}">点击前往</a>！
	</p>
	<table class="gridtable">
		<tr>
			<th colspan="2">报告标题：{{$rlist["taskName"]}}</th>
			<th colspan="2">开始：{{$rlist["beginTime"]}}</th>
			<th colspan="2">结束：{{$rlist["endTime"]}}</th>
			<th colspan="2">运行时长:{{$rlist["times"]}}</th>
		</tr>
		<!-- <tr>
			<td colspan="8"></td>
		</tr> -->
		<tr>
			<td colspan="2">运行脚本总数：{{$rlist["script"]["sCount"]}}</td>
			<td colspan="2">运行成功脚本数：{{$rlist["script"]["sucSCount"]}}</td>
			<td colspan="2">运行失败脚本数：{{$rlist["script"]["errSCount"]}}</td>
			<td colspan="2">脚本执行成功率：{{$rlist["script"]["sucSPercent"]}}</td>
		</tr>
		@if(!empty($errors))
		<tr>
			<td colspan="2">失败步骤列表：</td>
			<td colspan="2"></td>
			<td colspan="2"></td>
			<td colspan="2"></td>
		</tr>
		@endif @foreach($errors as $error)
		<tr>
			<td colspan="2">{{$error["schemeName"]}}</td>
			<td colspan="2">{{$error["scriptName"]}}</td>
			<td colspan="2">{{$error["optName"]}}</td>
			<td colspan="2">{{$error["msg"]}}</td>
		</tr>
		@endforeach
	</table>
</body>
</html>
