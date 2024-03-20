from bs4 import BeautifulSoup
import requests
import csv

page_scrape = requests.get("PUT SOURCE HERE")
soup = BeautifulSoup(page_scrape.text, "html.parser")

tags = soup.findAll('dd', attrs={'class':'search_tag'})
titles = soup.findAll('dt', attrs={'class':'work_name'})
prices = soup.findAll('dd', attrs={'class':'work_price_wrap'})
descs = soup.findAll('dd', attrs={'class':'work_text'})

file = open('CSVNAME.csv', 'w' )
writer = csv.writer(file)

writer.writerow(['title', 'tag', 'desc', 'price'])



for title, tag, desc, price in zip(titles, tags, descs, prices):
  print(title.find('a').contents[0], '-', tag.text,'-', desc.text,'-',price.text)
  writer.writerow([title.find('a').contents[0], tag.text, desc.text,price.text])

file.close()

'''
#links
for title in titles:
  print(title.find('a')['href'])

#titles
for title in titles:
  print(title.find('a').contents[0])

#tags
for tag in tags:
  print(tag.text)

#descriptions
for desc in descs:
  print(desc.text)

#prices
for price in prices:
  print(price.text)
'''
