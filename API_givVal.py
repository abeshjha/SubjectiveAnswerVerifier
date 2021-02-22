import math
import nav_test
import requests
from fuzzywuzzy import fuzz
import cosine_similarity as keywordVal

def myFun(model_answer, answer,para):
    # KEYWORDS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TODO : Enhance this thing
    

    ka,f = keywordVal.givKeywordsValue(model_answer, answer)

    # GRAMMAR =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   
    
    cosine = ka*100
    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    
    if para > 5 or kval == 6:
        g = 0
    else:
        g = 1

    # QST =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    qa = math.ceil(fuzz.token_set_ratio(model_answer, answer))
    if qa > 90:
        q = 1
    elif qa > 80:
        q = 2
    elif qa > 60:
        q = 3
    elif qa > 40:
        q = 4
    elif qa > 20:
        q = 5
    else:
        q = 6

    print("Keywords : ", kval)
    print("Grammar  : ", g)
    print("QST      : ", q)

    predicted = nav_test.predict(kval, g, q)
    print(predicted)
    return predicted




