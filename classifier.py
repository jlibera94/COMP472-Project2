4# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:43:41 2019

@author: jlibe
"""

import numpy
import math
import sys
import re
import matplotlib

import os


#loop through all the files 
# =============================================================================
# def readFiles(path):
#     for root, dirnames, filenames in os.link(path):
#         for filename in filenames:
#             path = os.path.join(root, filename)
#             
#             inBody = False
#             lines = []
#             f = io.open(path, 'r', encoding='latin1')
#             for line in f:
#                 if inBody:
#                     lines.append(line)
#                 elif line == '\n':
#                     inBody = True
#             f.close()
#             message = '\n' + join(lines)
#             yield path, message
# =============================================================================

#reading contents in email
def readfile(emails):
    with open(emails, 'r', encoding = 'latin-1') as mail:
        lines = mail.readlines()
    return lines

#email parser
def mail_parse(emails):
    listWords = []
    lines = readfile(emails)
    string = "".join(lines)
    string = string.lower()
    list = re.split("[^a-zA-Z]", string)          

    for word in list:
        if(len(word) >= 1):
            listWords.append(word)
    return listWords

#accessing the path to the files 
def parseFile(path):
    files = os.listdir(path)
    ham = 'ham'
    spam = 'spam'
    list_ham = []
    list_spam = []
    
    for file in files:
        if not os.path.isdir(file):
            if(ham in file):
                list_ham += mail_parse(path + "/" + file)
            if(spam in file):
                list_spam += mail_parse(path + "/" + file)
    return list_ham, list_spam, set(list_ham), set(list_spam)

#working on updating frequency of the words



# =============================================================================
# def dataFrameFromDirectory(path, classification):
#     rows = []
#     index = []
#     for filename, message in readFiles(path):
#         rows.append({'message':message, 'class':classification})
#         index.append(filename)
#         
#     return DataFrame(rows, index=index)
# 
# data = DataFrame({'message': [], 'class':[]})
# 
# data = data.append(dataFrameFromDirectory('C:\Users\jlibe\Desktop\COMP472-Project2\train','spam'))
# data = data.append(dataFrameFromDirectory('C:\Users\jlibe\Desktop\COMP472-Project2\train','ham'))
# 
# #cleaning up data
# corpus = []
# for i in range(0, len(messages)):
#     review = re.sub('[^a-zA-Z]',' ', messages['message'][i])
#     review = review.lower()
#     review = review.split()
#     
#     #using porterstemmer from sklearn
#     review = [ps.stem()]
# =============================================================================

#print-filter through relevant words

#naive bayes

##condtion for stopwords 