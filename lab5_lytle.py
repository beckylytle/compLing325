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
    if tree[0].label() == v1 and tree[1].label() == v2:
        #switch!
        left = tree[0]
        right = tree[1]
        tree[0] = right
        tree[1] = left
    if len(tree[0])>1:
        tree[0] = S_Transfer(tree[0],v1,v2)
        #recursive call
    if len(tree[1])>1:
        tree[1] = S_Transfer(tree[1],v1,v2)
        #recursive call
    return tree

#test sentence
vp = Tree('VP', [Tree('V', ['saw']), Tree('NP', ['him'])])
s = Tree('S', [Tree('NP', ['I']), vp])

testSentence = S_Transfer(s,'NP','VP')
print testSentence
