# Name: 

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','NWA','does','from','to','on','near','through'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':['that','this','a'],'Noun':['book','flight','meal','money'],'Verb':['book','include','prefer'],'Pronoun':['I','she','me'],'Proper-Noun':['Houston','TWA'],'Aux':['does'],'Preposition':['from','to','on','near','through']}

# This function determines whether a grammar is in Chomsky Normal Form

def InCNF(g):

    # Fill in your algorithm here


    return True # Placeholder

# This function takes a grammar and returns an equivalent grammar in Chomsky Normal Form

def ConvertToCNF(g):

    # Fill in your algorithm here

    return {} # Placeholder


# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise. 

def CKYRecognizer(g,s):

   # Fill in your algorithm here

   return True  # Placeholder



# Extra Credit (optional): Modify your CKYRecognizer function to instead return a valid parse of the string, if one exists.

def CKYParser(g,s):

    # Fill in your algorithm here

    return []  # Placeholder


# Demonstrations

print InCNF(grammar) # Should return False!

newgrammar = ConvertToCNF(grammar)

print newgrammar

print InCNF(newgrammar) # Should return True!

print CKYRecognizer(newgrammar,'Book the flight through Houston') # Should return True!

# Add more tests of CKYRecognizer here.



# Extra Credit: Add tests of CKYParse here.






