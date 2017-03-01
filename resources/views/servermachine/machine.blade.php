@extends('app') @section('content')
<script type="text/javascript"
	src="{{url('/javascript/service/machine.js')}}"></script>
<script type="text/javascript"
	src="{{url('/javascript/service/sub/browsers.js')}}"></script>

<form role="form" id="machineform" style="display: none; width: 800px;">
	<div class="row">
		<div class="col-sm-12">
			<div class="ibox float-e-margins">
				<div class="ibox-content">
					<div class="form-group">
						<label class="col-sm-2 control-label" for="machName">机器名称</label>
						<div class="col-sm-4">
							<input class="form-control" id="machName" type="text"
								validate="required;len[2:50]" val-name="机器名称" />
						</div>
						<label class="col-sm-2 control-label" for="ip">机器IP</label>
						<div class="col-sm-4">
							<input class="form-control" id="ip" type="text"
								validate="required;len[7:30]" val-name="机器IP" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="hub">Hub</label>
						<div class="col-sm-4">
							<input class="form-control" id="hub" type="text" val-name="Hub"
								validate="required;len[2:50]" value="/wd/hub" />
						</div>
						<label class="col-sm-2 control-label" for="hubPort">Hub端口</label>
						<div class="col-sm-4">
							<input class="form-control" id="hubPort" type="text"
								validate="required;number" val-name="Hub端口" value="4444" />
						</div>
					</div>
					<div class="form-group">
						<label class="col-sm-2 control-label" for="hubMaxCount">最大Hub数量</label>
						<div class="col-sm-4">
							<input class="form-control" id="hubMaxCount" type="text"
								validate="required;number" val-name="机器IP" value="20" />
						</div>
						<label class="col-sm-2 control-label" for="execBrowser">浏览器类型</label>
						<div class="col-sm-4" id="browserChecks"></div>
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
				<table id="machinelist"
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
	MachineUtil.init();
});
</script>
@endsection

