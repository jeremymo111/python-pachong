# 多个参数的时候
import urllib.request
import urllib.parse

base_url = "https://baidu.com/s?"

data = {
    "wd": "周杰伦",
    "sex": "男",
    "loction": "中国台湾省"
}

new_code = urllib.parse.urlencode(data)
# print(new_code)

url = base_url + new_code

# print(url)
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
}
request = urllib.request.Request(url = url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)


