import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    #req.add_header()
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    #正则表达式筛选出图片地址
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)

    for each in imglist:
        print (each)

    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)
'''
        response = urllib.request.urlopen(each)
        img = response.read()

        with open('filename.jpg','wb') as f:
            f.write(img)
'''
        
if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/3785167072?see_lz=1"
    get_img(open_url(url)) 
