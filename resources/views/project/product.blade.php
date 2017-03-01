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
						<!-- <button class="btn btn-default" type="button" id="save"
							disabled="disabled">新增产品</button>
						<button class="btn btn-default" type="button" id="delete"
							disabled="disabled">删除产品</button> -->
						<button class="btnCommon btn-default" type="button" id="save"
							disabled="disabled">新增产品</button>
						<button class="btnCommon btn-default" type="button" id="delete"
							disabled="disabled">删除产品</button>
					</div>
					<div class="form-group">
						<div id="projectItem" class="nav-uls projectTree"
							style="margin-left: 0px; border: 1px solid #57c7da;">
							<ul id="product" class="ztree"></ul>
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
	src="{{url('/javascript/service/project.js')}}"></script>

<script type="text/javascript">
$(function(){
	ProductUtil.init();
});
</script>
@endsection

