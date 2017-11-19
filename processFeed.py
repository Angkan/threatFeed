#!/usr/bin/python
try:
	import feedparser
	import bs4
	import sys
except Exception,e:
	print "[-]Error: " + str(e)
	print "[-]Exiting"
	sys.exit(-1)

print "[+]opening the html file"
with open("abc.html") as inf:
	txt = inf.read()
	soup = bs4.BeautifulSoup(txt,"lxml")	#prevents error

def readFeed(url):
  #Function to parse the rss sources and fetch the links
	print "[+]Reading feed: " + url
	d = feedparser.parse(url)
	length = len(d['entries'])
	for i in range(length):
		title = d['entries'][i]['title']
		link = d['entries'][i]['link']
		writeData(title,link)

def writeData(title,link):
  #Function to write data to the output html. On this HTML file, security analysts can view feeds from the rss
	print "[+]Writing data"
	lineBreak = soup.new_tag("br")
	new_link = soup.new_tag("a",href=link)
	new_link.string = title
	soup.body.append(new_link)
	soup.body.append(lineBreak)
	with open("abc.html","w") as outf:
		outf.write(str(soup))
	print "[+]Done!"

def main():
	print "[+]Main function"
	#Define sources here and add to the list
	urls = ["https://threatpost.com/category/vulnerabilities/feed/", "https://threatpost.com/category/government/feed/", "http://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/category/malware/feed/", "https://threatpost.com/category/web-security/feed/"]
	for url in urls:
		readFeed(url)

if __name__ == "__main__":
	main()
