# -*- coding: utf-8 -*-

"""
Created on Fri Jul 12 09:59:53 2019

@author: Abesh
"""
from sentencemodel import SentenceModel
from levenshtein_distance import calculate_levenshtein_distance
from keywordspy import TextRank4Keyword
import requests
from cosine_similarity import *

#1-------------------------------Levestian Distance-------------------------------------------
def levestiandistace(sentences1,sentences2):
    benchmarks = calculate_levenshtein_distance(sentences1, sentences2)/(max(len(sentences1), len(sentences2)))
    return benchmarks



#2--------------------------------Percent Match----------------------------------------------------
def percentmatch(sentences1,sentences2):
    tokens1 = SentenceModel(sentences1)
    abc = tokens1.tokens
    tokens2= SentenceModel(sentences2)
    cd = tokens2.tokens
    marks= (len(set(abc).intersection(set(cd))) / max(len(abc), len(cd)))
    return marks



#3-----------------------------Text-rank keywords---------------------------------------------------------
def keywords(text):
    
    tr4w = TextRank4Keyword()
    tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
    abc,cde = tr4w.get_keywords(10)
    return abc,cde



#4----------------------------------Grammars----------------------------------------------------
def grammars(answer):
    try:
        req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=qXL5LjCHjFhO5TBc").json()
        no_of_errors = len(req['errors'])
        print("number of errors" + str(no_of_errors))
        for i in range(no_of_errors):
            kind = req['errors'][i]['type']
            bad =  req['errors'][i]['bad']
            suggestion = req['errors'][i]['better']
            print(kind + ":" + bad)
            print("suggestions")
            print(suggestion)
        return no_of_errors
    except:
        print("sorry could not find grammatical mistakes due to internet connection")
        return 10
        

#5---------------------------------------Cosine Similarity--------------------------------------------
def cosinesimilarity(text1,text2):
    
    a,b = givKeywordsValue(text1, text2)
    return a,b

