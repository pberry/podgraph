# -*- coding: utf-8 -*-
import feedparser
import re
import time
from bs4 import BeautifulSoup

# d = feedparser.parse('https://daringfireball.net/thetalkshow/rss')
d = feedparser.parse('https://techmeme.com/techmeme-ride-home-feed')
for post in d.entries:
   	if "Longread" in post.summary :
   		soup = BeautifulSoup(post.summary, 'html.parser')
   		postPub = time.strftime("%A, %B %d" ,post.published_parsed)
   		print(postPub)
   		for p in soup.find_all('p'):
   			if "Longreads:" in p.text:
   				print ("\n**" + postPub + "**")
   				for a in (p.next_sibling.find_all('a')):
   					print ("* [" + a.string + "](" + a['href'] + ")")
