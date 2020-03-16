import requests

res = requests.get(url='http://www.baidu.com')

print(res.headers.get("Content-Type"))
print(res.headers.get("Host"))
print(res.headers.get("Referer"))
print(res.headers.get("user-agent"))

# user-agent:能够使服务器识别出用户的操作系统及版本、cpu类型、浏览器类型和版本。很多网站会设置user-agent白名单，只有在白名单范围内的请求才能正常访问
# Referer:有时候服务器还可能会校验Referer，所以还可能需要设置Referer(用来表示此时的请求是从哪个页面链接过来的)

headers = {
    'Host': 'https://blog.csdn.net',
    'Referer': 'https://blog.csdn.net/weixin_43499626/article/details/85875090',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.106 Safari/537.36'
}

response = requests.get("http://www.baidu.com", headers=headers)
print("response:", response.headers)
