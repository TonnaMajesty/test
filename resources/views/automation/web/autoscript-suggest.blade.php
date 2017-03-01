@extends('app') @section('content')
<link rel="stylesheet"
	href="{{url('/css/plugins/ztree/ztree-app.css')}}" type="text/css">
<link rel="stylesheet" href="{{url('/css/plugins/ztree/ztree.css')}}"
	type="text/css">
<script type="text/javascript"
	src="{{url('/javascript/service/autoscript.js')}}"></script>
<!-- style="display: none; width: 600px;" -->
<form role="form" id="menuform">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="menuAsc">所属产品</label>
						<div class="col-sm-4">
							<div class="input-group">
								<input type="text" class="form-control" id="product">
								<div class="input-group-btn">
									<button type="button" class="btn btn-white dropdown-toggle"
										data-toggle="dropdown">
										<span class="caret"></span>
									</button>
									<ul class="dropdown-menu dropdown-menu-right" role="menu">
									</ul>
								</div>
							</div>
						</div>
						<label class="col-sm-2 control-label">脚本类型</label>
						<div class="col-sm-4">
							<div class="radio i-checks">
								<label> <input type="radio" value="1" name="scriptType"> <i></i>
									公共脚本
								</label> <label> <input type="radio" checked="" value="2"
									name="scriptType"> <i></i> 业务脚本
								</label>
							</div>
						</div>
					</div>
					<div class="form-group">
						<div id="uploader"></div>
						<div class="pull-right">
							<button class="btn btn-primary" type="button" id="uploaderNext">下一步</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>
<div class="frame">
	<div class="leftFrame">
		<ul id="autoscript" class="ztree"></ul>
	</div>
	<div class="rightFrame">
		<div class="row">
			<div class="col-sm-12">
				<div class="ibox float-e-margins">
					<div class="ibox-content">
						<table id="scriptlist"
							class="table table-striped table-bordered table-hover dataTables-example"
							cellspacing="0">
							<thead>
							</thead>
						</table>
					</div>
				</div>

			</div>
		</div>
	</div>
</div>



<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.core.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.exedit.js')}}"></script>
<script
	src="{{url('/javascript/plugins/suggest/bootstrap-suggest.min.js')}}"></script>

<script type="text/javascript">
$(function(){
	AutoScriptUtil.init();
	var height = $(window).height();
	var width = $(window).width();
	$(".frame").css("height", height - 12);
});
</script>
@endsection
