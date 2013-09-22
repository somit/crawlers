import urllib2

from urlparse import urljoin
from BeautifulSoup import *


'''
Crawler class
'''

ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler:
    #crawler initialized with the name of database
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    #Function for getting an entry id ans adding it if not present.
    def getentryid(self, table, field, value, createnew=True):
        return None

    #index an individual page
    def addtoindex(self, url, soup):
        print "Indexing %s", url

    #Extract test from an html page(no tags)
    def gettextonly(self, soup):
        return None

    #Separate words by and non-whitespace character
    def separatewords(self, text):
        return None

    #returns true if url is already indexed
    def isindexed(self, url):
        return False

    #add links between 2 pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    #Starting with a list of pages do a BFS to the given depth,
    #indexing pages as we go
    def crawl(self, pages, depth=2):
        pass

    #Create database tables
    def createindextables(self):
        pass
