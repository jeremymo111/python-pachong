import urllib.request

url = "https://www.baidu.com"

# url的组成
# https://www.baidu.com/s?tn=39042058_40_oem_dg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#    协议             主机            80(http)/443(https)      s    tn=39042058_40_oem_dg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# http/https       www.baidu.com           端口号             路径          参数                                                          锚点

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36"
}

# 因为urlopen方法中不能存储字典  所以headers不能传递进去
# 请求对象定制
# 注意参数顺序，关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

print(content)
