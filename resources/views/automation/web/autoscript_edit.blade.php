 @extends('master') @section('mastercontent')
<link href="{{url('/css/plugins/codemirror/codemirror.css')}}"
	rel="stylesheet">
<link rel="stylesheet"
	href="{{url('javascript/plugins/codemirror/addon/fold/foldgutter.css')}}" />
<link rel="stylesheet"
	href="{{url('javascript/plugins/codemirror/addon/dialog/dialog.css')}}">
<link rel="stylesheet"
	href="{{url('javascript/plugins/codemirror/addon/search/matchesonscrollbar.css')}}">
<link rel="stylesheet"
	href="{{url('/css/plugins/codemirror/addon/hint/show-hint.css')}}">

<link href="{{url('/css/plugins/codemirror/theme/eclipse.css')}}"
	rel="stylesheet">
<!-- <link href="{{url('/css/plugins/codemirror/theme/panda-syntax.css')}}"
	rel="stylesheet"> -->

<div>
	<textarea id="scriptCode">{{$scriptcode}}</textarea>
</div>

<!-- CodeMirror -->
<script src="{{url('javascript/plugins/codemirror/codemirror.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/mode/python/python.js')}}"></script>
<!-- 代码折叠 -->
<script
	src="{{url('javascript/plugins/codemirror/addon/fold/foldcode.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/fold/foldgutter.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/fold/indent-fold.js')}}"></script>
<!-- 检索 ctrl+f--enter\替换 ctrl+shift+f--enter -->
<script
	src="{{url('javascript/plugins/codemirror/addon/dialog/dialog.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/search/searchcursor.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/search/search.js')}}"></script>
<!-- 智能提示 -->
<script
	src="{{url('javascript/plugins/codemirror/addon/hint/show-hint.js')}}"></script>
<script
	src="{{url('javascript/plugins/codemirror/addon/hint/anyword-hint.js')}}"></script>
<!-- 代码错误提示--lint(需要自己写python的错误、警告标准 暂不支持) -->
<script>
 var code_editor;
 var old_code;
 $(document).ready(
		 function() {
			 var request=CommonUtil.getRequest();
			 
			 code_editor= CodeMirror.fromTextArea(document
					 .getElementById("scriptCode"), {
						mode: {name: "python", globalVars: true},
						lineNumbers : true,
						matchBrackets : true,
						styleActiveLine : true,
						theme : "eclipse",//panda-syntax 
					    lineWrapping: true,//是否强制换行
					    foldGutter: true,//是否开启折叠
					    extraKeys: {"Ctrl-Q": "autocomplete"},//智能提示
					    gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
					    readOnly : parseInt(request["readonly"])  // 是否只读，默认false
					});
			 old_code=code_editor.getValue();
				});
</script>
@endsection
