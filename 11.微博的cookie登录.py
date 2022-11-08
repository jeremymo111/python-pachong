import urllib.request

url = "https://weibo.com/u/5620450623"

headers = {
    "cookie":"SINAGLOBAL=4314429050712.203.1642859228095; ULV=1642859228105:1:1:1:4314429050712.203.1642859228095:; SUB=_2A25OYLh4DeRhGeNI6VIV9S7KyT-IHXVtF66wrDV8PUNbmtANLRTBkW9NSINKwgVHdqUEh8zgvXT2S8EId4EXyn6f; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCTerMo.c_YbXieHsLgGie5JpX5KzhUgL.Fo-ceo5XSK5ceoe2dJLoI7L39PiLdPL_PfYt; ALF=1699085224; SSOLoginState=1667549224; PC_TOKEN=762af9117d",
    "referer": "https://weibo.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

with open("weibo.html", "w", encoding="utf-8") as fp:
    fp.write(content)
