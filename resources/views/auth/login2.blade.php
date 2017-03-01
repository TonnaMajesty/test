<!DOCTYPE html>
<html lang="en">
<head>
<meta name="_token" content="{{ csrf_token() }}" charset="utf-8" />
<meta charset="utf-8">
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<meta name="description" content="">
<meta name="author" content="">

<title>云测- 登录</title>
<link href="{{url('/css/bootstrap/bootstrap.min.css')}}"
	rel="stylesheet">
<link href="{{url('/css/font-awesome.min.css?v=4.3.0')}}"
	rel="stylesheet">
<link href="{{url('/css/style.min.css?v=3.3.0')}}" rel="stylesheet">
<link href="{{url('/css/login.min.css')}}" rel="stylesheet">
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-1.8.2.min.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/common.js')}}"></script>
</head>
<body class="signin">
	<div class="signinpanel">
		<div class="row">
			<div class="col-sm-7">
				<div class="signin-info">
					<div class="logopanel m-b">
						<h1>
							[云测]</span>
						</h1>
					</div>
					<div class="m-b"></div>
					<h4>
						欢迎使用 <strong>云测系统</strong>
					</h4>
					<ul class="m-b">
						<li><i class="fa fa-arrow-circle-o-right m-r-xs"></i> 优势一</li>
						<li><i class="fa fa-arrow-circle-o-right m-r-xs"></i> 优势二</li>
						<li><i class="fa fa-arrow-circle-o-right m-r-xs"></i> 优势三</li>
						<li><i class="fa fa-arrow-circle-o-right m-r-xs"></i> 优势四</li>
						<li><i class="fa fa-arrow-circle-o-right m-r-xs"></i> 优势五</li>
					</ul>
					<strong>还没有账号？ <a href="#">立即注册&raquo;</a></strong>
				</div>
			</div>
			<div class="col-sm-5">
				<h4 class="no-margins">登录：</h4>
				<p class="m-t-md">登录到云测系统</p>
				<form>
					<input id="email" type="text" class="form-control uname text"
						placeholder="用户名" value="zhangfjb@yonyou.com" /> <input
						id="password" type="password" class="form-control pword m-b text"
						placeholder="密码" value="111111" /> <a href="">忘记密码了？</a> <input
						type="button" id="login" class="btn btn-success btn-block"
						value="登录">
				</form>
			</div>
		</div>
		<div class="signup-footer">
			<div class="pull-left">用友优普信息技术有限公司 © yonyou up information
				technology Co., Ltd. 京ICP备05007539号-10</div>
		</div>
	</div>
</body>
<script type="text/javascript">
	$(function(){
			$("#login").on('click',function(){
				var email = $("#email").val();// 去掉左右空字符串
				var pwd = $("#password").val();
				var remember = "";
					if ($("#remember").attr("checked"))
						remember = $("#remember").val();
				var data = {
					"email" : email,
					"password" : pwd,
					"remember" : remember
				};
				CommonUtil.requestService("/auth/login", data, true, "POST", function(data,
						status) {
					if (data.success) {// 成功 重新加载列表
						//alert(data.url);
						CommonUtil.redirect(data.url);
					} else {
					}
				}, function(error) {
				});
			});
			});

</script>
</html>