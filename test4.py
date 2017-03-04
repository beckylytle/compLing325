import copy

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','TWA','does','from','to','on','near','through'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':['that','this','a'],'Noun':['book','flight','meal','money'],'Verb':['book','include','prefer'],'Pronoun':['I','she','me'],'Proper-Noun':['Houston','TWA'],'Aux':['does'],'Preposition':['from','to','on','near','through']}

"""
terminals = ['e']
nonterminals = ['S','A','B','C']
grammar = {'S':[['A','B','C'],['A']],'A':[['C']],'B':[['A'],['B','C']],'C':['e'] }
"""
def UnitProductions(grammar):
    newg = copy.deepcopy(grammar)
    for left in grammar:
        for right in grammar[left]:
            print right
            if len(right)==1 and type(right)!=type(''): #aka if this is a unit production
                #if left-->right is a unit production
                #we wanna find all rules such that right --> x
                #and add left --> x
                RS = right[0]
                RULES = grammar[right[0]]
                for word in RULES:
                    #grammar[left] += [word]
                    newg[left]+=[word]
                #grammar[left].remove([RS])
                newg[left].remove([RS])
    return newg

g=UnitProductions(grammar)
print g
