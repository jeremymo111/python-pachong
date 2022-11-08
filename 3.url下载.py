import urllib.request

#
# # 下载网页
url_page = "http://www.baidu.com"
# url_page 表示下载路径，baidu.html 表示文件名字
urllib.request.urlretrieve(url_page, "baidu.html")
#
# # 下载图片
# url_img = "https://tse3-mm.cn.bing.net/th/id/OIP-C.W0t5FV0woDlNBAPVWrxNLwHaLH?w=182&h=273&c=7&r=0&o=5&dpr=1.3&pid=1.7"
# urllib.request.urlretrieve(url_img,"zhixiao.jpg")

# 下载视频
# url_vedio = "https://vd2.bdstatic.com/mda-nhs2af3ecv6kdw5y/sc/cae_h264/1661564631754497290/mda-nhs2af3ecv6kdw5y.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1666965617-0-0-b1ec8b33494d11941457ca02d252eb02&bcevod_channel=searchbox_feed&cd=0&pd=1&pt=3&logid=1817015483&vid=8665642295264125170&abtest=104959_2-104859_1-105227_2&klogid=1817015483"
# urllib.request.urlretrieve(url_vedio,"shiping.mp4")
