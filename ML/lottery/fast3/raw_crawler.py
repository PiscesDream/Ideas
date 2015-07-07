print 'loading...'
html = open('./data_20140701001_20141031049.html', 'r').read()

from bs4 import BeautifulSoup as bs
from pprint import pprint

soup = bs(html)
print 'souping...'

data = []
for ele in soup.find_all('td', {'class':'z_bg_13'}):
    if len(ele.text) == 3:
        data.append([int(char) for char in ele.text])

pprint (data)

from cPickle import dump
from numpy import array
dump(array(data), open('data_20140701001_2014103104.dat', 'w'))
