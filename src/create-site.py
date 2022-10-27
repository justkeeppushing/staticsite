#!/usr/bin/env python
import json

configfile = 'items.json'
items = json.load(open(configfile, 'r'))

skeltop = """<!DOCTYPE html>
<html>
<head>
<title>3g0st's corner</title>
<link rel="stylesheet" href="style.css">
<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>
</head>
<body>
  <div>
    <ul class="button">"""

skelbot = """      </ul>
	  <footer>
		  "[3g0st]" artist, musician, engineer
	  </footer>
  </div>
</body>
</html>"""

urls = [url['href'] for url in [item for item in items]]
labels = [label['title'] for label in [item for item in items]]

def listoflists(site, button):
        return("\t" + "<li class=\"" + button + "\">" + "<a href=\"" + site + "\">" + button + "</a></li>")

clump = map(listoflists, urls, labels) #one use only

print(skeltop)
for code in list(clump):
        print(code)
print(skelbot)
