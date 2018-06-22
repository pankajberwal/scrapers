
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

client=ureq(my_url)
page_html=client.read()
client.close()

page_soup=soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

file_name="graphic_cards.csv"

f=open(file_name,"w",encoding="utf-8")

headers="Brand,Product_name,price\n"

f.write(headers)

for container in containers:
	brand_name=container.div.div.a.img["title"]

	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text

	price_container = container.findAll("li",{"class":"price-current"})
	price=price_container[0].text.strip().replace("\xa0(2 Offers)\n\n","")

	f.write(brand_name+","+product_name.replace(",","|")+","+price+"\n")

f.close()

