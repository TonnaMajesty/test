@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/service/project.js')}}"></script>
<form role="form" id="projectform" style="display: none; width: 600px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="projectName">项目名称</label>
						<div class="col-sm-10">
							<input class="form-control" id="projectName" type="text"
								validate="required;len[2:10]" val-name="项目名称" />
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
				<table id="projectlist"
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
	ProjectUtil.init();
});
</script>
@endsection

