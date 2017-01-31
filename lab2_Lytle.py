import nltk
from nltk.book import *

"""Based on the results what can you say about the lexical diversity of the three texts?
(for text2, text4, & text6)

My answer:

"""
def LexicalDiversity(words):
    #returns the lexical diversity of a given list of words
    # So, I think LD = # of total words / # of unique words (Check with Jane?)
    uniquewords = set(words)
    ratio = float(words)/uniquewords
    return ratio

"""Based on the results what can you say about the percentage use of "the" of the three texts?
(for text2, text4, & text6)

My answer:

"""
def PercentageUse(word,words):
    #returns the percentage use of a given word in a text (words)
    #words is like, text6 or something and word is 'the'
    listofword = [w for w in words if w==word] #i have never done lists like this ! so cool !!
    wordcount = len(listofword)
    totalwords = len(words)
    percent = (float(wordcount)/totalwords)*100
    return percent,"Percent"


"""
Comment about prefix "un"

How many words in this corpus with prefix "un"?
Answer:

Hypothesis: There will be more words with the suffix "er" than there are with the prefix "un"
Result:
"""
def FindPrefix(prefix,string): #takes a boolean value (if it's a prefix or not) & a string
    if prefix == True:
        lenPrefix = len(string)
        wordlist = nltk.corpus.words.words(‘en’)
        wordsWithPrefix = [w for w in wordlist if w[0:lenPrefix]==string]
        return len(wordsWithPrefix)
    else:
        lenPrefix = len(string)
        wordlist = nltk.corpus.words.words(‘en’)
        wordsWithPrefix = [w for w in wordlist if w[-lenPrefix:]==string]
        return len(wordsWithPrefix)
