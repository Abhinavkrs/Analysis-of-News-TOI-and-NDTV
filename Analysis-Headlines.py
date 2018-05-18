
# coding: utf-8

# In[1]:

import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np


o_toi = open("news_headlines_toi.csv", "r")
toi = o_toi.readlines()
pos_ndtv = 0
neg_ndtv = 0
neut_ndtv = 0

pos_toi = 0
neg_toi = 0
neut_toi = 0


for p_toi in toi:
    
    
    tb_toi = TextBlob(p_toi)

    sc_toi = tb_toi.sentiment.polarity
    

   
    if (sc_toi>0):
        pos_toi=pos_toi+1
    elif (sc_toi<0):
        neg_toi = neg_toi+1
    else:
        neut_toi = neut_toi+1


o_ndtv = open("news_headlines_ndtv.csv", "r")
ndtv = o_ndtv.readlines()


for p_ndtv in ndtv:
    
    
    tb_ndtv = TextBlob(p_ndtv)

    sc_ndtv = tb_ndtv.sentiment.polarity
    

   
    if (sc_ndtv>0):
        pos_ndtv=pos_ndtv+1
    elif (sc_toi<0):
        neg_ndtv = neg_ndtv+1
    else:
        neut_ndtv = neut_ndtv+1


print 'For NDTV:\nPositive News: ',pos_ndtv,'\nNegative News: ',neg_ndtv,'\nNeutral News: ',neut_ndtv

print 'For TOI:\nPositive News: ',pos_toi,'\nNegative News: ',neg_toi,'\nNeutral News: ',neut_toi

x = ('TOI','NDTV')
y_pos = np.arange(len(x))

print y_pos

pos = [(pos_toi*100)/len(toi),(pos_ndtv*100)/len(ndtv)]

plt.bar(y_pos, pos, align='center', alpha=0.5,width=.2,color = 'green')
plt.xticks(y_pos, x)
plt.ylabel('Percentage of Positive News')
plt.title('Positive News Comparision Of TOI and NDTV')

plt.show()

neg = [(neg_toi*100)/len(toi),(neg_ndtv*100)/len(ndtv)]


plt.bar(y_pos, neg, align='center', alpha=0.5,width=.2, color = 'red')
plt.xticks(y_pos, x)
plt.ylabel('Percentage of Negative News')
plt.title('Negative News Comparision Of TOI and NDTV')


plt.show()


neut = [(neut_toi*100)/len(toi),(neut_ndtv*100)/len(ndtv)]
plt.bar(y_pos, neut, align='center', alpha=0.5,width = .2, color ='yellow')
plt.xticks(y_pos, x)
plt.ylabel('Percentage of Neutral News')
plt.title('Neutral News Comparision Of TOI and NDTV')


plt.show()

o_toi.close()
o_ndtv.close()


# In[ ]:



