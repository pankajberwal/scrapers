from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url="https://www.flipkart.com/search?q=mobile%20phone&as=on&as-show=on&marketplace=FLIPKART&otracker=start&as-pos=2_q_mobile%20phone"

file_name="flipkartmobilerecord.csv"

f=open(file_name,"w",encoding="utf-8")
headers="product_name,price\n"

f.write(headers)

client=ureq(my_url)
page_html=client.read()
client.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"_1-2Iqu row"})

for container in containers:
	name_container=container.findAll("div",{"class":"_3wU53n"})
	name=name_container[0].text

	price_container= container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
	price=price_container[0].text
	price.replace("20b9 ","")



	#print("name :"+name+"price :"+price+"\n")

	f.write(name.replace(",","|")+","+price.replace(",","")+"\n")

f.close()