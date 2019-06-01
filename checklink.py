#抓取頁面下的播放清單網址
import requests
import re
from bs4 import BeautifulSoup
import urllib
params = {
    'el': 'embedded',
    'hl': 'zh_TW',
    'c':' WEB_EMBEDDED_PLAYER',
    'cplayer': 'UNIPLAYER',
    'cbr': 'Chrome',
    'cos':' Windows',
    'authuser':' 0',
    'iframe': '1',
    'embed_config':' {}'
}
playlist =[]
#合輯網址
url = 'https://youtu.be/w_aSA81ej9A'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')
#找出a,包含href
res2= soup.find_all('a')

for i in res2:
    s = i.get('href')
    #列出playlist項目
    if "&index" in s:
        #拼裝成短網址查找音源檔
        url_emb ="https://www.youtube.com/get_video_info?html5=1&video_id="+s[9:20]
        res3 = requests.get(url_emb, params=params)
        a = urllib.unquote(urllib.unquote(res3.text))
        if "---sn-" in a :
            playlist.append(s[9:20])
        else:
            print "not found" ,s[9:20]
#移除重複項
playlist2 = list(set(playlist))              
playlist3 = ','.join(str(k) for k in playlist2)       
print playlist3