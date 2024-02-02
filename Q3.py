import os
import nltk
import string
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import pickle

#************* Positional Inverted index **************
Inverted_index = {}
term_doc_frequency = {}


#*************************** Positional Inverted index creation Logic ********************************
def create_Inverted_Index():
    files = Path("Preprocessed files/Whitespace filtered files").glob('*')

    for file in files:
        f = open(file,"r")
        content = f.readlines()
        docId = int(file.name[4:-4])
        print(docId)
        i = 1
        for word in content:
            term = word.strip()
            if Inverted_index.get(term) == None:
                Inverted_index[term] = []
                term_doc_frequency[term] = 0

            isDocIdListExits = False
            for docIdList in Inverted_index.get(term):
                if docId == docIdList[0]:
                    docIdList[1].append(i)
                    isDocIdListExits = True
            
            if isDocIdListExits == False:
                Inverted_index[term].append([docId,[i]])
                term_doc_frequency[term] = term_doc_frequency.get(term) + 1
                sorted(Inverted_index.get(term),key= lambda x:x[0])
            i += 1

#**************************************************************************************************


#************************* Functions Saving and Loading Inverted Index ****************************
def saveInvertedIndex():
    InvertedIndexFile = open('Positional_Inverted_Index', 'wb')
    pickle.dump(Inverted_index, InvertedIndexFile)  
    InvertedIndexFile.close()

def LoadInvertedIndex():
    InvertedIndexFile = open('Positional_Inverted_Index', 'rb')
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
    print("********************* Input *********************")
    N = int(input("Number of Queries: "))
    for i in range(1,N+1):
        #************* Query Input ******************
        phrase = input("Enter phrase query: ")

        #*************** Pre processing *************
        TokensList = preprocessingFunc(phrase)

        #************** Query Processing ************
        docs = find_Containing_Docs(TokensList)
        res.append(docs)

    print("******************** Output ********************")
    for i in range(0,len(res)):
        print("Number of documents retrieved for query "+str(i+1)+" : "+str(len(res[i])))
        print("Name of the documents retrieved for query "+str(i+1)+" : ")
        for item in res[i]:
            print("file"+str(item)+".txt, ")
    
    return
#**************************************************************************************************



#************************* Function to find documents Containing phrase ****************************
def find_Containing_Docs(TokensList):
    firstTerm = TokensList[0]
    res = []
    Docs_Pos_Lists = Inverted_index.get(firstTerm)
    for list in Docs_Pos_Lists:
        docId = list[0]
        for pos in list[1]:
            if(isExistsInDoc(TokensList,1,docId,pos+1) == True):
                res.append(docId)
                break
    return res



#******************* Function to find is this pharse conatining in this doc ************************
def isExistsInDoc(TokensList,termIdx,docId,pos):
    if(termIdx == len(TokensList)):
        return True

    term = TokensList[termIdx]
    Docs_Pos_Lists = Inverted_index.get(term)
    for list in Docs_Pos_Lists:
        if(list[0] == docId):
            for p in list[1]:
                if(p == pos):
                    return isExistsInDoc(TokensList,termIdx + 1,docId,pos + 1)
                
    return False




#************************************ Calling Functions *******************************************
# create_Inverted_Index()
# saveInvertedIndex()
LoadInvertedIndex()
Input_Output_Func()