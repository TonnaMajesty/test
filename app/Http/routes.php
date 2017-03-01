<?php

/*
 * |-------------------------------------------------------------------------- | Application Routes |-------------------------------------------------------------------------- | | Here is where you can register all of the routes for an application. | It's a breeze. Simply tell Laravel the URIs it should respond to | and give it the controller to call when that URI is requested. |
 */
Route::controllers ( [ 
		'auth' => 'Auth\AuthController', // 认证登录
		'password' => 'Auth\PasswordController'  // 重置密码
] );
Route::get ( "/", "Auth\AuthController@getIndex" ); // Index
Route::group(['prefix'=>'camp'],function(){
    Route::get('/webtest',"Campaign\WebController@index");
    Route::get('/apptest',"Campaign\AppController@index");
    Route::get('/u8',"Campaign\U8Controller@index");
});
Route::get ( '/verify/image', 'Verify\VerifyController@index' ); // 图片验证码
                                                                 
// 管理中心
Route::group ( [ 
		'middleware' => 'auth' 
], function () {
	// 管理中心框架布局
	Route::group ( [ 
			'prefix' => 'desktop' 
	], function () {
		// 个人桌面
		Route::get ( "", "DesktopController@index" ); // 个人桌面
		Route::get ( "/deskmenus", "DesktopController@getDesktopMenus" ); // 获取桌面菜单（包括上导航，左导航，桌面菜单）信息
		Route::get ( "/menus", "DesktopController@getMenus" );
		// 登录
		Route::get ( "/index", "IndexController@index" );
		Route::group ( [ 
				'prefix' => 'index' 
		], function () {
			Route::get ( "/taskpie", "IndexController@getTaskPies" ); // 报告绘图统计
			Route::get ( "/taskline", "IndexController@getTaskLines" ); // 报告绘图统计
			Route::get ( "/scheme", "IndexController@getSchemeChart" ); // 报告绘图统计
			Route::get ( "/script", "IndexController@getScriptChart" ); // 报告绘图统计
		} );
	} );
	// 系统设置
	Route::group ( [ 
			'prefix' => 'sys',
			'namespace' => 'SystemSettings' 
	], function () {
		Route::post ( "osetting", "UserController@updateUserOSDisplay" ); // 系统设置
		Route::get ( "menu/list", "MenuController@getList" ); // 项目管理
		Route::resource ( "menu", "MenuController" ); // 项目管理
		
		Route::get ( "org/tree", "OrganizeController@getOrgTree" ); // 组织机构树
		Route::resource ( "org", "OrganizeController" ); // 组织机构
		
		Route::get ( "role/list", "RoleController@getList" ); // 角色管理
		Route::get ( "role/tree", "RoleController@getRoleTree" ); // 角色管理
		Route::resource ( "role", "RoleController" ); // 角色管理
		
		Route::get ( "user/list", "UserController@getList" ); // 员工管理
		Route::resource ( "user", "UserController" ); // 员工管理
		
		Route::get ( "allotright/list", "AllotPermissionController@getList" ); // 分配权限
		Route::resource ( "allotright", "AllotPermissionController" ); // 分配权限
		
		Route::get ( "right/tree", "PermissionController@getRightTree" ); // 功能权限树
		Route::get ( "right/dtree", "PermissionController@getDataRightTree" ); // 数据权限树
		Route::resource ( "right", "PermissionController" ); // 权限管理
	} );
	
	Route::group ( [ 
			'prefix' => 'mytask',
			'namespace' => 'MyTask' 
	], function () {
		Route::resource ( "timer/list", "TimerTaskController@getTimerTaskList" ); // 定时任务管理
		Route::resource ( "timer", "TimerTaskController" ); // 定时任务管理
	} );
	Route::group ( [ 
			'prefix' => 'pc',
			'namespace' => 'ServerMachine' 
	], function () {
		Route::get ( "machine/list", "MachineController@getMachineList" ); // 机器列表
		Route::resource ( "machine", "MachineController" ); // 机器管理
	} );
	Route::group ( [ 
			'prefix' => 'report',
			'namespace' => 'Report' 
	], function () {
		Route::get ( "bill/list", "ReportController@getReportList" ); // 报告列表
		Route::resource ( "bill", "ReportController" ); // 报告
	} );
	// 自动化
	Route::group ( [ 
			'prefix' => 'auto',
			'namespace' => 'Automation' 
	], function () {
		Route::resource ( 'browser', 'AutoBrowserController' );
		Route::resource ( "report", "AutoExecReportController" ); // 执行任务报告
		Route::group ( [ 
				'prefix' => 'web',
				'namespace' => 'Web' 
		], function () {
			// 脚本仓库
			Route::group ( [ 
					'prefix' => 'script' 
			], function () {
				Route::any ( 'uploader', 'AutoScriptController@uploader' );
				Route::get ( "tree", "AutoScriptController@getScriptTree" ); // 产品自动化脚本树结构
				Route::get ( "list", "AutoScriptController@getScriptList" ); // 产品自动化脚本列表
				Route::get ( "annalslist", "AutoScriptController@getAnnalsScriptList" ); // 历史脚本列表
				Route::get ( "backloglist", "AutoScriptController@getBackLogList" ); // 回滚日志列表
				Route::get ( "scriptdiff", "AutoScriptController@getScriptText" ); // 脚本内容
				Route::post ( "rollback", "AutoScriptController@rollBack" ); // 脚本内容
				Route::post ( "params", "AutoScriptController@storeParams" ); // 存储脚本的参数化文件
				Route::post ( "images", "AutoScriptController@storeImages" ); // 存储脚本所需图片
			} );
			Route::resource ( 'script', 'AutoScriptController' );
			// 脚本案例
			Route::group ( [ 
					'prefix' => 'scheme' 
			], function () {
				Route::get ( "list", "AutoSchemeController@getSchemeList" ); // 产品自动化案例列表
				Route::get ( "flowprocess/{id}", "AutoSchemeController@getFlowProcess" ); // 流程设计
				Route::get ( "addflow", "AutoSchemeController@addFlow" ); // 添加流程
				Route::post ( "addprocess", "AutoSchemeController@addProcess" ); // 添加流程步骤
				Route::post ( "delprocess", "AutoSchemeController@delProcess" ); // 删除流程步骤
				Route::post ( "saveflowprocess/{id}", "AutoSchemeController@saveFlowProcess" ); // 保存流程步骤面板的所有信息
				Route::get ( "download/{id}", "AutoSchemeController@downScheme" ); // 保存流程步骤面板的所有信息
				Route::get ( "exec/{id}", "AutoSchemeController@exec" ); // 案例执行
			} );
			Route::resource ( 'scheme', 'AutoSchemeController' );
			
			// 案例任务
			Route::group ( [ 
					'prefix' => 'task' 
			], function () {
				Route::get ( "list", "AutoTaskController@getTaskList" ); // 产品自动化案例列表
				Route::resource ( "exec", "AutoTaskExecController" ); // 执行任务
			} );
			Route::resource ( 'task', 'AutoTaskController' );
		} );
	} );
	// 项目管理
	Route::group ( [ 
			'prefix' => 'project',
			'namespace' => 'Project' 
	], function () {
		Route::get ( "bill/list", "ProjectController@getList" ); // 项目管理
		Route::resource ( "bill", "ProjectController" ); // 项目管理
		Route::get ( "product/tree", "ProductController@getProductTree" ); // 产品结构
		Route::resource ( "product", "ProductController" ); // 产品结构
	} );
} );

Route::group ( [ 
		'prefix' => 'ext',
		'namespace' => 'ExtServices' 
], function () {
	Route::post ( "/log", "AutoLogController@store" );
} );
