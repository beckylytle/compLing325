# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import treebank
from nltk.tree import Tree
"""
>>> from nltk.tree import Tree
>>> print(Tree(1, [2, Tree(3, [4]), 5]))
(1 2 (3 4) 5)
>>> vp = Tree('VP', [Tree('V', ['saw']),
...                  Tree('NP', ['him'])])
>>> s = Tree('S', [Tree('NP', ['I']), vp])
>>> print(s)
(S (NP I) (VP (V saw) (NP him)))
>>> print(s[1])
(VP (V saw) (NP him))
>>> print(s[1,1])
(NP him)
>>> t = Tree.fromstring("(S (NP I) (VP (V saw) (NP him)))")
>>> s == t
True
>>> t[1][1].set_label('X')
>>> t[1][1].label()
'X'
>>> print(t)
(S (NP I) (VP (V saw) (X him)))
>>> t[0], t[1,1] = t[1,1], t[0]
>>> print(t)
(S (X him) (VP (V saw) (NP I)))
"""


"""
Your task for the lab is to write a rule-based syntactic transfer function that takes a Tree and
returns another Tree. For example, your function might implement the change from NP-->
Adjective Noun to NP--> Noun Adjective, in which case it would have to identify such an NP
in the Tree and recreate it with the component Adjective and Noun in the opposite order.
"""

def S_Transfer(tree,v1,v2):
    #i'm assuming this is a binary tree and idk if that is right
    #update: it is not a binary tree so u need to fix this lol
    for i in range(0,len(tree)):
        #check i & i+1
        if i!=len(tree)-1 and tree[i].label() in v1 and tree[i+1].label() in v2:
        #switch!
            left = tree[i]
            right = tree[i+1]
            tree[i] = right
            tree[i+1] = left
    for j in range(0,len(tree)):
        if len(tree[j])>1:
            tree[j] = S_Transfer(tree[j],v1,v2)
        #recursive call
    return tree

"""
#These were my mini tests!
vp = Tree('VP', [Tree('V', ['saw']), Tree('NP', ['him'])])
s = Tree('S', [Tree('NP', ['I']), vp])
t = Tree.fromstring("(S (NP (D the) (NN dog)) (VP (V chased) (NP (D the) (JJ green) (NN cat))))")
"""

#Implementing the ( Adjective Noun --> Noun Adjective ) rule
s1=treebank.parsed_sents('wsj_0011.mrg')[3]
first = ['JJ','JJR','JJS'] #all types of adjectives
second = ['NN','NNS','NNP','NNPS'] #all types of nouns
testSentence = S_Transfer(s1,first,second)
print testSentence


#//////////////////////////////////////////////////////////////////////////////////////////////////////
#                                               EXTRA CREDIT
#//////////////////////////////////////////////////////////////////////////////////////////////////////

languageDict = {'*T*-12':'*T*-12','South':'Sur','Korea':'Corea',"'s":"'s",'boom':'auge','economic':'económico','which':'cual','began':'empezó','in':'en','1986':'1986','stopped':'detenido','this':'esta','year':'año','because':'porque','of':'de','prolonged':'prolongado','labor':'trabajo','disputes':'disputas',',':',','trade':'comercio','conflicts':'conflictos','and':'y','exports':'exportaciones','sluggish':'lento','.':'.'}

def L_Transfer(d,tree):
    print tree,tree[0],type(tree[0])
    if str(tree[0]) in d.keys():
        u = unicode(d[tree[0]], "utf-8")
        tree[0] = u
    else:
        for i in range(0,len(tree)):
            tree[i]=L_Transfer(d,tree[i]) #recursive call
    return tree

newSentence = L_Transfer(languageDict,testSentence)
print newSentence
