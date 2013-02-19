from pattern.web import URL,DOM
import re,os,sys


dict = {}

f = open("links.txt","r") 
fb = open("imagebroken.txt","w")
fi = open("allImageLinks.txt","w")
for browseUrl in f:
   print browseUrl
   url = URL(browseUrl)
   dom = DOM(url.download())
   try:
     for anchor in dom.by_tag('img'):
      url = anchor.src
      print url	
      try:
	dict[url] = dict[url]+1
      except:
        fi.write(url+"\n")
	dict[url] = 0
	try:
         image = URL(url)
         dom = DOM(image.download())
        except:
	 fb.write(url+" : Page-> "+browseUrl+"\n")
   except:
     pass

f.close()
fb.close()
fi.close()
