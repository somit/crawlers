from pattern.web import URL,DOM
import re,os,sys

print "Scanning LINKS.txt..................."

def generateUrl(root ,baseurl, href):
  if re.search(r'^/',href):
	return root+href
  if href.startswith("http://") or href.startswith("www."):
	return href  
  s = baseurl.split('/')
  s = baseurl.replace("/"+s.pop(),"/")
  return s+"href"



rootUrl = 'http://winzip.com/win/en/index.htm'
baseUrl = 'http://winzip.com'
dict = {}

f = open("links.txt","r") 
fb = open("jsandcssbroken.txt","w")
fi = open("alljsandcssLinks.txt","w")
for browseUrl in f:
   print browseUrl
   print "=================================================="
   url = URL(browseUrl)
   mainDom = DOM(url.download())
   try:
     for anchor in mainDom.by_tag('link'):
      url = generateUrl(rootUrl, baseUrl, anchor.href)
      try:
	dict[url] = dict[url]+1
      except:
        print url	
        fi.write(url+"\n")
	dict[url] = 0
	try:
         cssurl = URL(url)
         dom = DOM(cssurl.download())
        except:
	 fb.write(url+" : Page-> "+browseUrl+"\n")
   except:
     pass
   
   try:
     allUrl = []
     for anchor in mainDom.by_tag('script'):
      allUrl = allUrl+re.findall('<script.*src="(.*\.js)"></script>',anchor.html)
     for anchor in allUrl:
      url = generateUrl(rootUrl, baseUrl, anchor)
      print url
      try:
	dict[url] = dict[url]+1
      except:
        fi.write(url+"\n")
	dict[url] = 0
	try:
         jsurl = URL(url)
         dom = DOM(jsurl.download())
        except:
	 fb.write(url+" : Page-> "+browseUrl+"\n")
   except:
     pass



f.close()
fb.close()
fi.close()
