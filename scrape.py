from bs4 import BeautifulSoup
import requests
import csv

#with open('simple.html') as html_file:
    #soup = BeautifulSoup(html_file,'lxml')




#print soup
#print soup.prettify()


#match =soup.title.text

#match = soup.find('div',class='footer')
#print match

#headline=article.h2.a.text
#print headline

#summary=article.p.text
#print summary






#real example

source = requests.get('http://coreyms.com').text  
soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline.encode', 'summary.encode', 'video_link.encode'])



article =soup.find('article')
#print article.prettify().encode("utf-8")


																			#headline=article.h2.a.text
																			#print headline.encode("utf-8")



#summary = article.find('div', class_='entry-content').p.text
#print summary.encode("utf-8")



vid_src =article.find('iframe',class_='youtube-player')['src']
#print vid_src

vid_id=vid_src.split('/')[4]   #at index 4
vid_id=vid_id.split('?')[0]
#print vid_id

yt_link ='https://youtube.com/watch?v={}'.format(vid_id)
#print yt_link





#for all articles and videos link 
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline).encode("utf-8")

    summary = article.find('div', class_='entry-content').p.text
    print(summary).encode("utf-8")
 
    try:
        vid_src =article.find('iframe',class_='youtube-player')['src']
        vid_id=vid_src.split('/')[4]   #at index 4
        vid_id=vid_id.split('?')[0]

        yt_link ='https://youtube.com/watch?v={}'.format(vid_id)
        
    except Exception as e:
        yt_link =None

    print yt_link

    print '....'


    csv_writer.writerow([headline.encode("utf-8"), summary.encode("utf-8"), yt_link.encode("utf-8")])

csv_file.close()



























