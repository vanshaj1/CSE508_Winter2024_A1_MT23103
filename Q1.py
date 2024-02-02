import os
import nltk
import string
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')
from bs4 import BeautifulSoup

newDirectory = "Preprocessed files"


#***************** Creating pre processed directory Function*************
def create_PreProcessed_Directory():
    os.mkdir("Preprocessed files"); 



#*************************************** Helper functions *****************************************

#************************** Lowercase filtering ***************************
def Lowercase_filtering_func():
    files = Path("text_files").glob('*')
    os.mkdir("Preprocessed files/Lowercase files"); 
    for file in files:
        f = open(file,"r")
        content = f.read()
        print(content)
        content = content.lower()
        print(content)
        newPath = newDirectory+ '/Lowercase files/'+ file.name
        nf = open(newPath,'w')
        nf.write(content)

#************************ Tokenization Functiion *************************
def Tokenization_func():
    files = Path(newDirectory+ '/Lowercase files').glob('*')
    os.mkdir("Preprocessed files/Tokenized files"); 
    for file in files:
        f = open(file,"r")
        content = f.read()
        if BeautifulSoup(content, "html.parser").find() == True:
            soup = BeautifulSoup(content)
            for script in soup(["script", "style"]):
                script.extract()
            content = soup.get_text()
        tokens = word_tokenize(content)
        print(tokens)
        newPath = newDirectory+ '/Tokenized files/'+ file.name
        nf = open(newPath,"a")
        for token in tokens:
            nf.write(token)
            nf.write("\n")


#********************** Stopwords Filtering function ********************
def StopWords_filtering_func():
    files = Path(newDirectory+ '/Tokenized files').glob('*')
    os.mkdir("Preprocessed files/Stopword filtered files")
    stopwordsList = stopwords.words("english")
    for file in files:
        f = open(file,"r")
        content = f.readlines()
        newTokens = []
        for word in content:
            word = word.strip()
            if not word in stopwordsList:
                newTokens.append(word)

        newPath = newDirectory+ '/Stopword filtered files/'+ file.name
        nf = open(newPath,"a")
        for token in newTokens:
            nf.write(token)
            nf.write("\n")


#********************* Punctuation filtering function ********************
def Punctuation_filtering_func():
    files = Path(newDirectory+ '/Stopword filtered files').glob('*')
    os.mkdir("Preprocessed files/Punctuation filtered files")
    for file in files:
        f = open(file,"r")
        content = f.readlines()
        newTokens = []
        for word in content:
            word = word.strip()
            translator = str.maketrans('', '', string.punctuation)
            newToken = word.translate(translator)
            newTokens.append(newToken)
        print(content)
        print(newTokens)

        newPath = newDirectory+ '/Punctuation filtered files/'+ file.name
        nf = open(newPath,"a")
        for token in newTokens:
            nf.write(token)
            nf.write("\n")


#************************ White space filtering *************************
def Whitespace_filtering_func():
    files = Path(newDirectory+ '/Punctuation filtered files').glob('*')
    os.mkdir("Preprocessed files/Whitespace filtered files")
    for file in files:
        f = open(file,"r")
        content = f.readlines()
        newTokens = []
        for word in content:
            newToken = word.strip()
            if(newToken != ''):
                newTokens.append(newToken)
        print(content)
        print(newTokens)

        newPath = newDirectory+ '/Whitespace filtered files/'+ file.name
        nf = open(newPath,"a")
        for token in newTokens:
            nf.write(token)
            nf.write("\n")


#************************* Files printing function *********************
def printFilesContent(filepath):
    files = Path(filepath).glob('*')
    i = 0
    for file in files:
        if(i == 5):
            break
        print("*********************"+"file "+str(i+1)+"***********************")
        f = open(file,"r")
        content = f.read()
        print(content)
        print("\n")
        i += 1

#*************************************************************************************************



print("************************************ Pre Processing Starts ****************************************\n")
print("******************************* Creating Preprocessed Directory ********************************\n")
create_PreProcessed_Directory()

print("**************************************Lowercase filtering***************************************\n") 

print("**************** Files before lower casing the content *****************\n")
printFilesContent("text_files")



Lowercase_filtering_func()


print("*************** Files after lower casing the content ****************\n")
printFilesContent(newDirectory + '/Lowercase files')



print("**************************************Tokenization****************************************\n")

print("***************** Files before tokenization ********************\n")
printFilesContent(newDirectory + '/Lowercase files')


Tokenization_func()



print("**************** Files after Tokenization ********************\n")
printFilesContent(newDirectory + '/Tokenized files')





print("************************************StopWords filtering***********************************\n")

print("**************** files before StopWords removal *****************\n")
printFilesContent(newDirectory + '/Tokenized files')



StopWords_filtering_func()



print("**************** files after StopWords removal *****************\n")
printFilesContent(newDirectory+ '/Stopword filtered files')







print("***********************************Punctuation filtering*****************************************\n")

print("*************** files before Punctuation Removal *****************\n")
printFilesContent(newDirectory+ '/Stopword filtered files')


Punctuation_filtering_func()



print("**************** files after Punctuation removal *****************\n")
printFilesContent(newDirectory+ '/Punctuation filtered files')






print("**************************************Whitespace filtering*******************************************\n")

print("**************** files before Whitespace removal *****************\n")
printFilesContent(newDirectory+ '/Punctuation filtered files')
 

Whitespace_filtering_func()
    

print("**************** files after Whitespace removal *****************\n")
printFilesContent(newDirectory+ '/Whitespace filtered files')


print("******************************************Pre Processing Ends******************************************")