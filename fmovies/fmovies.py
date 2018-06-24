from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as open_url
from urllib.request import Request as req

my_url='http://fmovies.cloud/movie/filter/movie/latest/1-2-120-125-7-25-126-119-112-122-6-121-10-118-123-3-23-22/all/all/all/all/3/'

file_name='fmovies_data.csv'

f=open(file_name,'w+')

header='MOVIE_NAME,QUALITY\n'
f.write(header)


headers={}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

access_request=req(my_url,headers=headers)
client=open_url(access_request)
page_html=client.read()
client.close()


page_soup=soup(page_html,'html.parser')

containers=page_soup.findAll('div' , {'class':'ml-item'})

for container in containers:
	moviename_container=container.findAll('span' , {'class':'mli-info'})

	movie_name=moviename_container[0].text.strip()
	
	quality_container=container.findAll('span',{'class':'mli-quality'})
	quality=quality_container[0].text

	#print('movie_name : '+ movie_name +'          and  quality :'+quality)
	
	f.write(movie_name.replace(',','')+','+quality+'\n')
f.close()