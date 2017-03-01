@extends('app') @section('content')
<link href="{{url('/css/plugins/codemirror/codemirror.css')}}"
	rel="stylesheet">
<link rel=stylesheet
	href="{{url('css/plugins/codemirror/addon/merge/merge.css')}}">

<link href="{{url('/css/plugins/codemirror/theme/eclipse.css')}}"
	rel="stylesheet">
<input type="hidden" id="original" value="{{$original}}">
<input type="hidden" id="changed" value="{{$changed}}">
<input type="hidden" id="originalVer" value="{{$originalVer}}">
<input type="hidden" id="changedVer" value="{{$changedVer}}">
<div class="well">
	<div class="diff-wrapper">
		<div id="view"></div>
	</div>
</div>
<!-- CodeMirror -->
<script src="{{url('javascript/plugins/codemirror/codemirror.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/mode/python/python.js')}}"></script>
<!-- Diff march patch -->
<script
	src="{{url('/javascript/plugins/diff_match_patch/diff_match_patch.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/merge/merge.js')}}"></script>

<script type="text/javascript">
$(function(){
	original =$("#original").val();
	changed = $("#changed").val();
	var target=document.getElementById("view"); 
	target.innerHTML=""; 
	mid=CodeMirror.MergeView(target, {
		  mode:  {name: "python", globalVars: true},
		  value: changed,
		  origLeft: null,
		  orig: original,
		  lineNumbers: true,
		  highlightDifferences: true,
		  connect: null,
		  collapseIdentical: false,
		  readOnly:true,
		  mergeHtml:{"defaults":"现文件"+$("#originalVer").val(),"right":"将要回滚的文件"+$("#changedVer").val()}
	  });
	  var height=$(window).height();
	  //$(".CodeMirror-merge").height(height);
	  //var s=mid.getLine(2);
});
</script>
@endsection
