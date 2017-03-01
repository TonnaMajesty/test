<!DOCTYPE html >
<html>
<head>
<title>UpCAT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></meta>
<meta name="_token" content="{{ csrf_token() }}" charset="utf-8" />
<link href="{{url('/css/bootstrap/bootstrap.min.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{url('/css/font-awesome.min.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/animate.min.css')}}" rel="stylesheet"
	type="text/css" />
<!-- jquery-1.8.2.min.js -->
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-1.8.2.min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/jquery/jquery-ui-1.8.24.custom.min.js')}}"></script>
</head>
<body class="fixed-sidebar full-height-layout pace-done fixed-nav">
	@yield('mastercontent')
</body>
<script src="{{url('javascript/bootstrap/bootstrap.min.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/layer/layer.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/common.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/validate.js')}}"></script>
</html>
