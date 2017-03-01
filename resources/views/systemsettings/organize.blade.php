@extends('app') @section('content')
<link rel="stylesheet"
	href="{{url('/css/plugins/ztree/ztree-app.css')}}" type="text/css">
<link rel="stylesheet" href="{{url('/css/plugins/ztree/ztree.css')}}"
	type="text/css">

<form role="form">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<button class="btnCommon btn-default" type="button" id="save">新增机构</button>
						<button class="btnCommon btn-default" type="button" id="delete">删除机构</button>
					</div>
					<div class="form-group">
						<div id="projectItem" class="nav-uls projectTree"
							style="margin-left: 0px; border: 1px solid #57c7da;">
							<ul id="org" class="ztree"></ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>

<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.core.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.exedit.js')}}"></script>

<script type="text/javascript"
	src="{{url('/javascript/systemsettings/organize.js')}}"></script>

<script type="text/javascript">
$(function(){
	OrganizeUtil.init();
});
</script>
@endsection

