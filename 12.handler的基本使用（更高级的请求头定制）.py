import urllib.request

url = "http://baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
}

request = urllib.request.Request(url=url, headers=headers)

# handler   bulid_opener   open

# (1)获取handler对象
hanlder = urllib.request.HTTPHandler()

# (2)获取opener对象
opener = urllib.request.build_opener(hanlder)

# (3)调用open方法
response = opener.open(request)

content = response.read().decode("utf-8")

with open("baidu.html", "w", encoding="utf-8") as fp:
    fp.write(content)
