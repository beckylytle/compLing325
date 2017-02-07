import nltk
from nltk.corpus import brown
#from nltk.book import *
#from text import *

def MostLikelyTag(word):
    text=brown.tagged_words()
    saved={}
    """Actually collect all the seen tags"""
    for w in text:
        if w[0] == word:
            tag=w[1]
            try:
                saved[tag] = saved[tag] + 1 #aka if this tag has already been seen
            except KeyError:
                saved[tag] = 1 #if this is the first time we've seen the tag
    """Now find the one seen most often"""
    maxnum = 0
    maxtag = None
    for t in saved.keys():
        if maxnum == 0:
            maxnum = saved[t]
            magtag = t
        else:
            if saved[t] > maxnum:
                maxnum = saved[t]
                maxtag = t
    print saved
    return maxtag
    #takes a word as an input parameter and returns its 'most likely' POS tag
    #Which tag is most likely should be determined using the Brown corpus in NLTK.
    #Remember you can access the tagged corpus with brown.tagged_words()
    #return UNK if the word is not found


print MostLikelyTag('state')
#print MostLikelyTag('around')

def ApplyMLTag(text):
    #takes a text and tags each word with its most likely tag
    #You should 'tag' each word using the format of the NLTK taggers (i.e., make a tuple with the word and its tag).
    #This means your function takes a list of words as input and returns a list of tuples as its output.
    seen = {}
    for w in text:
        if w in seen.keys():
            tag = seen[w] #save tag
        else:
            tag = MostLikelyTag(w) #call function
            seen[w] = tag #save answer in dictionary
    return True

def Processing(text):
    #use this to separate any punctuation from words after using t.split() to make a list
    return True
