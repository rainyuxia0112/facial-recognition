import requests
from bs4 import BeautifulSoup
#step 1 get the image from website
dataurl = 'https://www.google.com.tw/search?ei=MswPXJnSDMaT8wWwoozQDA&yv=3&q={}&tbm=isch&vet=10ahUKEwiZs6TsgJjfAhXGybwKHTARA8oQuT0IMigB.MswPXJnSDMaT8wWwoozQDA.i&ved=0ahUKEwiZs6TsgJjfAhXGybwKHTARA8oQuT0IMigB&ijn=1&start={}&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
import os
os.mkdir('idol_eminem/')
os.mkdir('idol_justin_bieber/')   # build the dir for a new file

def getimage(name, dstpath):
    """
    :param name: the person we want to get the image
    :param dstpath: the directory to the file where we put the image
    :return: file
    """
    for i in range(5):
        res = requests.get(dataurl.format(name, i * 100))
        soup = BeautifulSoup(res.text, 'lxml')
        for ele in soup.select('img'):
            imgurl = ele.get('src')
            fname  = imgurl.split('tbn:')[1]
            with open(dstpath + fname + '.jpg', 'wb') as f:
                res2 = requests.get(imgurl)
                f.write(res2.content)
getimage('eminem','idol_eminem/')
getimage('justin bieber','idol_justin_bieber/')