#-*-coding:utf-8-*-
import urllib2
import re
import os

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

# open url and return html
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# open html to collect url of images
def getUrl(html):
    reg = r'(?:src|SRC)="?((?:http://)?.+?\.jpg)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return url_lst

# get image with given url
def getImage(url, i):
    # website may reject request once regarded as robot etc
    # add a header to make request like normal from browser
    try:
        file_name = '% s.jpg' % str(i)
        req = urllib2.Request(url,headers=hdr)
        u = urllib2.urlopen(req)
        f = open(file_name, 'wb')
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            f.write(buffer)
        f.close()
        print "Successfully download" + " " + file_name
    except:
        print "Web error"


raw_url = ''

html = getHtml(raw_url)
url_lst = getUrl(html)
index = 0

# create a folder to move dir to that folder
folder_name = 'Downloaded images'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
os.chdir(os.path.join(os.getcwd(), folder_name))

# download the images
for url in url_lst[:]:
    print url
    getImage(url,index)
    index += 1
print "% s" % str(index-1) + " images have been downloaded"
