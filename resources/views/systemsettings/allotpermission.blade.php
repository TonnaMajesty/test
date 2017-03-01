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
						<button class="btnCommon btn-default" type="button" id="save">保存</button>
					</div>
					<div class="form-group">
						<div class="col-sm-5">
							角色
							<div id="projectItem" class="nav-uls projectTree"
								style="margin-left: 0px; border: 1px solid #57c7da;">
								<ul id="role" class="ztree"></ul>
							</div>
						</div>
						<div class="col-sm-5">
							<ul id="myTab" class="nav nav-tabs">
								<li class="active" href="#funcPerm"><a>功能权限</a></li>
								<li href="#dataPerm"><a>数据权限</a></li>
							</ul>
							<div id="permItem" class="nav-uls projectTree tab-content"
								style="margin-left: 0px; border: 1px solid #57c7da;">
								<div id="funcPerm">
									<ul id="permissions" class="ztree"></ul>
								</div>
								<div id="dataPerm" style="display: none;">
									<ul id="dataPermissions" class="ztree"></ul>
								</div>
							</div>
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
	src="{{url('/javascript/plugins/ztree/jquery.ztree.excheck.js')}}"></script>

<script type="text/javascript"
	src="{{url('/javascript/systemsettings/allotright.js')}}"></script>

<script type="text/javascript">
$(function(){
	AllotRightUtil.init();
});
</script>
@endsection

