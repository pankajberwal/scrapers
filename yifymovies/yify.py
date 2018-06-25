from robobrowser import RoboBrowser

my_url='http://yifyhdtorrent.com/'

file_name='yify.csv'

f=open(file_name,'w')
headers='MOVIE_NAME,RATINGS\n'
f.write(headers)

browser=RoboBrowser(history=True)
browser.open(my_url)

browser.parsed('html')

containers=browser.find_all('div',attrs={'class':'smp-view'})

for container in containers:
	name_container=container.find('div',attrs={'class':'title-video'})
	movie_name=name_container.a
	name=movie_name.text

	ratings=container.div.text.strip()
	
	#print('NAME : '+name+'   \nRatings :'+ ratings[0] +'\n')

	f.write(name+','+ratings[0]+'\n')
	
f.close()
