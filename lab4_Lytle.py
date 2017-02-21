#NAME: Becky Lytle

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','NWA','does','from','to','on','near','through'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':['that','this','a'],'Noun':['book','flight','meal','money'],'Verb':['book','include','prefer'],'Pronoun':['I','she','me'],'Proper-Noun':['Houston','TWA'],'Aux':['does'],'Preposition':['from','to','on','near','through']}


"""Part 1: Chomsky Normal Form"""

def InCNF(g):
    # takes a grammar and returns True if that grammar is in CNF and False otherwise.
    value = True
    for leftSide in g:
        for val in g[leftSide]:
            if type(val)==type(''): #so like, if the value in the list is a string:
                if not val in terminals: #CHECK THAT THEY'RE TERMINALS
                    value = False
            else: #this is the case where the value in the list is a list
                if not len(val) == 2: #CHECK LENGTH
                    value = False
                else:
                    if not val[0] in nonterminals or not val[1] in nonterminals: #CHECK THAT THEYRE NONTERMINALS
                        value = False
    return value

"""Part 2: Converting to Chomsky Normal Form"""

def ConvertToCNF(g):
    # This function takes a grammar and returns an equivalent grammar in Chomsky Normal Form

    return True # Placeholder


"""Part 3: CKY Algorithm"""

# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise.

def CKYRecognizer(g,s):

   # Fill in your algorithm here

   return True  # Placeholder


"""Extra Credit"""

# Extra Credit (optional): Modify your CKYRecognizer function to instead return a valid parse of the string, if one exists.

def CKYParser(g,s):

    # Fill in your algorithm here

    return []  # Placeholder


"""Demonstrations"""

print InCNF(grammar) # Should return False!

newgrammar = ConvertToCNF(grammar)

print newgrammar

print InCNF(newgrammar) # Should return True!

print CKYRecognizer(newgrammar,'Book the flight through Houston') # Should return True!

# Add more tests of CKYRecognizer here.



# Extra Credit: Add tests of CKYParse here.
