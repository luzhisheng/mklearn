# 一、mitmproxy
https://mitmproxy.org/
https://docs.mitmproxy.org/stable/
## liunx安装：
* sudo apt install mitmproxy
* pip install mitmproxy
* mitmproxy --version
* mitmdump --version
* mitmweb --version
* mitmproxy:linux抓包 
* mitmweb:图形键面（linux/windows抓包可用）
* mitmdump:python交互

liunx启动：mitmproxy
* mitmproxy默认监听8080端口，设置一下SwitchyOmega插件
* 证书安装：http:mitm.it ,将证书放到受信任颁发机构里面去
* 上下键 ---- 控制查看那条记录
* 回车 ----- 查看详情
* tab键 ----- 选项卡
* esc+q ----- 返回抓包流键面

### mitmproxy命令
* 端口设置 mitmproxy -p 8889
* 下载文件：mitmdump -w 路径
* 清除数据包：z

### mitmproxy过滤
过滤命令行：输入f
```bash
~c 200
~d baidu.com
~m post & ~u baidu
```
断点拦截命令行:输入i
```bash
~m get & ~u baidu -》浏览器请求-》回车选择数据包-》request-》e修改数据包（d删除）-》q返回数据包列表-》a重新访问
~m get & ~u baidu -》浏览器请求-》回车选择数据包-》respone-》e修改数据包-》wq保存返回数据包列表-》a重新访问
```
过滤规则：https://blog.csdn.net/hqzxsc2006/article/details/73201581

### mitmdump
* 端口设置 mitmdump -p 8889
* 启动python脚本 mitmdump -p 8887 -s test.py
```bash
from mitmproxy import ctx

def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.error(str(flow.request.url))
    ctx.log.error(str(flow.request.host))
    ctx.log.error(str(flow.request.method))
    ctx.log.error(str(flow.request.path))

def response(flow):
    ctx.log.error(str(flow.response.status_code))
    ctx.log.error(str(flow.response.text))
```
### 手机抓包
1. 手机连接pc电脑无线网络
2. 手机高级选项
3. 代理手动
4. 设置代理服务器主机名
5. 设置代理服务器端口（mitmproxy的端口号）
6. 手机浏览器访问--》http:mitm.it--》下载证书
7. 访问网站，完成

### CA证书的安装

要捕获https证书，就得解决证书认证的问题，因此需要在通信发生的客户端安装证书，并且设置为受信任的根证书颁布机构。下面介绍6种客户端的安装方法。

　　当我们初次运行mitmproxy或mitmdump时，

　　会在当前目录下生成 ~/.mitmproxy文件夹，其中该文件下包含4个文件，这就是我们要的证书了。

　　mitmproxy-ca.pem 私钥
　　mitmproxy-ca-cert.pem 非windows平台使用
　　mitmproxy-ca-cert.p12 windows上使用
　　mitmproxy-ca-cert.cer 与mitmproxy-ca-cert.pem相同，android上使用

Firefox上安装
preferences-Advanced-Encryption-View Certificates-Import (mitmproxy-ca-cert.pem)-trust this CA to identify web sites

chrome上安装
设置-高级设置-HTTPS/SSL-管理证书-受信任的根证书颁发机构-导入mitmproxy-ca-cert.pem

osx上安装
双击mitmproxy-ca-cert.pem - always trust

windows7上安装
双击mitmproxy-ca-cert.p12-next-next-将所有的证书放入下列存储-受信任的根证书发布机构

iOS上安装
将mitmproxy-ca-cert.pem发送到iphone邮箱里，通过浏览器访问/邮件附件

Android上安装
将mitmproxy-ca-cert.cer 放到sdcard根目录下选择设置-安全和隐私-从存储设备安装证书

## windows安装：
https://mitmproxy.org/ .exe文件直接安装

# 二、手机抓包工具 packet capture
https://sj.qq.com/myapp/detail.htm?apkName=app.greyshirts.sslcapture

更多详情：
* https://www.jianshu.com/p/ecf1b2d5e8cd
* https://www.jianshu.com/p/ae4d433597ce

# 三、appium
* appium是一个自动化测试开源工具，支持ios平台和android平台的原生应用，web应用和混合应用
* appium就封装了标准的selenium客户端类库
* appium client --》server --》移动设备
* 服务端下载：http://appium.io/
* linux客户端安装： pip install appium
* simple：host port
* advanced：高级选项
* presets：预设选项卡

# 四、docker 命令
* docker images -a 列出所有镜像
* docker ps -a 列出所有容器
* docker irm 镜像 删除镜像
* docker rm 容器 删除容器
* docker run -it 镜像名称或者id /bin/bash 登录进入容器，并且开启一个伪终端，启动式交互

# 五、fiddler
## file
* capture traffic 启动抓包
* new viewer 打开新的窗口
* load archive 加载我们的抓包文件
* save 保存文件
* recent archive 加载最近的抓包文件
* import session 导入sessions文件
* export session 导出sessions文件

## edit
* coap 拷贝文件
* remove 删除文件
* select all 选择所有
* paste as sessions 粘贴一个sessions
* mark 标记颜色，划线等
* unlock for editing 解锁数据包，进行编辑
* find sessions 查找数据包

## tools
* options 软件的设置
* wininet options windows设置
* clear wininet cache 清除浏览器缓存
* clear wininet cookies 清除浏览器cookies
* textwizad 编码转换工具
* hosts host管理工具类似于windows host文件，dns解析关系

## rules
1. hide image requests 隐藏图片数据
2. hide connects 隐藏其他
3. automatic breakpoints 自动打断点
* 请求之前拦截 befere requests
* 请求之后拦截 after responses
* disabled 关闭
4. require proxy authentication 设置代理的认证
5. performmance 性能测试 选择第一个包---》按住shift---》最后一个包

## 工具栏
* 汽包框：注释
* replay：流重放
* go：手动执行流
* stream：流模式
* decode：解析数据包
* keep：加载的数据包
* any prcoess：抓取哪个进程
* find：查找
* save：保存
* 📷：截图
* clear cache:清除缓存
* textwizard：字符串转换，编码、解码

## 会话列表
* resuit http状态码
* protocol 请求使用的协议，如http，https，ftp
* host 请求地址的主机名
* url 请求资源的位置
* body 该请求的大小
* caching 请求的缓存过期时间或者缓存控制值
* content-type 请求响应的类型
* process 发送此请求的进程：进程id
* comments 允许用户为此会话添加备注
* custom 允许用户设置自定义值

## http请求头：
* get 请求方法
* host 请求的主机
* connection: 连接类型
* upgrade-insecur-requests：可以处理的http协议
* user-agent：代表我们目前用的浏览器版本
* accept:响应的类型
* accept-encoding：响应内容的编码
* accept-language：响应内容的语言

## http响应头：
* http：http响应的类型
* data：服务器日期
* server：服务器的版本
* content-type：响应的类型
* pragma：是否使用缓存
* cache-control：是否使用缓存
* expires：过期时间
* set-cookie：响应归来的cookie
* content-language：响应归来的语言
* connection: 连接类型
* content-length:响应头的大小
* 最后就是响应体内容

## 断点设置
1、通过图形界面设置断点（不推荐），会拦截到所有的请求，命令状态栏：可以指定拦截某个域名

![Image text](./readme_img/duandian1.png)

rulos --》automatic breakpoints --》请求拦截 befere requests --》可以编辑请求头 --》run to comp

rulos --》automatic breakpoints --》响应拦截 after responses --》choose response --》run to comp

2、命令行设置断点可以细化到某个域名的断点
命令状态栏：可以指定拦截某个域名

请求拦截：bpu 域名（www.baidu.com）--》webforms等信息修改 --》break on resp --》run to comp

清除请求拦截：bpu

响应拦截：bpafter 域名（www.baidu.com）--》choose response --》run to comp

清除响应拦截：bpa

3、通过fiddle设置网页的重定向
![Image text](./readme_img/cdx.png)

## 手机抓包
1. 手机连接pc电脑无线网络
2. 手机高级选项
3. 代理手动
4. 设置代理服务器主机名
5. 设置代理服务器端口（fiddler的端口号）
6. fiddle-->options->connections-->allow remote computers connect(勾选)
7. 手机浏览器访问--》主机ip:端口--》下载证书
8. 访问网站，完成
