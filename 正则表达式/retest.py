import re
# re.match :尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.match(pattern,String,flags=0)
# pattern:匹配的正则表达式,String:要匹配的字符串。flags:标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''
content = "Hello 123 452 Word_this this is a Demo!!"
print(content)
# 全匹配
result = re.match('^[A-Z][a-z]{4}\s\d{3}\s\d{3}\s\w{9}.*$',content)
print(result)
print(result.group())
print(result.span())
'''
# 获取匹配目标 加一个括号 添加一个组
'''
content = "Hello 123452 Word_this this is a Demo!!"
result = re.match('^[A-Z][a-z]{4}\s(\d+)\s\w{9}.*$',content)
print(result)
print(result.group(1))
print(result.span())
'''
#贪婪匹配 .* 尽可能多的匹配字符
'''
content = "Hello 123452 Word_this this is a Demo!!"
result = re.match('^He.*(\d+).*$',content)
print(result)
print(result.group(1))
print(result.span())
'''
#非贪婪匹配 .*？ 尽可能少的匹配字符
'''
content = "Hello 123452 Word_this this is a Demo!!"
result = re.match('^He.*?(\d+).*$',content)
print(result)
print(result.group(1))
print(result.span())
'''
# 匹配模式 尽量使用泛匹配、使用括号得到匹配目标、尽量使用非贪婪模式、有换行符就用re.S
'''
content = ''Hello 123452 Word_this this is a Demo!! is a Pegex Demo
''
result = re.match('^He.*?(\d+).*?$',content,re.S)
print(result)
print(result.group(1))
print(result.span())
'''
# 转义 "\"来对关键字符进行转换
'''
content = 'pice is $5.00'
result = re.match('^pi.*?\$\d\.00$',content)
print(result)
print(result.group())
print(result.span())
'''

# re.search 扫描整个字符串并返回第一个成功的匹配
'''
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
'''
#27：56