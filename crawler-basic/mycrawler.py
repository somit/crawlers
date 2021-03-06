from pattern.web import URL,DOM
from crawlerclass import link
import re,os,sys

def generateUrl(root ,baseurl, href):
  if re.search(r'^/',href):
	return root+href
  if href.startswith("http://") or href.startswith("www."):
	return ""  
  s = baseurl.split('/')
  s = baseurl.replace("/"+s.pop(),"/")
  return s+"href"

dict = {}
brokenUrls = {}
visited = {}

rootUrl = 'http://winzip.com/win/en/index.htm'
baseUrl = 'http://winzip.com'
dict[rootUrl] = link(baseUrl,0, rootUrl)

def browse(browseUrlObject):
    browseUrl = browseUrlObject.url
    try:
	 url = URL(browseUrl)
	 dom = DOM(url.download())
	 visited[browseUrl] = 1 
	 try:
	   for anchor in dom.by_tag('a'):
	  	 url = generateUrl(baseUrl,browseUrl,anchor.href)
	         if url != "":  
		   try:
		    dict[url].count = dict[url].count +1
		   except:
		    dict[url] = link(browseUrl,0,url)
	 except:
	     pass
    except:
    	del dict[browseUrl]
    	print browseUrlObject
	brokenUrls[browseUrl] = browseUrlObject
	pass

for i in range(10): 
  for x in dict.keys():
    try:
      visited[x]
    except:
      browse(dict[x])

f = open("links.txt","w")
fo = open("brokenLinks.txt","w")


for x in brokenUrls.keys():
	fo.write(brokenUrls[x].parentUrl + "   :   "+ x +"\n")

for x in dict.keys():
	f.write(x+"\n")

f.close()
fo.close()

