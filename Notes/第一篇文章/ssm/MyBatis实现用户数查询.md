# MyBatis实现用户数查询

任务：利用MyBatist框架实现用户数查询
任务分解：
实质：查询记录数
命令：select count(1) as count from smbms_user

一、如何搭建MyBatist环境？
0.创建项目（动态网站项目）
1.下载Jar包
[https://github.com/mybatis/mybatis-3/releases](https://github.com/mybatis/mybatis-3/releases)
mybatis-3.4.5.zip
2.加载Jar包
1)mybatis-3.4.5.jar  2)MySQL-java 驱动jar包（mysql-connector-java-5.1.0-bin.jar）
问题：放到项目的什么位置？  WebContent/WEB-INF/lib
然后在build path中通过add JARs加入上述两个Jar包
3.编写MyBatis核心配置文件（.xml）
1）项目下新建source folder类型的文件夹resources(存放配置文件）
2）从用户手册2.1.2拷贝配置代码 修改如下：
a)加入 <properties resource="database.properties"/>
b)将value="${userName}改为value="${user}”
c)<mapper resource="cn/smbms/dao/user/UserMapper.xml"/>
3）从项目SMBMS_c01_01中拷贝数据库连接参数文件database.properties
4.创建sql映射文件

1. 新建包cn.smbms.dao.user
2）在上述包中新建映射文件UserMapper.xml
2. 从用户手册2.1.5中拷贝代码
4）修改属性 namespace,id,resultType；更新SQL代码
5.编写测试类
加载配置文件，执行映射文件中的sql(代码），显示结果
新建类，新建方法test() 加入如下代码：

```jsx
2. @Test
public void test() {
String resouce="mybatis-config.xml";
InputStream is;
try {
is = Resources.getResourceAsStream(resouce);
SqlSessionFactory factory=new SqlSessionFactoryBuilder().build(is);
int count=0;
SqlSession sqlSession=null;
sqlSession=factory.openSession();
count=sqlSession.selectOne("cn.smbms.dao.user.UserMapper.count");
System.out.println("the count of users is:"+count);
    
    } catch (IOException e) {
    	// TODO Auto-generated catch block
    	e.printStackTrace();
    }
    
    }
```

