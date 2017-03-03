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
	@if(!empty($task_list))
	<table class="task">
	<tr>
			<th colspan="2">任务名称</th>
			<th colspan="2">所属项目</th>
			<th colspan="2">创建人</th>
			<th colspan="2">任务状态</th>
            <th colspan="2">浏览器</th>
            <th colspan="2">执行完毕时间</th>
		</tr>
	@foreach($task_list as $task)
		<tr>
			<td colspan="2">{{$task["chrTaskName"]}}</td>
			<td colspan="2">{{$task["chrProjectName"]}}</td>
			<td colspan="2">{{$task["chrUserName"]}}</td>
			<td colspan="2">{{$task["state"]}}</td>
			<td colspan="2">{{$task["chrBrowserNames"]}}</td>
			<td colspan="2">{{$task["updated_at"]}}</td>
		</tr>
	@endforeach
	</table>
	@endif

	@if(!empty($scheme_list))
	<table class="scheme">
	<tr>
            <th colspan="2">任务名称</th>
            <th colspan="2">案例名称</th>
            <th colspan="2">所属项目</th>
            <th colspan="2">创建人</th>
            <th colspan="2">执行状态</th>
            <th colspan="2">浏览器</th>
		</tr>
	@foreach($scheme_list as $scheme)
		<tr>
			<td colspan="2">{{$scheme["chrTaskName"]}}</td>
			<td colspan="2">{{$scheme["schemeName"]}}</td>
			<td colspan="2">{{$scheme["projectName"]}}</td>
			<td colspan="2">{{$scheme["createUser"]}}</td>
			<td colspan="2">{{$scheme["state"]}}</td>
			<td colspan="2">{{$scheme["browserNames"]}}</td>
		</tr>
	@endforeach
	</table>
	@endif

	@if(!empty($scheme_list))
	<table class="script_sum">
	<tr>
            <th colspan="4">事件</th>
            <th colspan="4">次数</th>
            <th colspan="4">成功率</th>
		</tr>
	@foreach($script_sum as $val)
		<tr>
			<td colspan="2">{{$val["chrDescription"]}}</td>
			<td colspan="2">{{$val["count"]}}</td>
			<td colspan="2">{{$val["passlv"]}} %</td>
		</tr>
	@endforeach
	</table>
	@endif
</body>
</html>
