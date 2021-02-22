from levenshtein_distance import calculate_levenshtein_distance   
from sentencemodel import SentenceModel
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
from rake_nltk import Rake
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer,PorterStemmer
from appJar import gui
from calculations import *
from API_givVal import *

app=gui("evaluation")

testlist=[]
trainlist=[]
uniquelist=[]
keys=[]
values=[]
global i

def choice(btn):
    if btn=='Add Question':
        
        app.addLabel(250,"Enter question and standard answer")
        app.addLabelEntry("question")
        app.addLabelEntry("answer")
        
        app.addButton("done",teacher)

    elif btn=='Give Exam':
        f= open("question.txt","r+")
        question = f.read()
        app.addLabel(250,question)     
        app.addLabelEntry("answer")
        app.addButton("submit",student)
    elif btn=='Get Score':
        f= open("answer.txt","r+")
        train_data = f.read()
        g= open("student.txt","r+")
        test_data = g.read()
        app.addLabel(250,"Get score on basis of keywords matched and synonyms")
        Extract(train_data,test_data,max_score)
        
     

def lematize(lista):
    w=WordNetLemmatizer()
    a=list(map(w.lemmatize,lista))
    return a
def stem(lista):
    s=PorterStemmer()
    a=list(map(s.stem,lista))
    return a
def break_phrases(list):
    a=[]
    for x in list:
        if len(x.split())==1:
            a.append(x)
        else:
            a.extend(x.split())
    return a



f= open("answer.txt","r+")
answer = f.read()
key,values = keywords(answer)
keys=lematize(key)
dict = {k.lower(): v for k, v in zip(keys, values)}
print("----------------------------------------------------")
print("the keywords and corresponding values after text-rank algorithm")
print(dict)
print("----------------------------------------------------")


def teacher(btn):
    question=app.getEntry("question")
    f= open("question.txt","w+")
    f.write(question)
    print('question writing done')
    answer=app.getEntry("answer")
    f= open("answer.txt","w+")
    f.write(answer)
    print('answer writing done') 
def student(btn):
    student=app.getEntry("answer")
    f= open("student.txt","w+")
    f.write(student)
    print(' student answer writing done') 

     
def Extract(train_data,test_data,max_score,Enter_rank=True):
    train,test = Rake(),Rake()
    train.extract_keywords_from_text(train_data)
    test.extract_keywords_from_text(test_data)
    train_keywords=lematize(break_phrases(train.get_ranked_phrases()))
    test_keywords=lematize(break_phrases(test.get_ranked_phrases()))
    
    
    for b in train_keywords:
        
       # print(b)      
        trainlist.append(b)

    print("the keywords extracted from student's answer")
    for x in test_keywords:
               
        testlist.append(x)
    
    
    result=0
     
    
    for a in testlist:
      if not a in uniquelist:
          uniquelist.append(a);
    print(uniquelist)
    print("----------------------------------------------------")
    total= sum(dict.values())
    for x in uniquelist:
        
        if x in dict.keys():
            
            print(x)
            result=result+(dict[x]/total)*100
            print(result,dict[x])
            dict[x]=0
        else:
            print(x)
            synonyms = []
            for syn in wordnet.synsets(x):
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    
            check = 5
            for i in synonyms:
                if i in dict.keys():
                    print ("the synonym for " + str(x)+ " found in dictionary is "+ str(i))
                    
                    result=result+(dict[i]/total)*100
                    print(result,dict[i])
                    dict[i]=0
                    check = 0
            if check != 0:
                print("no synonms found")
                
              
                    
    f= open("answer.txt","r+")
    sentences1 = f.read()
    g= open("student.txt","r+")
    sentences2 = g.read()
    
    #---------------------------------------calculation of parameter 1 keywords.....................................
    param1 = 0.4*result
    print("----------------------------------------")
    print("percentage from keyword match")
    print(param1)
    print("----------------------------------------")
    #print(param1)
    
    #----------------------------------------calculation of parameter 2 levestian distance.....................................
    param = levestiandistace(sentences1,sentences2)
    param2 = 0.1*(1 -param)*100
    print("percentage from levestian distance")
    print(param2)
    print("----------------------------------------")
    
    #---------------------------------------calculation of parameter 3 percent match.....................................
    abc= percentmatch(sentences1,sentences2)
    param3 = 0.1*abc*100
    print("percenatge from percent match")
    print(param3)
    print("----------------------------------------")
    
   
    #---------------------------------------calculation of parameter 4 grammars.....................................
   
    
    print("percentage  from grammar")
    para= grammars(sentences2)
    if para==0:
        ad = 100
    elif para==1:
        ad= 80
    elif para==2:
        ad = 60
    elif para==3:
        ad = 40
    elif para==4:
        ad == 20
    else:
        ad = 0
    param4 = 0.2*ad
    print(param4)
    print("----------------------------------------")
    
    #-----------------------------------------calcuation of paramter 5 cosine similarity and fuzzy---------------------
    
    ab,cd= cosinesimilarity(sentences1,sentences2)
    fuzzy = 0.05*cd
    param5= (0.05*ab*100)+fuzzy
    print("result from fuzzy logics")
    print(cd)
    print("------------------------------------------------------")
    print("percentage from cosine similarity")
    print(param5)
    print("----------------------------------------")
    
    #-------------------------------------------calculation  of paramter 6 gaussian nb classifier----------------------
    
    predicted = myFun(sentences1,sentences2,para)
    param6 = 0.1*(predicted * 11)
    print("percentage from baysian network" )
    print(param6)
    print("----------------------------------------")
    
    result = (param1+param2+param3+param4+param5+param6)
    print("hence,the final result"+str(result))
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", result)
    if result >= 90:
        grade = "A+"
    elif result >=80:
        grade = "A"
    elif result >=70:
        grade = "B+"
    elif result >=60:
        grade = "B"
    elif result >= 40:
        grade = "C"
    else:
        grade = "D"
    app.addLabel("GRADE: " + grade)
    app.stopSubWindow()
    app.addButton("get score",score)
    
def score(btn):
    app.showSubWindow("one")

    


max_score=10
app.setSize("500x300")
app.addLabel("50", "Welcome to Evaluation System")

app.addButtons(["Add Question","Give Exam","Get Score"],choice)

app.go()
