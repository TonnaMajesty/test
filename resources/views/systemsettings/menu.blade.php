@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/systemsettings/systemsettings.js')}}"></script>
<form role="form" id="menuform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="parentId">父级菜单</label>
						<div class="col-sm-4">
							<select id="parentId" class="form-control">
								<option value="0">顶级</option> @foreach($menus as $menu)
								<option value="{{$menu->id}}">{{$menu->chrMenuName}}</option>
								@endforeach
							</select>
						</div>
						<label class="col-sm-2 control-label" for="menuAsc">菜单顺序号</label>
						<div class="col-sm-4">
							<input class="form-control" id="menuAsc" type="text"
								validate="required;number" val-name="菜单顺序号" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="menuName">菜单名称</label>
						<div class="col-sm-4">
							<input class="form-control" id="menuName" type="text"
								validate="required;len[2:10]" val-name="菜单名称" />
						</div>
						<label class="col-sm-2 control-label" for="menuArgs">菜单URL</label>
						<div class="col-sm-4">
							<input class="form-control" id="menuArgs" type="text"
								val-name="菜单URL" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="memo">备注</label>
						<div class="col-sm-10">
							<textarea class="form-control" id="memo" rows="3"></textarea>
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
				<table id="menulist"
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
	MenuUtil.init();
});
</script>
@endsection

