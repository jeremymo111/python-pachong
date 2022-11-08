import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

content = response.read().decode()

print(content)

print(type(response))

# 按照一个字节一个字节读取
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)

# 读取一行
# content = response.readline()

# 按行读取
# content = response.readlines()

# 返回状态码   如果是200  那么证明我们的逻辑没有错
# print(response.getcode())

# 返回的是url地址
# print(response.geturl())

# 获取状态信息
# print(response.getheaders())
