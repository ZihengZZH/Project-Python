import urllib2
import re
import os

# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find all pdf files
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

# get the file with given url
def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name

raw_url = 'https://sites.google.com/site/nlpliverpool/home'

html = getHtml(raw_url)
url_lst = getUrl(html)

# The folder should not exist and its name can be modified
os.mkdir('Seminar Slides')
os.chdir(os.path.join(os.getcwd(), 'Seminar Slides'))

for url in url_lst[:]:
    getFile(url)
