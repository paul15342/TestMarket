# -*- encoding=utf-8 -*-
import sys
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )
url = "http://www.qiushibaike.com/hot/"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"
headers = {"User-Agent":user_agent}
html = urllib2.Request(url,headers=headers)
resposn = urllib2.urlopen(html)
HTML = resposn.read()
soup = BeautifulSoup(HTML,"html.parser")
text = open(r"D:\DeskTop\test.txt", "w+")
for strings in soup.strings:
    text.write(strings)

# for strings in soup.stripped_strings :
#     print strings
# print re.findall('src="https:.*?"',strings)
# print HTML
res = r'<script type="text/javascript" src="(.*?)"></script>'
r =re.findall(res,HTML)
for i in range(len(r)):
    urllib.urlretrieve(r[i], "D://DeskTop//test.txt")



