from lxml import html
import requests
import os
import sys
import argparse

# Must run with TPB search query (e.g. "suits")
searchTerm = sys.argv[1]

# Build URL using search query
url = "https://thepiratebay.org/search/%s/0/99/0" % searchTerm
print(url)

# Request content from URL and convert to a tree
page = requests.get(url)
tree = html.fromstring(page.content)

# Build path to extract magnet link from first result
path = '//div[@id="SearchResults"]/div[@id="content"]/div[@id="main-content"]/table[@id="searchResult"]/tr[position() = 1]/td[position() = 2]/a[position() = 1]/@href'
magnetLink = tree.xpath(path)[0]

# Open the magnet link (should launch torrent client)
cmd = 'open %s' % magnetLink
os.system(cmd)
