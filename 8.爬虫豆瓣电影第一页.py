import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")
# open方法默认情况下使用gbk的编码，如果我们想要保存汉字 那么需要在open方法中指定编码格式为utf-8
fp = open("douban.json", "w", encoding="utf-8")
fp.write(content)
