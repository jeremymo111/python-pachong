from lxml import etree

# xpath
# 解析本地文件：etree.parse("文件名")
# 解析服务器相应文件：etree.HTML(response.reade().decode("utf-8"))

tree = etree.parse("15.1解析.html")

# 查找ul下面的li    text()---获取标签中的内容
# li_list = tree.xpath("//ur/li/text()")

# 查找所有有id属性的标签
# li_list = tree.xpath("//ur/li[@id]/text()")

# 查找id为l1的li标签  注意引号
# li_list = tree.xpath('//ur/li[@id="l1"]/text()')

# 查找到id为l1的li标签的class的属性值
# li_list = tree.xpath('//ur/li[@id="l1"]/@class')

# 查询id中包含l的li标签
# li_list = tree.xpath("//ur/li[contains(@id,'l')]/text()")

# 查询id的值以l开头的li标签
li_list = tree.xpath("//ur/li[starts-with(@id,'c')]/text()")
print(li_list)