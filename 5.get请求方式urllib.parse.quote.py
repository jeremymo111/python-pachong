import urllib.request
import urllib.parse
url = "https://www.baidu.com/s?wd="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36"
}
# 将周杰伦三个字变成unicode
# 我们需要urllib.parse
name = urllib.parse.quote("周杰伦")
url = url + name
# print(url)
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)
