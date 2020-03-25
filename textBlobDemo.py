# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:35:47 2018

@author: sudhanshu kumar sinh
"""

from textblob import TextBlob
val="Monty is happy. मोंटी खुश है"
blob=TextBlob(val)
blob.tags           #[('Monty', 'NNP'), ('is', 'VBZ'), ('happy', 'JJ')]

blob.sentences      #WordList(['monty'])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    
for sentence in blob.sentences:
    if sentence.detect_language()!="en":
        print(sentence.translate(to="en"))
    else:
        print(sentence)