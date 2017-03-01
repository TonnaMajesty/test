@extends('app') @section('content')
<link rel="stylesheet"
	href="{{url('/css/plugins/ztree/ztree-app.css')}}" type="text/css">
<link rel="stylesheet" href="{{url('/css/plugins/ztree/ztree.css')}}"
	type="text/css">
<script type="text/javascript"
	src="{{url('/javascript/systemsettings/user.js')}}"></script>
<form role="form" id="userform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="userCode">员工编号</label>
						<div class="col-sm-4">
							<input class="form-control" id="userCode" type="text"
								validate="required;len[2:20]" val-name="员工编号" />
						</div>
						<label class="col-sm-2 control-label" for="userName">员工名称</label>
						<div class="col-sm-4">
							<input class="form-control" id="userName" type="text"
								validate="required;len[2:20]" val-name="员工名称" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="email">邮箱</label>
						<div class="col-sm-4">
							<input class="form-control" id="email" type="text"
								validate="required;email" val-name="邮箱" />
						</div>
						<label class="col-sm-2 control-label" for="tel">手机号</label>
						<div class="col-sm-4">
							<input class="form-control" id="tel" type="text"
								validate="required;tel" val-name="手机号" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="orgId">所属组织/部门</label>
						<div class="col-sm-4">
							<select id="orgId" class="form-control"> @foreach($orgs as $org)
								<option value="{{$org->id}}">{{$org->name}}</option> @endforeach
							</select>
						</div>
						<div name="pwd">
							<label class="col-sm-2 control-label" for="pwd">初始密码</label>
							<div class="col-sm-4">
								<input class="form-control" id="pwd" type="password"
									validate="required;len[6:60]" val-name="初始密码" />
							</div>
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="roleName">角色</label>
						<div class="col-sm-4">
							<div class="jiegou">
								<h3>
									<input class="form-control" id="roleName" type="text"
										validate="required" val-name="角色" />
								</h3>
							</div>
							<div id="projectItem" class="nav-uls projectTree"
								style="display: none; margin-left: 0px; border: 1px solid #57c7da;">
								<ul id="role" class="ztree"></ul>
							</div>
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
				<table id="userlist"
					class="table table-striped table-bordered table-hover dataTables-example"
					cellspacing="0">
					<thead>
					</thead>
				</table>
			</div>
		</div>
	</div>
</div>



<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.core.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.exedit.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/plugins/ztree/jquery.ztree.excheck.js')}}"></script>

<script type="text/javascript">
$(function(){
	EmployeeUtil.init();
});
</script>
@endsection

