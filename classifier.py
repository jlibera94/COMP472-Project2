# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:43:41 2019

@author: jlibe
"""

import numpy
import math
import sys
import re
import matplotlib

import io
import os

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



#loop through all the files 
def readFiles(path):
    for root, dirnames, filenames in os.link(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n' + join(lines)
            yield path, message
            
def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message':message, 'class':classification})
        index.append(filename)
        
    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class':[]})

data = data.append(dataFrameFromDirectory('C:\Users\jlibe\Desktop\COMP472-Project2\train','spam'))
data = data.append(dataFrameFromDirectory('C:\Users\jlibe\Desktop\COMP472-Project2\train','ham'))

#cleaning up data
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]',' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    #using porterstemmer from sklearn
    review = [ps.stem()]

#print-filter through relevant words

#naive bayes

##condtion for stopwords 