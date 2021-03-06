import pickle
import numpy
import corefResolution
import csv
from FeatureExtractor import generate_entity_features

def getWhere(inputFile, entities_in_article):
    file = open("../data/my_where_classifier.pkl", "rb")
    gnb_classifier = pickle.load(file)
    #inputFile = "../data/test.txt"
    whereList = []
    for id in entities_in_article.keys():
        for where in entities_in_article[id].keys():
            l = entities_in_article[id][where]
            type = l[3]
            l = l[:3]
            if type == 'PERSON':
                l = l + [0,0,1]
            elif type == 'ORGANISATION':
                l = l + [0,1,0]
            elif type == 'LOCATION':
                l = l + [1,0,0]
                for i in range(0,len(l)):
                    l[i] = float(l[i])
                    
            #print ("new l: " , l)
                feature = numpy.array(l)
                feature = numpy.reshape(feature,(1,6)) 
                #feature = numpy.asarray(l,dtype = numpy.float(32))
                
                #print("feature", feature)
                ans = gnb_classifier.predict(feature)
                prob_ans= gnb_classifier.predict_proba(feature)
                
                #print(who,ans[0])
                #print("probability")
                #print(who,prob_ans[0][1])
                if ans[0]== float(1):
                    whereList.append((where,prob_ans[0][1]))
            else:
                l = l + [0,0,0]    
            
            #print("list: " , l)
            
            
    if len(whereList) > 0:            
        whereList = sorted(whereList, key = lambda x:x[1],reverse  = True)
    else:
        whereList=" "
    #print(whoList) 
    return whereList  

#getWho("../data/test.txt")
                      
