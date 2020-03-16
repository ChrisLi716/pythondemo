import requests
from http import cookiejar
from urllib import request

import os

# res = requests.get("https://blog.csdn.net/weixin_43499626")
# print(res.text)

# 向服务器发送一个post请求并携带相关参数，将服务器返回的cookie保存在本地,
# cookie是服务器在客户端上的“监视器”，记录了登录信息等。客户端通过识别请求携带的cookie，确定是否登录
res = requests.post("https://passport.csdn.net/login?code=public",
                    data={"username": "lilunlogic@163.com", "passwd": "Lilun299792458+"})
for key, value in res.cookies.items():
    print('key = ', key + ' ||| value :' + value)


# 构建一个cookie的处理器
def build_save_cookie():
    """
    MozillaCookieJar ： cookiejar的子类
    从FileCookieJar派生而来，创建与Mozilla浏览器
    cookies.txt兼容的FileCookieJar实例。
    """
    cookie = cookiejar.MozillaCookieJar(os.curdir + os.sep + 'cookie.txt')
    # 构建一个cookie的处理器
    handler = request.HTTPCookieProcessor(cookie)
    # 获取一个opener对象
    opener = request.build_opener(handler)
    #  获取一个请求对象
    req = request.Request('http://flights.ctrip.com/', headers={"Connection": "keep-alive"})
    # 请求服务器，获取响应对象, cookie会在response里一起响应
    response = opener.open(req)
    print(response)
    # 保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)


# build_save_cookie()

def request_with_cookie():
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(os.curdir + os.sep + 'cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req = request.Request('http://flights.ctrip.com/')
    html = opener.open(req).read().decode('gbk')
    print(html)


request_with_cookie()
