import requests

res = requests.get("http://test.beautystudio.com.cn/dg_admin_h5/#/login")
print(res.status_code)

res = requests.get("http://test.beautystudio.com.cn/dg_admin_h5/#/login",
                   data={"user": "superadmin", "pass": "20192020buyerbee"})
print(res.encoding)
print(res.headers)
print(res.content)
print(res.cookies)
print(res.text)


