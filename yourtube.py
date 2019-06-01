import requests
import re
from bs4 import BeautifulSoup
import urllib
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
    if request.method == 'POST':   
        if "list=" in request.values['res']:
            url = "https://www.youtube.com/embed/" + request.values['res'][-31:]
            return render_template('video.html',res=url)
        elif "watch?" in request.values['res']: 
            url = "https://www.youtube.com/embed/" + request.values['res'][-11:]
            return render_template('video.html',res=url)
        elif "https://youtu.be/" in request.values['res']:
            url = "https://www.youtube.com/embed/" + request.values['res'][-11:]
            return render_template('video.html',res=url)
        elif "embed" in request.values['res']: 
            url = request.values['res']
            return render_template('video.html',res=url)
            

        

    return render_template('url.html')




if __name__ == '__main__':
    app.run()
    app.debug=True
    #host='0.0.0.0', debug=True
