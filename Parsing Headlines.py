
# coding: utf-8

# In[1]:

import urllib
from BeautifulSoup import *
import csv
ndtv = open("news_headlines_ndtv.csv", "a") #opening a new csv file for ndtv headlines in append mode
for i_ndtv in range(1,14):
    headlines_ndtv = list()
    page_ndtv = urllib.urlopen('http://www.ndtv.com/top-stories/page-'+str(i_ndtv)) #accessing different pages on ndtv website
    soup_ndtv = BeautifulSoup(page_ndtv)
    p_ndtv = soup_ndtv('div') #parsing wrt 'div' tag
    hl_ndtv = soup_ndtv('a') #parsing wrt 'a' tag
    for x_ndtv in p_ndtv:
        for t_ndtv in hl_ndtv:
            if (x_ndtv.get('class') == 'nstory_header'):  #parsing wrt 'class' attribute
                if(str(t_ndtv.get('title')) != 'None'):
                    if(str(t_ndtv.get('title'))!="Weddings"):
                        temp_ndtv = (str(t_ndtv.get('title'))).split(',')
                        temp_concat_ndtv = ''
                        for i in temp_ndtv:
                            temp_concat_ndtv = i + ' '+temp_concat_ndtv
                        headlines_ndtv.append(temp_concat_ndtv) #accessing the contents of 'title' attribute and storing in created list
    
    for l_ndtv in range(12,41): #accessing only the headlines in list and discarding garbage(wrt headlines)
        if (l_ndtv%2==0):
            ndtv.write(headlines_ndtv[l_ndtv]+'\n') #storing into the created file
            
    #ndtv.write('\n')
    
    
ndtv.close()

toi = open('news_headlines_toi.csv','a') #opening a new csv file for toi headlines in append mode
headlines_toi=list()
page_toi = urllib.urlopen('https://timesofindia.indiatimes.com/home/headlines')
soup_toi = BeautifulSoup(page_toi)
p_toi = soup_toi('div') #parsing wrt 'div' tag
hl_toi = soup_toi('a') #parsing wrt 'a' tag
for x_toi in p_toi:
    for t_toi in hl_toi:
        if (x_toi.get('class') == 'top-newslist'): #parsing wrt 'class' attribute
            if(str(t_toi.get('title')) != 'None'):
                temp_concat_toi = ''
                temp_toi = (str(t_toi.get('title'))).split(',')
                for i in temp_toi:
                    temp_concat_toi = i + ' '+temp_concat_toi
                headlines_toi.append(temp_concat_toi) #accessing the contents of 'title' attribute and stor

                

for i_toi in range (10,135): #accessing only the headlines in list and discarding garbage(wrt headlines)
   toi.write(headlines_toi[i_toi]+'\n') #storing into the created file
toi.close()


# In[ ]:



