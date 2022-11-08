# 使用urllib来获取百度首页的源码
import urllib.request

# 定义一个url  就是要访问的网站地址
url = "http://www.baidu.com/"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应中的页面源代码
# read方法  返回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串类型
# 二进制→字符串  解码  decode("编码格式")
content = response.read().decode("utf-8")

# 打印数据
print(content)