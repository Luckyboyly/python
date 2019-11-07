import requests
#获得响应

respons = requests.get("http://www.baidu.com")

#输出响应内容
print(respons.text)
#输出响应的状态码
print(respons.status_code)
#输出响应的请求头
print(respons.headers)

#下载图片

img = requests.get("https://ss0.bdstatic.com/9bA1vGfa2gU2pMbfm9GUKT-w/timg?wisealaddin&sec=1573109128&di=ae7c881a139a9999d1227f970f9d05cd&quality=100&size=f242_182&src=http%3A%2F%2Fvdposter.bdstatic.com%2Fbc7f149c5a12b55c0a6fa84feb583d95.jpeg")
print(img.content)
with open('D:\WorkpaceFile\PythonCrawler\img\景甜.gif','wb') as f:
    f.write(img.content)
    f.close()

