
<link rel="stylesheet" type="text/css"
	href="{{url('/css/plugins/webuploader/webuploader.css')}}">
<link rel="stylesheet" type="text/css"
	href="{{url('/css/plugins/webuploader/webuploader-app.css')}}">

<div class="ibox-content">
	<div class="page-container">
		<div id="uploader" class="wu-example">
			<div class="statusBar" style="display: none;">
				<div class="progress">
					<span class="text">0%</span> <span class="percentage"></span>
				</div>
				<div class="info"></div>
				<div class="btns">
					<div id="filePicker2"></div>
					<div class="uploadBtn">开始上传</div>
				</div>
			</div>
			<div class="queueList" style="border-top: 2px dashed #e6e6e6;">
				<div id="dndArea" class="placeholder">
					<div id="filePicker"></div>
					<p>支持将文件直接拖拽到此处</p>
				</div>
			</div>
		</div>
	</div>
</div>
<input id="uploaderServer" type="hidden"
	value="{{$args['uploaderServer']}}">
<input id="action" type="hidden" value="{{$args['action']}}">
<input id="optType" type="hidden" value="{{$args['optType']}}">
<input id="finishUploader" type="hidden">
<script type="text/javascript">
            // 添加全局站点信息
            var uploaderServer =CommonUtil.getRootPath()+$("#uploaderServer").val() ;//'http://localhost:8088/testworm/public/auto/web/script/uploader';
            var action=$("#action").val();//"uploadfile";
            var optType=$("#optType").val();
</script>
<script
	src="{{url('/javascript/plugins/webuploader/webuploader.min.js')}}"></script>
<script
	src="{{url('/javascript/plugins/webuploader/webuploader-app.min.js')}}"></script>


