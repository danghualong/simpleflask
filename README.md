如何部署到IIS?
1.在系统环境变量中增加 WORKON_HOME键，其值设置为venv
2.pipenv shell 创建虚拟环境变量
3.pipenv install 安装依赖包
4.创建web.config（其中scriptProcessor的设置因项目而已)
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
        <system.webServer>
            <handlers>
            <add name="FlaskFastCGI" path="*" verb="*" modules="FastCgiModule" scriptProcessor="d:\codekarta\python\flask\simpleflask\venv\simpleflask-04vq_sfr\scripts\python.exe|d:\codekarta\python\flask\simpleflask\venv\simpleflask-04vq_sfr\lib\site-packages\wfastcgi.py" resourceType="Unspecified" requireAccess="Script" />
            </handlers>
            <security> 
                <!-- URL 重写中的特殊字符，比如加号+等等 -->
                <requestFiltering allowDoubleEscaping="true"></requestFiltering> 
            </security> 
        </system.webServer>
        <appSettings>
            <!-- 此处为wsgi模块中的Flask对象 -->
            <add key="WSGI_HANDLER" value="wsgi.app" />
            <add key="PYTHONPATH" value="~/" />
            <!-- Optional settings -->
            <!-- 需要先创建日志目录，否则报错 -->
            <!-- 如果访问其他目录，需要开启目录访问权限 -->
            <!-- <add key="WSGI_LOG" value="C:\\web.log" /> -->
        </appSettings>
    </configuration>

5.IIS启用CGI
6.IIS中配置FastCGI应用程序
  如:d:\codekarta\python\flask\simpleflask\venv\simpleflask-04vq_sfr\scripts\wfastcgi-enable.exe
7.IIS中把当前项目添加为网站，并启动服务即可。
  


