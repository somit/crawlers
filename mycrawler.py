from pattern.web import URL,DOM
import re,os,sys


def generateUrl(root ,baseurl, href):
  if re.search(r'^/',href):
	return root+href
  if href.startswith("http://"):
	return ""  
  s = baseurl.split('/')
  s = baseurl.replace("/"+s.pop(),"/")
  return s+"href"

dict = {}

rootUrl = 'http://winzip.com/win/en/index.htm'
baseUrl = 'http://winzip.com'
dict[rootUrl] = 0

f = open("links.txt","w")
fo = open("brokenLinks.txt","w")
def browse(browseUrl):
    try:
	 url = URL(browseUrl)
	 dom = DOM(url.download())
	 try:
	   for anchor in dom.by_tag('a'):
	  	 url = generateUrl(baseUrl,browseUrl,anchor.href)
	         if url != "":  
		   try:
		    dict[url] = dict[url]+1
		   except:
		    f.write(browseUrl+ " : " + anchor.href +" : "+ url+"\n")
		    dict[url] = 0
	 except:
	     pass
    except:
	fo.write(browseUrl+"\n")
	pass

for i in range(2): 
  for x in dict.keys():
    if dict[x] != 2:
      browse(x)

f.close()
fo.close()

