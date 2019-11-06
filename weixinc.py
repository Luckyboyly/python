#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing import Pool
import urllib3

from bs4 import BeautifulSoup
import pymysql
import requests
import json
import time
import random
# 禁用安全请求警告
urllib3.disable_warnings()
url = 'http://mp.weixin.qq.com/mp/profile_ext?action=getmsg'#（公众号不让添加主页链接，xxx表示profile_ext)
db = pymysql.connect("localhost","root","123456","hydatabase",charset="utf8")
cursor = db.cursor()    #游标
def get_wx_article(biz, uin, key, wxname, index, count=10):
 offset = (index) * count
 params = {
 '__biz': biz,
 'uin': uin,
 'key': key,
 'offset': offset,
 'count': count,
 'action': 'getmsg',
 'f': 'json'
 }
 headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
 }
 response = requests.get(url=url, params=params, headers=headers)
 resp_json = response.json()
 if resp_json.get('errmsg') == 'ok':
  resp_json = response.json()
 # 是否还有分页数据， 用于判断return的值
  can_msg_continue = resp_json['can_msg_continue']
 # 当前分页文章数
  msg_count = resp_json['msg_count']
  general_msg_list = json.loads(resp_json['general_msg_list'])
  list = general_msg_list.get('list')
  print(list, "**************")
  for i in list:
   # 判断文章类型 49为图文消息 1为纯文字
   if i['comm_msg_info']['type'] == 49 :
    app_msg_ext_info = i['app_msg_ext_info']
    # 判断是否是多图文消息
    is_multi = app_msg_ext_info['is_multi']
    # 标题
    title = app_msg_ext_info['title']
    # 文章地址
    content_url = app_msg_ext_info['content_url']
    # 文章内容
    c_url = content_url
    c_url.replace('amp;', '').replace('#wechat_redirect', '').replace('http', 'https')
    contents = crawl_article_content(c_url)
    # 封面图
    cover = app_msg_ext_info['cover']
    # 发布时间
    datetime = i['comm_msg_info']['datetime']
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime))
    # 作者
    author = app_msg_ext_info['author']
    print(contents)
    sql = "INSERT INTO wechatdb (title,wxname,author,content_url,cover,contents,datetime) VALUES (\""+title+"\", \""+wxname+"\", \""+author+"\", \""+content_url+"\", \""+cover+"\", \""+contents+"\", \""+datetime+"\")"
    try:
     cursor.execute("SELECT content_url FROM wechatdb WHERE content_url = \"" + content_url +"\"")
     # 根据content_url从数据库中判断是否重复,同时判断其是否为空
     if (cursor.fetchone() == None and content_url != ''):
      # 执行sql语句
      cursor.execute(sql)
      # 提交到数据库执行
      db.commit()
    except:
     # 如果发生错误则回滚
     db.rollback()
    if is_multi == 1:
     for j in app_msg_ext_info['multi_app_msg_item_list'] :
      # 标题
      title = j['title']
      # 文章地址
      content_url = j['content_url']
      # 文章内容
      c_url = content_url
      c_url.replace('amp;', '').replace('#wechat_redirect', '').replace('http', 'https')
      contents = crawl_article_content(c_url)
      # 封面图
      cover = j['cover']
      # 作者
      author = j['author']
      print(contents)
      sql = "INSERT INTO wechatdb (title,wxname,author,content_url,cover,contents,datetime) VALUES (\"" + title + "\", \"" + wxname + "\", \"" + author + "\", \"" + content_url + "\", \"" + cover + "\", \"" + contents + "\", \"" + datetime + "\")"
      try:
       cursor.execute("SELECT content_url FROM wechatdb WHERE content_url = \"" + content_url + "\"")
       # 根据content_url从数据库中判断是否重复,同时判断其是否为空
       if (cursor.fetchone() == None and content_url != ''):
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
      except:
       # 如果发生错误则回滚
       db.rollback()
   elif i['comm_msg_info']['type'] == 1 :
    # 文章内容
    contents = i['comm_msg_info']['content']
    # 发布时间
    datetime = i['comm_msg_info']['datetime']
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime))
    sql = "INSERT INTO wechatdb (wxname,contents,datetime) VALUES (\""+wxname+"\",\""+contents+"\", \""+datetime+"\")"
    print(contents)
    try:
     # 执行sql语句
     cursor.execute(sql)
     # 提交到数据库执行
     db.commit()
    except:
     # 如果发生错误则回滚
     db.rollback()
  if can_msg_continue == 1:
   return True
   return False
  else:
   print('获取文章异常...')
   return False

def get_wx_target(biz, uin, key, wxname):
 index = 0
 while 1:
  print(f'开始抓取公众号: { wxname } 第 {index + 1} 页文章.')
  flag = get_wx_article(biz, uin, key, wxname, index=index)
  # 防止和谐，暂停3~6秒
  time.sleep(random.randint(3,6))
  index += 1
  if not flag:
   print('本公众号文章已全部抓取完毕，开始下一个公众号.')
   break
  print(f'..........准备抓取公众号: { wxname } 第 {index + 1} 页文章.')

def crawl_article_content(content_url):
 """抓取文章内容
 :param content_url: 文章地址
 """
 try:
  html = requests.get(content_url, verify=False).text
 except:
  print(content_url)
  return ''
 else:
  bs = BeautifulSoup(html, 'html.parser')
  js_content = bs.find(id='js_content')
  if js_content:
   p_list = js_content.find_all('p')
   content_list = list(map(lambda p: p.text, filter(lambda p: p.text != '', p_list)))
   content = ''.join(content_list)
   return content
if __name__ == '__main__':
 cursor.execute("SELECT biz,uin,wxkey,wxname FROM wechat_target")
 target = cursor.fetchall()
 # 创建进程池，最大个数为5
 p = Pool(5)
 for i in target:
  # 调用apply_async异步执行子进程，传入所需参数
  p.apply_async(get_wx_target, args=(i[0], i[1], i[2], i[3],))
 # 等待所有子进程结束
 p.close()
 p.join()
 db.close()
 print('公众号文章已全部抓取完毕，退出程序.')