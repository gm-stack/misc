#!/usr/bin/env python

import urllib

def getPastebinLinks():
	f = urllib.urlopen("http://pastebin.com/")
	page = f.read()
	page = page.split("""<div class="content_left_box">""")[1]
	page = page.split("""<div style="padding: 0 0 10px 0;"><script type="text/javascript">""")[0]
	page = page.split("\n")
	links = []
	for line in page:
		if '<div class="clb_top"><a href="' in line:
			links.append(line.split('"')[3])
	return links

def clean(filename):
	return filename.replace("/","").replace(".","")

def getPastebin(link):
	ident = link.split("/")[-1]
	f = urllib.urlopen("http://pastebin.com/download.php?i=%s" % ident)
	page = f.read()
	f = open("pastebin/%s.txt" % clean(ident), 'w')
	f.write(page)
	f.close()
	return page

alreadyViewedLinks = []
while 1:
	links = getPastebinLinks()[::-1] # backwards because we print downwards
	for link in links:
		if not link in alreadyViewedLinks:
			print link
			print getPastebin(link)
			alreadyViewedLinks.append(link)
	print "-"