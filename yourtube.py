# ecoding:UTF-8 
import requests
import re
from bs4 import BeautifulSoup
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def url():
    params = {
    'el': 'embedded',
    'hl': 'zh_TW',
    'c':' WEB_EMBEDDED_PLAYER',
    'cplayer': 'UNIPLAYER',
    'cbr': 'Chrome',
    'cos':' Windows',
    'authuser':' 0',
    'iframe': '1',
    'embed_config':'{}'
    }
    playlist =[]
#    try:
    if request.method == 'POST':   
        if "list" in request.values['res']: 
            n= request.values['res'].find("&list")            
            url = "https://youtu.be/"+ request.values['res'][n-12:n-1] + "?" + request.values['res'][n:n+18]
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
                    a = urllib.parse.unquote(urllib.parse.unquote(res3.text))
                    if "---sn-" in a :
                        playlist.append(s[9:20])
                #移除重複項
                playlist2 = list(set(playlist))              
                playlist3 = ','.join(str(k) for k in playlist2)      
                url = "https://www.youtube.com/embed/VIDEO_ID?playlist=" + playlist3
            return render_template('video.html',res=url)   
        elif "watch?" in request.values['res']: 
            n= request.values['res'].find("watch?v")
            url = "https://www.youtube.com/embed/" + request.values['res'][n+8:n+19]
            return render_template('video.html',res=url)
        elif "https://youtu.be/" in request.values['res']:
            n= request.values['res'].find(".be/")
            url = "https://www.youtube.com/embed/" + request.values['res'][n+4:n+15]
            return render_template('video.html',res=url)
        elif "embed" in request.values['res']: 
            url = request.values['res']
            return render_template('video.html',res=url)
#    except:
#        return render_template('url.html')

    return render_template('url.html')




if __name__ == '__main__':
    app.run()    
    #host='0.0.0.0', debug=True
