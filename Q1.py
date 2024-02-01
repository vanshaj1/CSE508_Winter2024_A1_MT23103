import os
import nltk
import string
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')

newDirectory = "Preprocessed files"
# os.mkdir("Preprocessed files"); 

print("************************************ Pre Processing Starts ****************************************\n")

print("**************************************Lowercase filtering***************************************\n") 
files = Path("text_files").glob('*')

print("**************** Files before lower casing the content *****************\n")
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


# ***************Logic****************
# os.mkdir("Preprocessed files/Lowercase files"); 
# for file in files:
#     f = open(file,"r")
#     content = f.read()
#     print(content)
#     content = content.lower()
#     print(content)
#     newPath = newDirectory+ '/Lowercase files/'+ file.name
#     nf = open(newPath,'w')
#     nf.write(content)


print("*************** Files after lower casing the content ****************\n")
files = Path(newDirectory + '/Lowercase files').glob('*')
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



print("**************************************Tokenization****************************************\n")
files = Path(newDirectory+ '/Lowercase files').glob('*')

print("***************** Files before tokenization ********************\n")
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1

# ***************Logic****************
# os.mkdir("Preprocessed files/Tokenized files"); 
# for file in files:
#     f = open(file,"r")
#     content = f.read()
#     tokens = word_tokenize(content)
#     print(tokens)
#     newPath = newDirectory+ '/Tokenized files/'+ file.name
#     nf = open(newPath,"a")
#     for token in tokens:
#         nf.write(token)
#         nf.write("\n")



print("**************** Files after Tokenization ********************\n")
files = Path(newDirectory + '/Tokenized files').glob('*')
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1





print("************************************StopWords filtering***********************************\n")
files = Path(newDirectory+ '/Tokenized files').glob('*')

print("**************** files before StopWords removal *****************\n")
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1

# ***************Logic****************
# os.mkdir("Preprocessed files/Stopword filtered files")
# stopwords = stopwords.words("english")
# for file in files:
#     f = open(file,"r")
#     content = f.readlines()
#     newTokens = []
#     for word in content:
#         word = word.strip()
#         if not word in stopwords:
#             newTokens.append(word)

#     newPath = newDirectory+ '/Stopword filtered files/'+ file.name
#     nf = open(newPath,"a")
#     for token in newTokens:
#         nf.write(token)
#         nf.write("\n")


print("**************** files after StopWords removal *****************\n")
files = Path(newDirectory+ '/Stopword filtered files').glob('*')
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1






print("***********************************Punctuation filtering*****************************************\n")
files = Path(newDirectory+ '/Stopword filtered files').glob('*')

print("*************** files before Punctuation Removal *****************\n")
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1

# *********************Logic************************
# os.mkdir("Preprocessed files/Punctuation filtered files")
# for file in files:
#     f = open(file,"r")
#     content = f.readlines()
#     newTokens = []
#     for word in content:
#         word = word.strip()
#         translator = str.maketrans('', '', string.punctuation)
#         newToken = word.translate(translator)
#         newTokens.append(newToken)
#     print(content)
#     print(newTokens)

#     newPath = newDirectory+ '/Punctuation filtered files/'+ file.name
#     nf = open(newPath,"a")
#     for token in newTokens:
#         nf.write(token)
#         nf.write("\n")


print("**************** files after Punctuation removal *****************\n")
files = Path(newDirectory+ '/Punctuation filtered files').glob('*')
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1





print("**************************************Whitespace filtering*******************************************\n")
files = Path(newDirectory+ '/Punctuation filtered files').glob('*')

print("**************** files before Whitespace removal *****************\n")
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1    

# ************************Logic****************************
# os.mkdir("Preprocessed files/Whitespace filtered files")
# for file in files:
#     f = open(file,"r")
#     content = f.readlines()
#     newTokens = []
#     for word in content:
#         newToken = word.strip()
#         if(newToken != ''):
#             newTokens.append(newToken)
#     print(content)
#     print(newTokens)

#     newPath = newDirectory+ '/Whitespace filtered files/'+ file.name
#     nf = open(newPath,"a")
#     for token in newTokens:
#         nf.write(token)
#         nf.write("\n")
    

print("**************** files after Whitespace removal *****************\n")
files = Path(newDirectory+ '/Whitespace filtered files').glob('*')
i = 0
for file in files:
    if(i == 5):
        break
    print("********"+"file "+str(i+1)+"**********")
    f = open(file,"r")
    content = f.read()
    print(content)
    print("\n")
    i += 1

print("******************************************Pre Processing Ends******************************************")