import nltk
from nltk.corpus import brown
from text import *
import re

def MostLikelyTag(word):
    text=brown.tagged_words()
    saved={}
    """Actually collect all the seen tags"""
    for w in text:
        if w[0] == word or w[0] == word.lower() or w[0]== (word[0].upper()+word[1:]):
            tag=w[1]
            try:
                saved[tag] = saved[tag] + 1 #aka if this tag has already been seen
            except KeyError:
                saved[tag] = 1 #if this is the first time we've seen the tag
    """Now find the one seen most often"""
    maxnum = 0
    maxtag = None
    print saved.keys()
    for t in saved.keys():
        if maxnum == 0:
            maxnum = saved[t]
            maxtag = t
        else:
            if saved[t] > maxnum:
                maxnum = saved[t]
                maxtag = t
    print 'maxtag',maxtag
    if maxtag==None:
        if word == "n't":
            return '*'
        else:
            return 'UNK'
    else:
        return maxtag
    #takes a word as an input parameter and returns its 'most likely' POS tag
    #Which tag is most likely should be determined using the Brown corpus in NLTK.
    #Remember you can access the tagged corpus with brown.tagged_words()
    #return UNK if the word is not found

#print MostLikelyTag('is')
#print MostLikelyTag('state')
#print MostLikelyTag('around')

def ApplyMLTag(text):
    #takes a text and tags each word with its most likely tag
    #You should 'tag' each word using the format of the NLTK taggers (i.e., make a tuple with the word and its tag).
    #This means your function takes a list of words as input and returns a list of tuples as its output.
    tags=[]
    seen = {}
    for w in text:
        if w.lower() in seen.keys(): #check if we've seen this word yet
            tag = seen[w.lower()] #save tag
        else:
            tag = MostLikelyTag(w) #call function
            seen[w.lower()] = tag #save answer in dictionary
        tags+=[(w,tag)]     #add word & tag to list
    return tags

"""example: [ isn't. ] b/c it has two punctuations in one string"""
def Processing(text):
    new_text = []
    for w in text:
        valid = re.match('^[\w-]+$', w) is not None #check if has any punctuation
        if valid == False: #aka, if there is any punctuation
            """DO SOMETHING"""
            val=0
            if "n't" in w:
                cutoff = w.index("n't")
                new_text+=[w[0:cutoff]] #add first part
                new_text+=[w[cutoff:cutoff+3]] #get the n't part too
                if not cutoff+3 == len(w): #if the n't isn't the end of the string
                    new_text+=[w[cutoff+3:]] #add the punctuation
            else:
                for char in w: #go thru characters in word
                    if not char.isalnum(): #IF THIS IS A PUNCTUATION char
                        indexOfChar = w.index(char) #definitely add this
                        firsthalf = w[val:indexOfChar] #definitely add this
                        if not indexOfChar == len(w)-1:
                            secondhalf = w[indexOfChar+1:] #save this bc could have more punctuation in it ..
                        val = indexOfChar+1 #New beginning of string
                        new_text+=[firsthalf]
                        new_text+=[char]
                    else:
                        if w.index(char) == len(w)-1: #if this is the last character
                            new_text+=[w[val:]]

        else:
            new_text += [w] #just add this word as it is to the new text list
    #use this to separate any punctuation from words after using t.split() to make a list
    return new_text

#text = t.split()
#newtext = Processing(text) #process this list of words to separate punctuation!
#tags = ApplyMLTag(newtext)
#print tags

def ApplyTransform(text,transformation):
    # takes a text and a transformation and returns the text with that transformation applied where relevant.
    # assume the transformation is of the form a → b / z __.
    # transformation = [a,b,z] for simplicity
    a = transformation[0]
    b = transformation[1]
    z = transformation[2]
    for i in range(1,len(text)):
        if text[i][1] == a and text[i-1][1] == z: #this is what we lookin for !
            text[i][1] = b #change tag to b
    return text

def CompareTexts(text1,text2):
    # takes two texts and returns the number of tags for which they disagree.
    counter = 0
    for i in range(0,len(text1)): #loop thru all word/tag combos
        if not text1[i][1] == text2[i][1]:
            counter+=1
    return counter

def BestTransform(candidateTransforms,FinalText,MyText):
    #it determines which of the candidateTransforms is the best one.
    #FinalText is the correctly tagged version of the text & MyText is the tagging that my functions did
    best_transformed_text = None
    best_transform = None
    best_errors = None
    for ct in candidateTransforms:
        MyNewText = ApplyTransform(MyText,ct)
        errorcount = CompareTexts(MyNewText,FinalText)
        if best_transform == None:
            best_transformed_text = MyNewText
            best_transform = ct
            best_errors = errorcount
        else:
            if best_errors > errorcount: #aka if this new transformation is better than the previous 1
                best_transformed_text = MyNewText
                best_transform = ct
                best_errors = errorcount
    return best_transform


MyText = [('The', u'AT'), ('government', u'NN'), ("'", u"'"), ('s', u'NP'), ('borrowing', u'VBG'), ('authority', u'NN'), ('dropped', u'VBD'), ('at', u'IN'), ('midnight', u'NN'), ('Tuesday', u'NR'), ('to', u'TO'), ('2', u'CD'), ('.', u'.'), ('80', u'CD'), ('trillion', u'CD'), ('dollars', u'NNS'), ('.', u'.'), ('Legislation', u'NN'), ('to', u'TO'), ('lift', u'VB'), ('the', u'AT'), ('debt', u'NN'), ('ceiling', u'NN'), ('is', u'BEZ'), ('ensnarled', UNK), ('in', u'IN'), ('the', u'AT'), ('fight', u'NN'), ('over', u'IN'), ('cutting', u'VBG'), ('taxes', u'NNS'), ('.', u'.'), ('The', u'AT'), ('House', u'NN'), ('has', u'HVZ'), ('voted', u'VBD'), ('to', u'TO'), ('raise', u'VB'), ('the', u'AT'), ('ceiling', u'NN'), ('to', u'TO'), ('3', u'CD'), ('.', u'.'), ('1', u'CD'), ('trillion', u'CD'), ('dollars', u'NNS'), (',', u','), ('but', u'CC'), ('the', u'AT'), ('Senate', u'NN-TL'), ('is', u'BEZ'), ("n't", '*'), ('expected', u'VBN'), ('to', u'TO'), ('act', u'NN-TL'), ('until', u'CS'), ('next', u'AP'), ('week', u'NN'), ('at', u'IN'), ('the', u'AT'), ('earliest', u'JJT'), ('.', u'.'), ('The', u'AT'), ('Treasury', u'NN-TL'), ('said', u'VBD'), ('the', u'AT'), ('United', u'VBN-TL'), ('States', u'NNS-TL'), ('will', u'MD'), ('default', u'NN'), ('if', u'CS'), ('Congress', u'NP'), ('does', u'DOZ'), ("n't", '*'), ('act', u'NN-TL'), ('.', u'.'), ('Vitulli', UNK), ('was', u'BEDZ'), ('named', u'VBN'), ('senior', u'JJ'), ('vice', u'NN'), ('president', u'NN-TL'), ('and', u'CC'), ('general', u'JJ'), ('manager', u'NN'), ('of', u'IN'), ('the', u'AT'), ('United', u'VBN-TL'), ('States', u'NNS-TL'), ('sales', u'NNS'), ('and', u'CC'), ('marketing', u'VBG'), ('arm', u'NN'), ('of', u'IN'), ('Japanese', u'JJ'), ('auto', u'NN'), ('maker', u'NN'), ('Mazda', UNK), ('.', u'.'), ('In', u'IN'), ('the', u'AT'), ('new', u'JJ'), ('position', u'NN'), ('he', u'PPS'), ('will', u'MD'), ('oversee', UNK), ('Mazda', UNK), ("'", u"'"), ('s', u'NP'), ('American', u'JJ'), ('sales', u'NNS'), (',', u','), ('service', u'NN'), (',', u','), ('parts', u'NNS'), (',', u','), ('and', u'CC'), ('marketing', u'VBG'), ('operations', u'NNS'), ('.', u'.')]
