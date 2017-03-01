@extends('master') @section('mastercontent')
<link href="{{url('/css/plugins/dataTables/dataTables.bootstrap.css')}}"
	rel="stylesheet" type="text/css" />
<link href="{{url('/css/plugins/iCheck/icheck.css')}}" rel="stylesheet"
	type="text/css" />
<link href="{{url('/css/classical/classical.css')}}" rel="stylesheet"
	type="text/css" />
<link rel="stylesheet" href="{{url('css/classical/common.css')}}">
<link rel="stylesheet" href="{{url('css/classical/index.css')}}">
<script type="text/javascript"
	src="{{url('/javascript/plugins/dataTables/jquery.dataTables.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/iCheck/icheck.min.js')}}"></script>
<script type="text/javascript" src="{{url('/javascript/tablelist.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/systemsettings/systemsettings.js')}}"></script>
<div class="formbody form-horizontal">@yield('content')</div>
@endsection
