import requests
import json
# request get请求 如果需要发送post、put等方式的请求，
# 直接调用就好 例如获得post响应的resp = requests.post("url")
'''
resp = requests.get("http://www.baidu.com")
# 获得响应的类型
print(type(resp))
# 获得响应的状态码
print(resp.status_code)
# 获得响应的内容
print(resp.text)
# 获得响应的cookies
print(resp.cookies)
'''
# 带参数的get请求
#resp = requests.get("https://www.baidu.com/s?wd=cheng")
'''
data = {
    "wd":"cheng"
}
resp = requests.get("http://www.baidu.com",params=data)
# 获得响应的内容
print(resp.text)
# 可以解析json
print(resp.json())
print(json.loads(resp.text))
print(type(resp.text))
'''

# 获取二进制数据（图片/视频）
'''
resp = requests.get("http://img2.imgtn.bdimg.com/it/u=3101924320,584965792&fm=26&gp=0.jpg")
print(type(resp.text),type(resp.content))
print(resp.text)
print(resp.content)

# 写入文件
with open("D:\WorkpaceFile\PythonCrawler\img\image.jpg",'wb') as f:
    f.write(resp.content)
    f.close()
'''
# 添加headers
'''
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
resp = requests.get("https://www.zhihu.com/explore",headers=headers)
print(resp.text)
'''
# post请求
'''
data = {
    'wz': 'cheng'
}
resp = requests.post("https://127.0.0.1:8081/post",data=data)
print(resp.text)
'''
# 响应
'''
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
resp = requests.get("http://www.jianshu.com",headers = headers)
print(type(resp.status_code),resp.status_code)
print(type(resp.headers),resp.headers)
print(type(resp.cookies),resp.cookies)
print(type(resp.url),resp.url)
print(type(resp.history),resp.history)
print(resp.text)
'''

# 状态码判断
'''
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
resp = requests.get("http://www.jianshu.com",headers = headers)
exit() if not resp.status_code == 200 else print("Resquest Successfuly")
'''
# 高级操作

# 文件上传
'''
files = {'file': open('D:\WorkpaceFile\PythonCrawler\img\image.jpg','rb')}
resp = requests.post("https://127.0.0.1:8081/post",files=files)
print(resp.text)
'''

# 获取cookies
'''
resp = requests.get("http://www.baidu.com")
print(resp.cookies)
for key,value in resp.cookies.items():
    print(key +'='+value)
'''
# 会话维持
'''
s = requests.Session()
s.get("http://www.httpbin.org/cookies/set/number/123456789")
resp = requests.get("http://www.httpbin.org/cookies")
print(resp.text)
'''

# 证书验证
'''
resp = requests.get("https://www.12306.cn/index/",verify=False)
print(resp.status_code)
'''
# 代理设置
'''
# http/https
proxies = {
    "http": "http://127.0.0.1",
    "https":"https://127.0.0.1",
    # 假如有用户名和密码
    "http": "http://user:pwd@ip:端口"
}
resp = requests.get("http://www.baidu.com",proxies=proxies)
print(requests.status_codes)

# socks 需要使用pip安装 pip install -U requests[socks]

session = requests.session()
session.proxies = {'http': 'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}
resp = session.get('https://api.github.com', auth=('user', 'pass'))
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.text)
'''
# 超时设置
'''
from requests.exceptions import ReadTimeout
try:
    resp = requests.get("https://github.com",timeout = 0.5)
    print(resp.status_code)
except ReadTimeout:
    print("Timeout")
'''
# 认证设置
'''
from requests.auth import HTTPBasicAuth

r=requests.get("http://localhost:9011/oauth/authorize?client_id=clientapp&redirect_uri=http://localhost:9001/callback&response_type=code&scope=read_userinfo",auth=HTTPBasicAuth('bobo','xyz'))
print(r.status_code)
'''
