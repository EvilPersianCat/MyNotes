# 技术栈

Spring Boot + Thymeleaf + Spring Security + MyBatis-Plus

# 搭建环境

1、pom.xml

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.0.RELEASE</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- 模板此处开始 -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.3.2</version>
    </dependency>

    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-generator</artifactId>
        <version>3.3.2</version>
    </dependency>

    <dependency>
        <groupId>org.apache.velocity</groupId>
        <artifactId>velocity</artifactId>
        <version>1.7</version>
    </dependency>


    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
    </dependency>

    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

2、application.yml

```yaml


spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/smbms?characterEncoding=utf8&useSSL=false&serverTimezone=UTC&rewriteBatchedStatements=true
    username: root
    password: root
mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl

server:
  port: 8383
```

3、代码自动生成

```java
package com.evilpersiancat.common;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.DataSourceConfig;
import com.baomidou.mybatisplus.generator.config.GlobalConfig;
import com.baomidou.mybatisplus.generator.config.PackageConfig;
import com.baomidou.mybatisplus.generator.config.StrategyConfig;
import com.baomidou.mybatisplus.generator.config.po.TableFill;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        //创建对象
        AutoGenerator autoGenerator = new AutoGenerator();
        //数据源
        DataSourceConfig dataSourceConfig = new DataSourceConfig();
        dataSourceConfig.setDbType(DbType.MYSQL);
        dataSourceConfig.setDriverName("com.mysql.cj.jdbc.Driver");
        dataSourceConfig.setUrl("jdbc:mysql://localhost:3306/common");
        dataSourceConfig.setUsername("root");
        dataSourceConfig.setPassword("root");
        autoGenerator.setDataSource(dataSourceConfig);
        //全局配置
        GlobalConfig globalConfig = new GlobalConfig();
        globalConfig.setOutputDir(System.getProperty("user.dir")+"/src/main/java");
        globalConfig.setAuthor("admin");
        globalConfig.setOpen(false);
        //去掉Service的I
        globalConfig.setServiceName("%sService");
        autoGenerator.setGlobalConfig(globalConfig);
        //包配置
        PackageConfig packageConfig = new PackageConfig();
        packageConfig.setParent("com.evilpersiancat.common");
        packageConfig.setEntity("entity");
        packageConfig.setMapper("mapper");
        packageConfig.setService("service");
        packageConfig.setServiceImpl("service.impl");
        packageConfig.setController("controller");
        autoGenerator.setPackageInfo(packageConfig);
        //策略配置
        StrategyConfig strategyConfig = new StrategyConfig();
        strategyConfig.setInclude("sys_user");
        strategyConfig.setNaming(NamingStrategy.underline_to_camel);
        strategyConfig.setColumnNaming(NamingStrategy.underline_to_camel);
        strategyConfig.setEntityLombokModel(true);
        TableFill tableFill = new TableFill("create_time", FieldFill.INSERT);
        TableFill tableFill2 = new TableFill("update_time", FieldFill.INSERT_UPDATE);
        List<TableFill> list = Arrays.asList(tableFill,tableFill2);
        strategyConfig.setTableFillList(list);
        autoGenerator.setStrategy(strategyConfig);
        //启动
        autoGenerator.execute();
    }
}
```

# Spring Security 登录权限认证

1、数据表需要添加权限字段，字段值必须是 ROLE_ 开头

2、pom.xml

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

3、配置类

```java
package com.southwind.configuration;

import com.southwind.service.impl.UserDetailServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.web.access.AccessDeniedHandler;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Configuration
@EnableWebSecurity
public class SecurityConfiguration extends WebSecurityConfigurerAdapter {

    @Autowired
    private UserDetailServiceImpl userDetailService;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(this.userDetailService).passwordEncoder(new MyPasswordEncoder());
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                .antMatchers("/**").access("hasRole('ADMIN')")
                .and()
                .formLogin()
                .loginPage("/login")
                .permitAll()
                .and()
                .logout()
                .permitAll()
                .and()
                .csrf()
                .disable();
        http.exceptionHandling()
                .accessDeniedHandler(new AccessDeniedHandler() {
                    @Override
                    public void handle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, AccessDeniedException e) throws IOException, ServletException {
                        httpServletRequest.setAttribute("authError", true);
                        httpServletRequest.getRequestDispatcher(httpServletRequest.getContextPath()+"/login").forward(httpServletRequest, httpServletResponse);
                    }
                });
    }
}
```

```java
package com.southwind.configuration;

import com.southwind.util.MD5Util;
import org.springframework.security.crypto.password.PasswordEncoder;

public class MyPasswordEncoder implements PasswordEncoder {
    @Override
    public String encode(CharSequence charSequence) {
        return charSequence.toString();
    }

    @Override
    public boolean matches(CharSequence charSequence, String s) {
        return MD5Util.getSaltverifyMD5(charSequence.toString(), s);
    }
}
```

# 解决 bug

1、favicon.ico 异常

```java
@GetMapping("favicon.ico")
@ResponseBody
public void returnNoFavicon(){

}
```

2、iframe 不允许使用

```java
//允许使用iframe
http.headers().frameOptions().sameOrigin();
```

# 添加数据

```html
<a data-toggle="modal" class="btn btn-success" href="/user_list.html#modal-form">
    <i class="fa fa-plus"></i> 新增
</a>
```

```html
<div id="modal-form" class="modal fade" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body">
                <div class="row">
                    <div class="col-sm-12 b-r">
                        <h3 class="m-t-none m-b">添加用户信息</h3>
                        <form class="form-horizontal" action="/user/save" method="post">
                            <div class="form-group">
                                <label class="col-sm-3 control-label">用户名：</label>

                                <div class="col-sm-8">
                                    <input type="text" required name="userName" placeholder="用户名" class="form-control">
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-3 control-label">密码：</label>

                                <div class="col-sm-8">
                                    <input type="password" required name="password" placeholder="密码" class="form-control">
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-3 control-label">昵称：</label>

                                <div class="col-sm-8">
                                    <input type="text" required name="nickName" placeholder="昵称" class="form-control">
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-3 control-label">手机号：</label>

                                <div class="col-sm-8">
                                    <input type="text" required name="mobile" placeholder="手机号" class="form-control">
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-3 control-label">账号类型：</label>

                                <div class="col-sm-8">
                                    <select type="text" name="accountType" placeholder="账号类型" class="form-control">
                                        <option value="1">系统账号</option>
                                        <option value="2">普通账号</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-3 control-label">账号状态：</label>

                                <div class="col-sm-8">
                                    <select type="text" name="accountState" placeholder="账号状态" class="form-control">
                                        <option value="1">启用</option>
                                        <option value="0">冻结</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="col-sm-offset-3 col-sm-8">
                                    <button class="btn btn-sm btn-primary pull-right m-t-n-xs" type="submit"><strong>添 加</strong>
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

时间自动填充 Handler

```java
package com.southwind.handler;

import com.baomidou.mybatisplus.core.handlers.MetaObjectHandler;
import org.apache.ibatis.reflection.MetaObject;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;

@Component
public class FillHandler implements MetaObjectHandler {
    @Override
    public void insertFill(MetaObject metaObject) {
        this.setFieldValByName("createTime", LocalDateTime.now(), metaObject);
        this.setFieldValByName("updateTime", LocalDateTime.now(), metaObject);
    }

    @Override
    public void updateFill(MetaObject metaObject) {
        this.setFieldValByName("updateTime", LocalDateTime.now(), metaObject);
    }
}
```

# 分页

显示

start end total

按钮

pages



共 8 条记录，每页展示 3 条，一共 3 页

page = 1 start = 1 end = 3

page = 2 start = 4 end = 6

page = 3 start = 7 end = 8

start = (page-1)*3+1

end = page*3 = 9



分页 Configuration

```java
package com.southwind.configuration;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class PageConfiguration {

    @Bean
    public PaginationInterceptor paginationInterceptor(){
        return new PaginationInterceptor();
    }
}
```

# 折线图

```java
package com.southwind.controller;


import com.southwind.entity.SysWeather;
import com.southwind.service.SysWeatherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author admin
 * @since 2022-08-26
 */
@RestController
@RequestMapping("/weather")
public class SysWeatherController {

    @Autowired
    private SysWeatherService weatherService;

    @GetMapping("/line")
    public Map<String, List> lineData(){
        List<SysWeather> list = this.weatherService.list();
        List<String> dateList = new ArrayList<>();
        List<Integer> maxList = new ArrayList<>();
        List<Integer> minList = new ArrayList<>();
        for (SysWeather sysWeather : list) {
            dateList.add(sysWeather.getDate());
            maxList.add(sysWeather.getMaxTemperature());
            minList.add(sysWeather.getMinTemperature());
        }
        Map<String,List> map = new HashMap<>();
        map.put("date", dateList);
        map.put("max", maxList);
        map.put("min", minList);
        return map;
    }
}
```

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <title>H+ 后台主题UI框架 - 百度ECHarts</title>
    <meta name="keywords" content="H+后台主题,后台bootstrap框架,会员中心主题,后台HTML,响应式后台">
    <meta name="description" content="H+是一个完全响应式，基于Bootstrap3最新版本开发的扁平化主题，她采用了主流的左右两栏式布局，使用了Html5+CSS3等现代技术">

    <link rel="shortcut icon" href="favicon.ico"> <link href="css/bootstrap.min.css?v=3.3.7" rel="stylesheet">
    <link href="/css/font-awesome.css?v=4.4.0" rel="stylesheet">

    <link href="/css/animate.css" rel="stylesheet">
    <link href="/css/style.css?v=4.1.0" rel="stylesheet">

</head>

<body class="gray-bg">
<div class="wrapper wrapper-content animated fadeInRight">
    <div class="row">
        <div class="col-sm-12">
            <div class="ibox float-e-margins">
                <div class="ibox-title">
                    <h5>折线图</h5>
                    <div class="ibox-tools">
                        <a class="collapse-link">
                            <i class="fa fa-chevron-up"></i>
                        </a>
                        <a class="dropdown-toggle" data-toggle="dropdown" href="graph_flot.html#">
                            <i class="fa fa-wrench"></i>
                        </a>
                        <ul class="dropdown-menu dropdown-user">
                            <li><a href="graph_flot.html#">选项1</a>
                            </li>
                            <li><a href="graph_flot.html#">选项2</a>
                            </li>
                        </ul>
                        <a class="close-link">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                </div>
                <div class="ibox-content">
                    <div class="echarts" id="echarts-line-chart"></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- 全局js -->
<script src="/js/jquery.min.js?v=2.1.4"></script>
<script src="/js/bootstrap.min.js?v=3.3.7"></script>



<!-- ECharts -->
<script src="/js/plugins/echarts/echarts-all.js"></script>

<!-- 自定义js -->
<script src="/js/content.js?v=1.0.0"></script>


<!-- ECharts demo data -->
<script src="/js/demo/echarts-line.js"></script>

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=9051096" charset="UTF-8"></script>
<!--统计代码，可删除-->

</body>

</html>
```

```js
$(function () {
    var lineChart = echarts.init(document.getElementById("echarts-line-chart"));
    $.get('/weather/line',function (data) {
        var lineoption = {
            title : {
                text: '未来一周气温变化'
            },
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:['最高气温','最低气温']
            },
            grid:{
                x:40,
                x2:40,
                y2:24
            },
            calculable : true,
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : data.date
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    axisLabel : {
                        formatter: '{value} °C'
                    }
                }
            ],
            series : [
                {
                    name:'最高气温',
                    type:'line',
                    data:data.max,
                    markPoint : {
                        data : [
                            {type : 'max', name: '最大值'},
                            {type : 'min', name: '最小值'}
                        ]
                    },
                    markLine : {
                        data : [
                            {type : 'average', name: '平均值'}
                        ]
                    }
                },
                {
                    name:'最低气温',
                    type:'line',
                    data:data.min,
                    markLine : {
                        data : [
                            {type : 'average', name : '平均值'}
                        ]
                    }
                }
            ]
        };
        lineChart.setOption(lineoption);
        $(window).resize(lineChart.resize);
    })
});
```

# 饼状图

```java
package com.southwind.controller;


import com.southwind.entity.SysProduct;
import com.southwind.service.SysProductService;
import com.southwind.vo.SysProductVO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author admin
 * @since 2022-08-26
 */
@RestController
@RequestMapping("/product")
public class SysProductController {

    @Autowired
    private SysProductService productService;

    @GetMapping("/pie")
    public Map<String,List> pie(){
        List<SysProduct> list = this.productService.list();
        SysProductVO vo;
        List<SysProductVO> voList = new ArrayList<>();
        List<String> titleList = new ArrayList<>();
        for (SysProduct sysProduct : list) {
            vo = new SysProductVO();
            vo.setName(sysProduct.getName());
            vo.setValue(sysProduct.getSale());
            voList.add(vo);
            titleList.add(sysProduct.getName());
        }
        Map<String,List> map = new HashMap<>();
        map.put("data", voList);
        map.put("title", titleList);
        return map;
    }
}
```

```java
package com.southwind.vo;

import lombok.Data;

@Data
public class SysProductVO {
    private String name;
    private Integer value;
}
```

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <title>H+ 后台主题UI框架 - 百度ECHarts</title>
    <meta name="keywords" content="H+后台主题,后台bootstrap框架,会员中心主题,后台HTML,响应式后台">
    <meta name="description" content="H+是一个完全响应式，基于Bootstrap3最新版本开发的扁平化主题，她采用了主流的左右两栏式布局，使用了Html5+CSS3等现代技术">

    <link rel="shortcut icon" href="favicon.ico"> <link href="css/bootstrap.min.css?v=3.3.7" rel="stylesheet">
    <link href="/css/font-awesome.css?v=4.4.0" rel="stylesheet">

    <link href="/css/animate.css" rel="stylesheet">
    <link href="/css/style.css?v=4.1.0" rel="stylesheet">

</head>

<body class="gray-bg">
<div class="wrapper wrapper-content animated fadeInRight">
    <div class="row">
        <div class="col-sm-12">
            <div class="ibox float-e-margins">
                <div class="ibox-title">
                    <h5>饼状图</h5>
                    <div class="ibox-tools">
                        <a class="collapse-link">
                            <i class="fa fa-chevron-up"></i>
                        </a>
                        <a class="dropdown-toggle" data-toggle="dropdown" href="graph_flot.html#">
                            <i class="fa fa-wrench"></i>
                        </a>
                        <ul class="dropdown-menu dropdown-user">
                            <li><a href="graph_flot.html#">选项1</a>
                            </li>
                            <li><a href="graph_flot.html#">选项2</a>
                            </li>
                        </ul>
                        <a class="close-link">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                </div>
                <div class="ibox-content">
                    <div class="echarts" id="echarts-pie-chart"></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- 全局js -->
<script src="/js/jquery.min.js?v=2.1.4"></script>
<script src="/js/bootstrap.min.js?v=3.3.7"></script>



<!-- ECharts -->
<script src="/js/plugins/echarts/echarts-all.js"></script>

<!-- 自定义js -->
<script src="/js/content.js?v=1.0.0"></script>


<!-- ECharts demo data -->
<script src="/js/demo/echarts-pie.js"></script>

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=9051096" charset="UTF-8"></script>
<!--统计代码，可删除-->

</body>

</html>
```

```js
$(function () {
    var pieChart = echarts.init(document.getElementById("echarts-pie-chart"));
    $.get('/product/pie',function (data) {
        var pieoption = {
            title : {
                text: '商品销量统计',
                subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient : 'vertical',
                x : 'left',
                data:data.title
            },
            calculable : true,
            series : [
                {
                    name:'访问来源',
                    type:'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:data.data
                }
            ]
        };
        pieChart.setOption(pieoption);
        $(window).resize(pieChart.resize);
    });
});
```

# 文件上传

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>easyexcel</artifactId>
    <version>2.2.6</version>
</dependency>
```

```java
@RestController
@RequestMapping("/upload")
public class UploadController {

    @RequestMapping("/importExcel")
    public void importExcel(@RequestParam("file")MultipartFile file){
        try {
            EasyExcel.read(file.getInputStream())
                    .head(ExcelVO.class)
                    .sheet()
                    .registerReadListener(new AnalysisEventListener<ExcelVO>() {
                        @Override
                        public void invoke(ExcelVO excelVO, AnalysisContext analysisContext) {
                            System.out.println(excelVO);
                        }

                        @Override
                        public void doAfterAllAnalysed(AnalysisContext analysisContext) {
                            System.out.println("======文件解析完成======");
                        }
                    }).doRead();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
```

```html
<!DOCTYPE html>
<html>

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <title>H+ 后台主题UI框架 - 文件上传</title>
    <meta name="keywords" content="H+后台主题,后台bootstrap框架,会员中心主题,后台HTML,响应式后台">
    <meta name="description" content="H+是一个完全响应式，基于Bootstrap3最新版本开发的扁平化主题，她采用了主流的左右两栏式布局，使用了Html5+CSS3等现代技术">

    <link rel="shortcut icon" href="/favicon.ico"> <link href="/css/bootstrap.min.css?v=3.3.7" rel="stylesheet">
    <link href="/css/font-awesome.css?v=4.4.0" rel="stylesheet">
    <link href="/css/animate.css" rel="stylesheet">
    <link href="/css/plugins/dropzone/basic.css" rel="stylesheet">
    <link href="/css/plugins/dropzone/dropzone.css" rel="stylesheet">
    <link href="/css/style.css?v=4.1.0" rel="stylesheet">

</head>

<body class="gray-bg">
<div class="wrapper wrapper-content animated fadeIn">
    <div class="row">
        <div class="col-sm-12">
            <div class="ibox float-e-margins">
                <div class="ibox-title">
                    <h5>文件上传</h5>
                    <div class="ibox-tools">
                        <a class="collapse-link">
                            <i class="fa fa-chevron-up"></i>
                        </a>
                        <a class="dropdown-toggle" data-toggle="dropdown" href="/form_file_upload.html#">
                            <i class="fa fa-wrench"></i>
                        </a>
                        <ul class="dropdown-menu dropdown-user">
                            <li><a href="/form_file_upload.html#">选项1</a>
                            </li>
                            <li><a href="/form_file_upload.html#">选项2</a>
                            </li>
                        </ul>
                        <a class="close-link">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                </div>
                <div class="ibox-content">
                    <form id="my-awesome-dropzone" class="dropzone" action="/upload/importExcel">
                        <div class="dropzone-previews"></div>
                    </form>
                </div>
            </div>
        </div>
    </div>

</div>

<!-- 全局js -->
<script src="/js/jquery.min.js?v=2.1.4"></script>
<script src="/js/bootstrap.min.js?v=3.3.7"></script>



<!-- 自定义js -->
<script src="/js/content.js?v=1.0.0"></script>


<!-- DROPZONE -->
<script src="/js/plugins/dropzone/dropzone.js"></script>

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=9051096" charset="UTF-8"></script>
<!--统计代码，可删除-->

</body>

</html>
```