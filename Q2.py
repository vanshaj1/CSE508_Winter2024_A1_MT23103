import os
import nltk
import string
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import pickle

#************* Unigram Inverted index **************
Inverted_index = {}
term_doc_frequency = {}

#****************** DocId Pool *********************
DocId_pool = []

#*************************** Unigram Inverted index creation Logic ********************************
def create_Intverted_Index():
    files = Path("Preprocessed files/Whitespace filtered files").glob('*')

    for file in files:
        f = open(file,"r")
        content = f.readlines()
        docId = int(file.name[4:-4])
        DocId_pool.append(docId)
        print(docId)
        for word in content:
            term = word.strip()
            if Inverted_index.get(term) == None:
                Inverted_index[term] = []
                term_doc_frequency[term] = 0
            if not docId in Inverted_index.get(term):
                Inverted_index.get(term).append(docId)
                Inverted_index.get(term).sort()
                term_doc_frequency[term] = term_doc_frequency.get(term) + 1

#**************************************************************************************************

#************************* Functions Saving and Loading Inverted Index ****************************
def saveInvertedIndex():
    InvertedIndexFile = open('Unigram_Inverted_Index', 'wb')
    pickle.dump(Inverted_index, InvertedIndexFile)  
    InvertedIndexFile.close()

def LoadInvertedIndex():
    InvertedIndexFile = open('Unigram_Inverted_Index', 'rb')
    Inverted_index_temp = pickle.load(InvertedIndexFile)
    for term in Inverted_index_temp.keys():
        Inverted_index[term] = Inverted_index_temp.get(term)
    InvertedIndexFile.close()



#***************************************** Pre Processing *****************************************
def preprocessingFunc(sentence):
    #*** Lower case filtering ***
    sentence = sentence.lower()
    
    #****** Tokenization ********
    if BeautifulSoup(sentence, "html.parser").find() == True:
        soup = BeautifulSoup(sentence)
        for script in soup(["script", "style"]):
            script.extract()
        sentence = soup.get_text()
    tokens = word_tokenize(sentence)

    #**** stopword removal ******
    newTokens = []
    stopwordsList = stopwords.words("english")
    for token in tokens:
        if not token in stopwordsList:
            newTokens.append(token)
    tokens = newTokens
    
    #**** punctuations removal **
    newTokens = []
    for token in tokens:
        translator = str.maketrans('', '', string.punctuation)
        newToken = token.translate(translator)
        newTokens.append(newToken)
    tokens = newTokens

    #***** Whitespace removal ***
    newTokens = []
    for token in tokens:
        if(token != ''):
            newTokens.append(token)
    tokens = newTokens

    return tokens
#*************************************************************************************************


#*************************************** Input Output Handling ************************************
def Input_Output_Func():
    res = []
    query = []
    print("********************* Input *********************")
    N = int(input("Number of Queries: "))
    for i in range(1,N+1):
        #************* Query Input ******************
        sentence = input("Input sequence: ")
        operations = input("Operations separated by comma: ")
        query.append(sentence)

        #*************** Pre processing *************
        operationsList = operations.split(",")
        TokensList = preprocessingFunc(sentence)
        Term_Doc_List = []
        for term in TokensList:
            doc_List = Inverted_index.get(term)
            Term_Doc_List.append(doc_List)

        #************** Query Processing ************
        queryRes = GenericQueryFunc(Term_Doc_List,operationsList)
        res.append(queryRes)

    print("******************** Output ********************")
    for i in range(0,len(query)):
        print("Query "+str(i+1)+": "+str(query[i]))
        print("Number of documents retrieved for query "+str(len(res[i])))
        print("Name of the documents retrieved for query ")
        for item in res[i]:
            print("file"+str(item)+".txt, ")
    
    return
#**************************************************************************************************
            


#**************************************** Generic Operations **************************************
def GenericQueryFunc(TermsLists,Operations): 
    for operation in Operations:
        if operation == "OR":
            T1 = TermsLists.pop(0)
            T2 = TermsLists.pop(0)
            res = ORFunc(T1,T2)
            TermsLists.insert(0,res)

        elif operation == "AND" :
            T1 = TermsLists.pop(0)
            T2 = TermsLists.pop(0)
            res = AndFunc(T1,T2)
            TermsLists.insert(0,res)

        elif operation == "OR NOT":
            T1 = TermsLists.pop(0)
            T2 = TermsLists.pop(0)
            res = OR_NOT_Func(T1,T2)
            TermsLists.insert(0,res)

        elif operation == "AND NOT" :
            T1 = TermsLists.pop(0)
            T2 = TermsLists.pop(0)
            res = AND_NOT_Func(T1,T2)
            TermsLists.insert(0,res)
    
    return TermsLists[0]
#**************************************************************************************************



#************************************** Binary Operations *****************************************

#*********************************** BASIC Functions ************************************
#************************** AND Operation *************************
def AndFunc(T1,T2):
    res = []

    for item1 in T1:
        if item1 in T2:
            res.append(item1)

    return res

#************************** OR Operation **************************
def ORFunc(T1,T2):
    res = []

    for item in T1:
        res.append(item)

    for item in T2:
        if not item in res:
            res.append(item)

    return res

#************************** NOT Operation *************************
def NOTFunc(T):
    res = []

    for item in DocId_pool:
        if not item in T:
            res.append(item)

    return res

#************************************* Complex Function **********************************
#*********************** OR NOT ***********************
def OR_NOT_Func(T1,T2):
    nT2 = NOTFunc(T2)
    res = ORFunc(T1,nT2)
    return res

#*********************** AND NOT **********************
def AND_NOT_Func(T1,T2):
    nT2 = NOTFunc(T2)
    res = AndFunc(T1,nT2)
    return res

#***************************************************************************************************        




#************************ function calling **********************
# create_Intverted_Index()
# saveInvertedIndex()
LoadInvertedIndex()
Input_Output_Func()
        


        
            

