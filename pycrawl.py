
# coding=utf-8
import urllib
import hashlib
import http.client
import http.cookiejar
import http.cookies


#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'http://www.gradms.sdu.edu.cn/bsuims/bsMainFrameInit.do' #从提交数据包中分析出，处理post请求的url

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功，当然有的网站也不对此做要求，那就省去这一步）
h = urllib.request.urlopen('http://www.gradms.sdu.edu.cn/')

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。

headers = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': ' zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
            #  'Accept-Encoding': 'gzip, deflate',#大坑。加入后要手动对gzip解压后才会有可识别的内容
            'Referer': 'http://xxxxx/userlogin.jsp?reason=login',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',}
            #构造Post数据，也是从抓大的包里分析得出的。

postData = {'login_strLoginName': 'MjAxNzM0ODc2',
            'login_strPassword': 'Zm9yZXZlcjIxODE=',           #你的密码，密码可能是明文传输也可能是密文，如果是密文需要调用相应的加密算法加密,需查看js代码                                                   #才知我就直接硬编码了
             'save_cookie': 'none'
}

#需要给Post数据编码
postData = urllib.parse.urlencode(postData).encode(encoding='UTF-8')

#通过urllib.request提供的Request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib.request.Request(posturl, postData, headers)
response = urllib.request.urlopen(request)
text = response.read()

#测试是否成功登陆，这里是请求用户信息，如果成功登陆，那么cookie发到这个页面之后就会返回用户资料，否则提示错误，也知道自己登陆失败了
headers1 = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': ' zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
            #  'Accept-Encoding': 'gzip, deflate',#大坑。加入后要手动对gzip解压后才会有可识别的内容
            'Referer': 'http://xxxx.edu.cn/ntms/userLogin.jsp?reason=logout',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Content-Type': '    application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
}
request = urllib.request.Request('http://www.gradms.sdu.edu.cn/bsuims/bsMainFrameTopReload.do?contextName=gradmsTopPage&leftMenuUrl=/bsuims/bsMainFrameLeftMenuReload.do&leftMenuModel=bsUimsLeftMenuPage&workBenchUrl=/bsuims/formViewPageInit.do?contextName=bsSystemUserNotifyPage', None, headers1)
response = urllib.request.urlopen(request)
text = response.read()
#打印回应的内容
print(str(text, encoding='utf-8', errors='strict'))
