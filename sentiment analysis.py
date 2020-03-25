# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 19:20:54 2018

@author: sudhanshu kumar sinh
"""

from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import numpy as np


def get_wordCloud(blob):
    message=""
    stopwords=set(STOPWORDS)
    for i in blob.words:
        i=i.lower()
        message+=i+" "
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(message)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    plt.show()
    
def frequencyWord(valNA,valNeg,valPos):
    plt.figure(figsize=(8,8))
    index = np.arange(len(["Positive","Negative","Unknown"]))
    plt.bar(index, [valPos,valNeg,valNA],color=["green","red","blue"])
    plt.xlabel("$Words Category$")
    plt.ylabel("$Frequency$")
    plt.xticks(index, ["Positive","Negative","Unknown"], rotation=30)
    plt.title("$Words Frequency$")
    plt.show()
    
def overAllSentiments(blob):
    print(blob.sentiment.polarity)



def main():    
    text2=open("demo.txt",'w',encoding="utf8")
    text=open("dataset.txt",'r',encoding="utf8")
    message=text.readlines()
    for i in message:
        temp=' '.join(re.sub("(@[A-Za-z0-9]+)|(#[0-9A-Za-z]+)|(_[0-9A-Za-z]+)|(#[^0-9A-Za-z]+)|(\w+:\/\/\S+)"," ",i).split())
        temp=' '.join(re.sub("([^0-9A-Za-z]+)"," ",temp).split())
        temp=temp.replace("RT","")
        text2.write(temp)
        text2.write("\n")
    text.close()
    text2.close()
    
    
    
    
    f=open("demo.txt",'r',encoding="utf8")
    data=f.read()
    f.close()
    blob=TextBlob(data)
    valPos=0
    valNeg=0
    valNA=0
    d=blob.word_counts
    for word in d:
        val=TextBlob(word)
        if val.sentiment.polarity>0:
            valPos+=d["word"]
        elif val.sentiment.polarity<0:
            valNeg+=d["word"]
        else:
            valNA+=1
    
    frequencyWord(valNA,valNeg,valPos)
    get_wordCloud(blob)
    print("The OverAll sentiments on this topic:")
    overAllSentiments(blob)
    
if __name__=="__main__":
    main()
        



#result =' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",message).split()) #re.sub(r"http\S+", "", message)
#blob=TextBlob(result)
#for sentence in blob.sentences:
#    print(sentence)
#    x=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",sentence).split())
#    print(x)
#import re
#x="@peter I really love that shirt at #Macy. http://bit.ly//WjdiW4"
#a=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())