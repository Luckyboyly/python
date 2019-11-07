import urllib.request
import urllib.parse
import socket
import  urllib.error
import http.cookiejar
from  urllib import request
from urllib.parse import urlencode

#get请求
'''
resp = urllib.request.urlopen("http://www.baidu.com")
# read().decode('utf-8') 读取数据 并改成utf-8的格式
print(resp.read().decode('utf-8'))
'''

#post请求
'''
data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding="utf-8")
resp = urllib.request.urlopen("http://www.httpbin.org/post",data=data)
print(resp.read())
'''

#超时
'''
try:
    resp = urllib.request.urlopen("http://www.baidu.com",timeout=0.1)
    print(resp.read().decode("utf-8"))
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT")
'''
#响应内容，响应类型,状态码，响应头,响应服务器
'''
resp = urllib.request.urlopen("http://www.baidu.com")
# read().decode('utf-8') 读取数据 并改成utf-8的格式
print(resp.read().decode('utf-8'))
print(type(resp))
print(resp.status)
print(resp.getheaders())
print(resp.getheader('Server')) #可以带参数获得header具体某个参数的值
'''
#使用request携带请求头
'''
url = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Host": "www.baidu.com"
}
#构建一个带请求头的请求
req = request.Request(url=url,headers=headers)
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
'''
'Handler'
#代理
'''
proxy_handler = urllib.request.ProxyHandler({
    "http":"http://127.0.0.1"
    "https":"https://127.0.0.1
})
opener = urllib.request.build_opener(proxy_handler)
resp = opener.open("http://www.baidu.com")
print(resp.read())
'''
#Cookie
'''
cookeie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookeie)
opener = urllib.request.build_opener(handler)
request = opener.open("http://www.baidu.com")
for item in cookeie:
    print(item.name+"="+item.value)
'''
#urlencode:将字典转换成get参数
params = {
    "name":"cheng",
    "age":19
}
base_url = "http://www.baidu.com?"
url = base_url+urlencode(params)
print(url)
