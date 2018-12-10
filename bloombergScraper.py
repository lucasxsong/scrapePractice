# import libraries
import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.bloomberg.com/quote/SPX:IND%27'

# query the website and return the html to the variable "page"
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store it into the variable soup
soup = BeautifulSoup(page, 'html.parser')

# take out the <div> and get its value
name_box = soup.find('h1, attrs={'class': 'name'})

# strip() is used to remove starting and trailing
name = name_box.text.strip() 
print name

# get the index price
price_box = soup.find('div',attrs = {'class': 'price'})
price = price_box.text
print price