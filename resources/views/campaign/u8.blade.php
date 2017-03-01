@extends('campaign.app') @section('content')
    <!-- time-line ================================================== -->
    <div class="container m-100 u8">
        <h3>U8工具箱</h3>
        <div class="row">
            <div class="col-md-6" style="padding-right: 0;">
                <h4>功能测试工具</h4>
                <div class="col-md-6 ">
                    <!--.common-box.bg1-->
                    <a href="#" class=" common-box bg1">
                        <img src="{{url('images/campaign/u8-1.png')}}"/>
                        <p>（ULT）升级对数工具</p>
                    </a>
                </div>
                <div class="col-md-6 ">
                    <a href="#" class=" common-box bg2">
                        <img src="{{url('images/campaign/u8-2.png')}}"/>
                        <p>（MTT）多语测试工具</p>
                    </a>
                </div>
                <div class="col-md-12">
                    <a href="#" class=" common-box bg3">
                        <img src="{{url('images/campaign/u8-3.png')}}" class="l-80"/>
                        <p>（SETT)软加密测试工具</p>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="#" class=" common-box bg4">
                        <img src="{{url('images/campaign/u8-4.png')}}"/>
                        <p>（(DULT)数据卸载对数工具</p>
                    </a>
                </div>
                <div class="col-md-6  ">
                    <a href="#" class=" common-box bg1">
                        <img src="{{url('images/campaign/u8-5.png')}}"/>
                        <p>（PCT）权限对比工具</p>
                    </a>
                </div>
            </div>
            <div class="col-md-6" style="padding-left: 0;">
                <h4>代码测试工具</h4>
                <div class="col-md-6">
                    <a href="#" class=" common-box bg1 height-2">
                        <img src="{{url('images/campaign/u8-6.png')}}"/>
                        <p>（SCCT）静态代码检查工具</p>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="#" class=" common-box bg2">
                        <img src="{{url('images/campaign/u8-7.png')}}"/>
                        <p>（GDI）内存泄露检查</p>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="#" class=" common-box bg4">
                        <img src="{{url('images/campaign/u8-8.png')}}"/>
                        <p>（RTT）报表测试工具</p>
                    </a>
                </div>
                <div class="col-md-12">
                    <a href="#" class=" common-box bg3">
                        <img src="{{url('images/campaign/u8-9.png')}}" class="l-80"/>
                        <p>（monkey、MAT、APT）移动端检测工具</p>
                    </a>
                </div>
            </div>
        </div>


        <h3>U8集成系统</h3>
        <div class="row">
            <div class="col-md-12">
                <div class="col-md-3">
                    <a href="#" class=" common-box bg2">
                        <img src="{{url('images/campaign/u8-10.png')}}"/>
                        <p>（UEP）体验中心</p>
                    </a>
                </div>
                <div class="col-md-3">
                    <a href="#" class=" common-box bg3">
                        <img src="{{url('images/campaign/u8-11.png')}}"/>
                        <p>（TTS）痕迹跟踪系统</p>
                    </a>
                </div>
                <div class="col-md-3">
                    <a href="#" class=" common-box bg4">
                        <img src="{{url('images/campaign/u8-12.png')}}"/>
                        <p>（WTS）工作任务系统</p>
                    </a>
                </div>
                <div class="col-md-3">
                    <a href="#" class=" common-box bg1">
                        <img src="{{url('images/campaign/u8-13.png')}}"/>
                        <p>（TTS）用例执行工具</p>
                    </a>
                </div>
            </div>
        </div>
    </div>
    <script src="{{url('/javascript/campaign/nav.js')}}" type="text/javascript" charset="utf-8"></script>
    <script src="{{url('/javascript/campaign/main.js')}}" type="text/javascript" charset="utf-8"></script>
@endsection