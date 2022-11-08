
# https://sc.chinaz.com/tupian/index.html
# https://sc.chinaz.com/tupian/index_2.html
import urllib.request
from lxml import etree

def creat_page(page):
    if page == 1:
        url = "https://sc.chinaz.com/tupian/index.html"
    else:
        url = "https://sc.chinaz.com/tupian/index_" + str(page) +".html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Cookie": "PSTM=1640089829; BIDUPSID=B5B15F981ADB94134E9D4F529265ECC6; __yjs_duid=1_52337ea8e8e6aed0139009fd685d57d81640089836743; BAIDUID=4C1DF7E2C95AF32EEC5EF06D29239484:FG=1; sugstore=0; BDUSS=2pqellxc0lXWXFlQ0pIRXZEc0RrMzZHc3pvZEJ4elZPODRCMlJQOGs1WUt6VVpqSVFBQUFBJCQAAAAAAAAAAAEAAAD2~Qz0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApAH2MKQB9jZ; BDUSS_BFESS=2pqellxc0lXWXFlQ0pIRXZEc0RrMzZHc3pvZEJ4elZPODRCMlJQOGs1WUt6VVpqSVFBQUFBJCQAAAAAAAAAAAEAAAD2~Qz0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApAH2MKQB9jZ; BD_UPN=12314753; H_WISE_SIDS=110085_114552_180636_204427_204911_209305_211986_212295_212739_213039_213346_214802_215727_216833_216941_217168_219412_219624_219942_219946_220014_221678_222298_222396_222522_222625_223064_223161_223211_224045_224047_224080_224457_225593_226088_226547_226627_226815_227151_227515_227528_227732_227868_227895_227932_227980_228369_228617_228650_228834_229061_229154_229166_229365_229685_229914_229968_230183_230583_230622_230846_230925_230930_231025_231177_231467_231481_231565_231653_231722_231833_231903_231979_232249_232254_232626_232673_232686_232781_232825_232842_232924_232927_233006_233043_233117_233137_233177_233216_233411; BAIDUID_BFESS=4C1DF7E2C95AF32EEC5EF06D29239484:FG=1; B64_BOT=1; COOKIE_SESSION=4137544_0_8_0_14_9_1_0_8_8_6_1_4137907_0_372_0_1667130268_0_1667129896%7C9%230_0_1667129896%7C1; H_WISE_SIDS_BFESS=110085_114552_180636_204427_204911_209305_211986_212295_212739_213039_213346_214802_215727_216833_216941_217168_219412_219624_219942_219946_220014_221678_222298_222396_222522_222625_223064_223161_223211_224045_224047_224080_224457_225593_226088_226547_226627_226815_227151_227515_227528_227732_227868_227895_227932_227980_228369_228617_228650_228834_229061_229154_229166_229365_229685_229914_229968_230183_230583_230622_230846_230925_230930_231025_231177_231467_231481_231565_231653_231722_231833_231903_231979_232249_232254_232626_232673_232686_232781_232825_232842_232924_232927_233006_233043_233117_233137_233177_233216_233411; baikeVisitId=45747e49-a8e8-4d2c-8d62-d879b43c2b94; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1667048059,1667129900,1667483778; BDRCVFR[BASDVugcKF6]=IdAnGome-nsnWnYPi4WUvY; delPer=0; BD_CK_SAM=1; PSINO=3; BA_HECTOR=20ak008g042h80a40k0k0e1o1hma6341e; ZFY=jZrPTGanCgx1eCAeUfVH70:BYYWPtFiSPWuY6NY:BZrDc:C; BDRCVFR[i-mpQbvDcB_]=mk3SLVN4HKm; H_PS_PSSID=; H_PS_645EC=58f89P6mELA8keK%2FcvxUs2pFQ1wj7Go2CxZj7E45OiqIjv8ZTJc63sWZsLzBULhgi8F5LeEynX9Y; BDORZ=FFFB88E999055A3F8A630C64834BD6D0"
    }

    request = urllib.request.Request(url = url,headers = headers)

    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_data(content):
    # urllib.request.urlretrieve("图片地址","图片名称")
    tree = etree.HTML(content)
    # data_original = tree.xpath("html/body/div[3]/div[2]/div[1]/img/@data-original")
    data_original = tree.xpath('//div[@class="container"]//img/@data-original')
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    # urllib.request.urlretrieve("data_original", "name_list")
    # j=0
    # for i in data_original:
    #     print(i)
    #     j=j+1
    # print(j)
    for i in range(len(name_list)):
        name = name_list[i]
        data = 'https:'+data_original[i]
        urllib.request.urlretrieve(url = data,filename=name + ".jpg")

if __name__ == '__main__':
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page,end_page+1):
        # 请求对象定制
        request = creat_page(page)
        # 获取网页内容
        content = get_content(request)
        # 下载
        down_data(content)
