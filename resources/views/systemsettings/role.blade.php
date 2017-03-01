@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/systemsettings/role.js')}}"></script>
<form role="form" id="roleform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="roleName">角色名称</label>
						<div class="col-sm-10">
							<input class="form-control" id="roleName" type="text"
								validate="required;len[2:20]" val-name="角色名称" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="desc">描述</label>
						<div class="col-sm-10">
							<textarea class="form-control" id="desc" rows="3"></textarea>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</form>

<div class="row">
	<div class="col-sm-12">
		<div class="ibox float-e-margins">
			<div class="ibox-content">
				<table id="rolelist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
			</div>
		</div>
	</div>
</div>


<script type="text/javascript">
$(function(){
	RoleUtil.init();
});
</script>
@endsection

