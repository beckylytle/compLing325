import nltk
from nltk.book import *

def countStr(word):
    files = inaugural.fileids()
    for speech in files:
        year = speech[0:4] #save year as string
        allWords = inaugural.words(speech)
        num = allWords.count(word)
        print year,num

print countStr('country')
