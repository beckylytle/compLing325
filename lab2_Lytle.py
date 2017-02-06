import nltk
from nltk.book import *

"""Based on the results what can you say about the lexical diversity of the three texts?
(for text2, text4, & text6)

My answer: (texts w/ their lexical diversity scores)
text6 - 7.83
text4 - 14.94
text2 - 20.72

It seems that a lower lexical diversity score means that there are more unique words in that text.
Therefore, text6 seems to have the most lexical diversity.
"""
def LexicalDiversity(words):
    #returns the lexical diversity of a given list of words
    # So, I think LD = # of total words / # of unique words (Check with Jane?)
    uniquewords = set(words)
    ratio = float(len(words))/len(uniquewords)
    return ratio

"""Based on the results what can you say about the percentage use of "the" of the three texts?
(for text2, text4, & text6)

My answer: (texts w/ their percentage use of 'the')
text6 - 1.76%
text4 - 6.37%
text2 - 2.73%

Text4 has the highest percentage of the word "the"!
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

How many words in this corpus with prefix "un"? (uppercase & lowercase)
Answer: 14,516 words

Hypothesis: There will be more words with the suffix "er" than there are with the prefix "un"
Result: 11,026 words

I was wrong! There are more words with the "un" prefix.
"""
def FindPrefix(prefix,string): #takes a boolean value (if it's a prefix or not) & a string
    if prefix == True:
        lenPrefix = len(string)
        wordlist = nltk.corpus.words.words('en')
        wordsWithPrefix = [w for w in wordlist if w[0:lenPrefix]==string]
        wordsWithLowerCasePrefix = [w for w in wordlist if w[0:lenPrefix]==string.lower()]
        return len(wordsWithPrefix)+len(wordsWithLowerCasePrefix)
    else:
        lenPrefix = len(string)
        wordlist = nltk.corpus.words.words('en')
        wordsWithPrefix = [w for w in wordlist if w[-lenPrefix:]==string]
        return len(wordsWithPrefix)

word = 'Un'
print FindPrefix(True,word) #assuming we pass in prefix as Uppercase first letter
