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

#reading contents in email
def readtexts(emails):
    with open(emails, 'r', encoding = 'latin-1') as mail:
        lines = mail.readlines()
    return lines

#email parser
def mail_parse(emails):
    listWords = []
    lines = readtexts(emails)
    aString = "".join(lines)
    aString = aString.lower()
    list = re.split("\[\^a-zA-Z]", aString)          

    for word in list:
        if(len(word) >= 1):
            listWords.append(word)
    return listWords



# =============================================================================
# def main():
#     print()
# if __name__ == '__main__':
#     main()
# =============================================================================

#accessing path to files
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

## Building and Evaluating the Classifier        
def test_model(test_files_name,model_name):
    
    files = os.listdir(test_files_name)
    ham = 'ham'
    spam = 'spam'
    ham_count = 0
    spam_count = 0
    
    
    #Traversing a folder
    for file in files: 
        #Determine if it is a folder, not a folder to open
        if not os.path.isdir(file):     
            if (ham in file):
                ham_count += 1
            if (spam in file):
                spam_count += 1
     
    with open('baseline-result.txt','a', encoding = 'latin-1') as test:
        number = 0
        result = ''
        key = 0    
        with open("model.txt", "r") as model:
            model_set = [[x for x in line.split()] for line in model] 
            for file in files:
                number +=1
                ##email_list = email_parser(file)
                test.write(str(number) + '  ' + str(file) + '  ')
                
                email_list = mail_parse(test_files_name + "/" + file)
                
                score_ham = math.log( (ham_count)/(spam_count + ham_count),10)
                score_spam = math.log( (spam_count)/(spam_count + ham_count),10)
                
                    
                for word in email_list: 
                    for record in model_set:
                        for data in record:
                            if data == word:
                                score_ham += math.log(float(model_set[model_set.index(record)][2]), 10)
                                score_spam += math.log(float(model_set[model_set.index(record)][4]), 10)
                                      
                test.write(str(score_ham) + '  ' + str(score_spam) + '  ') 
                if (ham in file ):
                    test.write(ham + '  ')                   
                if (spam in file):
                    test.write(spam + '  ')
                test.write('\n')
                
 ##Building the Model
def set_model(list_ham,list_spam,ham_set,spam_set,file_name):
    vocab_set = ham_set.union(spam_set)
    with open(file_name,'a', encoding = 'latin-1') as model:
        
        #adding in smoothing
        for word in vocab_set:
            ham_count = list_ham.count(word)
            ham_prob = (list_ham.count(word) + 0.5)/(len(list_ham) + 0.5*len(vocab_set))
            spam_count = (list_spam.count(word))
            spam_prob = (list_spam.count(word) + 0.5)/(len(list_spam)+0.5*len(spam_set))
            model.write(word+ '  ' +str(ham_count)+ '  ' +str(round(ham_prob,6))+ '  ' +str(spam_count) + '  ' + str(round(spam_prob,6)) + '\n' )
        

def word_count(list_ham,list_spam,vocab_set):
    ham_wc = {}     #wc is wordcount
    spam_wc = {}
    
    for word in vocab_set:
        counter = 0
        if (word in list_ham):
            counter = list_ham.count(word)
            ham_wc[word] = counter
        if (word in list_spam):
            counter = list_spam.count(word)
            spam_wc[word] = counter
     
    return ham_wc,spam_wc

#print quantity and ham and spam works
def main():
    list_ham, list_spam,ham_set,spam_set = parseFile('train')
    print(len(ham_set))
    print(len(spam_set))
    vocab = ham_set.union(spam_set)
    print(len(vocab))
    
    ham_wc,spam_wc = word_count(list_ham,list_spam,vocab)
    print (list_ham.count('a') + list_spam.count('a'))
    print (ham_wc['a'])
    print (spam_wc['a'])
    
    set_model(list_ham,list_spam,ham_set,spam_set,'model.txt')
    test_model('test', 'model.txt')
    
if __name__ == '__main__':
		main()	
