# import libraries
import urllib2

from bs4 import BeautifulSoup

quote_page = 'http://books.toscrape.com/'

# query the website and return the html to the variable "page"
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store it into the variable soup
soup = BeautifulSoup(page, 'html.parser')

# take out the <div> and get its value
name_box = soup.find('div', attrs={'class': 'product_price'})

# strip() is used to remove starting and trailing
print(name_box.get_text(strip=True))

# get the index price
price_box = soup.find('div',attrs = {'class': 'price_color'})
price = price_box.text
print price