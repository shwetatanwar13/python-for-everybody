import urllib
from BeautifulSoup import *

def follow_link(url, count, position, calls = 0): 
  print 'Retrieving:',url.replace('tsugi/mod/python-data/data', ' ... ')
  if calls == count:
    exit()  
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  tags = soup('a')
  iter = 1
  for tag in tags:
    if iter == position:
      name = tag.contents[0]
      print name
      #print calls    
      follow_link(tag.get('href', None), count, position, calls + 1)
    iter = iter + 1
  
url = raw_input('Enter URL: ')
input_count = raw_input('Enter count: ')
input_position = raw_input('Enter position: ')

count = int(input_count)
position = int(input_position)

follow_link(url, count, position)

'''
https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
count       4
position    3

https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Ivory.html
count       7
position    18
'''



