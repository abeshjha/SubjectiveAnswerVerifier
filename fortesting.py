# -*- coding: utf-8 -*-



from sentencemodel import SentenceModel
from levenshtein_distance import calculate_levenshtein_distance
from keywordspy import TextRank4Keyword
import requests
from cosine_similarity import *
#nltk.download('wordnet')

#1-------------------------------Levestian Distance-------------------------------------------

sentences1="I am an orange"
sentences2="I am an apple"
benchmarks = calculate_levenshtein_distance(sentences1, sentences2)/(max(len(sentences1), len(sentences2)))
print(benchmarks)



#2--------------------------------Percent Match----------------------------------------------------
def percentmatch(sentences1,sentences2):
    tokens1 = SentenceModel(sentences1)
    abc = tokens1.tokens
    tokens2= SentenceModel(sentences2)
    cd = tokens2.tokens
    print(abc)
    print(cd)
    marks= (len(set(abc).intersection(set(cd))) / max(len(abc), len(cd)))
    print(marks)

percentmatch("is ","is ")

#3-----------------------------Text-rank keywords---------------------------------------------------------
text = " the theory and development of computer systems able to perform tasks normally requiring human intelligence such as visual perception, speech recognition, decision-making,"
tr4w = TextRank4Keyword()
tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
tr4w.get_keywords(10)



#4----------------------------------Grammars----------------------------------------------------
'''
answer="I is a enginer."
req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=8Zks8aYc65BXWtRw").json()
no_of_errors = len(req['errors'])
print("number of errors" + str(no_of_errors))
for i in range(no_of_errors):
    kind = req['errors'][i]['type']
    bad =  req['errors'][i]['bad']
    suggestion = req['errors'][i]['better']
    print(kind + ":" + bad)
    print("suggestions")
    print(suggestion)
'''


#5---------------------------------------Cosine Similarity--------------------------------------------
text1 = "I love apple"
text2 = "I love apple" 
         
a = givKeywordsValue(text1=text1, text2=text2)
print(a)

#------------------------------ use of wordnet-------------------------------------------
dict = ["orange","mango","apple","nice","sound","sorry"]
synonyms = []
x = "apple"
for syn in wordnet.synsets(x):
    for l in syn.lemmas():
        synonyms.append(l.name())
        
check = 5
print(synonyms)
for i in synonyms:
    if i in dict:
        print ("the synonym for " + str(x)+ " found in dictionary is "+ str(i))
        check = 0
if check != 0:
    print("no synonms found")


