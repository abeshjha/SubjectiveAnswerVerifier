import re, math
from collections import Counter
import fuzzywuzzy.fuzz

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def givKeywordsValue(text1, text2):
    vector1 = text_to_vector(text1)
    #print (vector1)
    vector2 = text_to_vector(text2)
    #print(vector2)
    fuzzy= fuzzywuzzy.fuzz.token_set_ratio(vector1,vector2)

    cosine = round(get_cosine(vector1, vector2),4)
    return cosine,fuzzy

   # kval = 0
    #if cosine > 90:
     #   kval = 1
    #elif cosine > 80:
     #   kval = 2
    #elif cosine > 60:
     #   kval = 3
    #elif cosine > 40:
     #   kval = 4
    #elif cosine > 20:
     #   kval = 5
    #else:
     #   kval = 6
    

#
#text1 = "Julie loves me more than Linda loves me" 
         

#text2 = "Jane likes me more than Julie loves me" 
         

#a = givKeywordsValue(text1=text1, text2=text2)
#print(a)
