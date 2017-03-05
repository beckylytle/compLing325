#NAME: Becky Lytle
import copy

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','TWA','does','from','to','on','near','through'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':['that','this','a'],'Noun':['book','flight','meal','money'],'Verb':['book','include','prefer'],'Pronoun':['I','she','me'],'Proper-Noun':['Houston','TWA'],'Aux':['does'],'Preposition':['from','to','on','near','through']}


"""Part 1: Chomsky Normal Form"""

def InCNF(g,terminals,nonterminals):
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

def miniCheck(l,r,terminals,nonterminals):
    if type(r)==type('') and r in terminals:
        return True
    elif type(r)==type('') and not r in terminals:
        return False #this is unlikely
    else:
        if len(r) < 2:
            return False
        elif len(r) > 2:
            return False
        elif not r[0] in nonterminals or not r[1] in nonterminals:
            return False
        else:
            return True

def checkUnit(grammar):
    for left in grammar:
        for right in grammar[left]:
            if type(right)!=type('') and len(right)==1:
                return False
    return True

def UnitProductions(grammar):
    newg = copy.deepcopy(grammar)
    for left in grammar:
        for right in grammar[left]:
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
    check = checkUnit(newg)
    if check:
        return newg
    else:
        #print newg
        return UnitProductions(newg)

def ConvertToCNF(g,i,terminals,nonterminals):
    # This function takes a grammar and returns an equivalent grammar in Chomsky Normal Form
    # PASS IN i AS 0!!!!!
    newG = {}
    for key in g:
        newG[key] = []
    for leftSide in g:
        for val in g[leftSide]:
            cnf = miniCheck(leftSide,val,terminals,nonterminals)
            if not cnf: #Run Thru 3 Cases
                if len(val)>2:
                    #im gonna do this sloppily bc i think itll end up working
                    new = val[0:2] #get the first two things
                    other = val[2:] #get the rest of the things
                    dummy = 'X' + str(i)
                    i+=1 #update i so we never make the same dummy var again
                    newG[dummy] = [new]
                    newrule = [dummy] + other
                    newG[leftSide] += [newrule] #incorporate into old rule
                    # a better way to do this would be to make a helper function that loops thru the rule til its ok
                    #print 'CASE 1'
                    #print 'added ',leftSide,'-->',newrule,' and ',dummy,'-->',new
                    nonterminals.add(dummy)
                elif len(val)<2:
                    #this shouldn't be happening
                    print leftSide,val
                    print "something is wrong...!"
                    exit()
                else:
                    if not val[0] in nonterminals:
                        baby = val[0] #bc its like the tiny baby letter!!
                        dummy = 'X' + str(i)
                        i+=1 #update i so we never make the same dummy var again
                        newG[dummy] = [baby]
                        newG[leftSide] += [[dummy,val[1]]]
                        #print 'CASE 2'
                        #print 'added ',leftSide,'-->',dummy,val[1],' and ',dummy,'-->',[baby]
                        nonterminals.add(dummy)
                    else:
                        baby = val[1] #bc its like the tiny baby letter!!
                        dummy = 'X' + str(i)
                        i+=1 #update i so we never make the same dummy var again
                        newG[dummy] = [baby]
                        newG[leftSide] += [[val[0],dummy]]
                        #print 'CASE 3'
                        #print 'added ',leftSide,'-->',val[0],dummy,' and ',dummy,'-->',[baby]
                        nonterminals.add(dummy)

            if cnf:
                newG[leftSide]+=[val] #Add to our new grammar
    #At the end...
    check = InCNF(newG,terminals,nonterminals)
    if check == True:
        return newG
    else:
        return ConvertToCNF(newG,i,terminals,nonterminals) #do it again? maybe not the most efficient method

"""
terminals = ['e']
nonterminals = ['S','A','B','C']
grammar = {'S':[['A','B','C'],['A']],'A':[['C']],'B':[['A'],['B','C']],'C':['e'] }
"""
#g=UnitProductions(grammar)
#print g
#newg=ConvertToCNF(g,0,terminals,nonterminals)
#print newg
#print InCNF(newg,terminals,nonterminals)

"""Part 3: CKY Algorithm"""

# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise.

def helper(g,v1,v2):
    answer = []
    for left in g:
        for right in g[left]:
            if type(right)!=type(''):
                if right[0]==v1 and right[1]==v2:
                    answer+=[left]
    return answer


def CKYRecognizer(g,s):
    s=s.split()
    size=len(s)
    #create n x n matrix
    #columns correspond to word in s
    #for example, matrix[n][m] corresponds to word m in row n
    matrix = []
    for n in range(0,size):
        matrix += [[]]
        for m in range(0,size):
            matrix[n] += [[]]
    #first, go along diagonal!!
    for i in range(0,size):
        word = s[i]
        #current = matrix[i][i]
        #go thru grammar and see if word is ever on the right side ..
        for rule in g:
            if word in g[rule]:
                matrix[i][i] += [rule]
    #now..go along the upper diagonals until u reach matrix[0][n]
    for j in range(1,size):
        #each loop of j represents a new diagonal we will go along ..
        length = size-j #this is how long the diagonal is
        row = 0
        col = j
        for k in range(0,length):
            #current box = matrix[row][col]
            #after filling this box, we do row+=1, col+=1
            #for this box, we must check all of the relevant combos!!
            #aka [ (row,row) & (row+1,col), (row,row+1) & (row+2,col) ... (row,col-1) & (col,col) ]
            #and for all of those combos we have to check the actual combos of stuff in the BOXES
            #print ('BOX',row,col)
            for val in range(row,col):
                first = (row,val)
                firstbox = matrix[row][val]
                second = (val+1,col)
                secondbox = matrix[val+1][col]
                #print first,second
                #print firstbox,secondbox
                for v in range(0,len(firstbox)):
                    for x in range(0,len(secondbox)):
                        val1= firstbox[v]
                        val2= secondbox[x]
                        combo = helper(g,val1,val2) #CALL HELPER FUNCTION TO SEE IF ANY RELEVANT GRAMMAR RULES
                        #now see if these r ever seen together!!
                        for t in combo:
                            matrix[row][col] += [t]
            row+=1
            col+=1
    if 'S' in matrix[0][size-1]:
        return True
    else:
        return False



"""Extra Credit"""

# Extra Credit (optional): Modify your CKYRecognizer function to instead return a valid parse of the string, if one exists.

def CKYParser(g,s):

    # Fill in your algorithm here

    return []  # Placeholder


"""Demonstrations"""

print InCNF(grammar,terminals,nonterminals) # Should return False!

grammar = UnitProductions(grammar) #NECESSARY STEP!!! I added this helper function to help w/ ConvertToCNF
newgrammar = ConvertToCNF(grammar,0,terminals,nonterminals)

print newgrammar

print InCNF(newgrammar,terminals,nonterminals) # Should return True!

print CKYRecognizer(newgrammar,'book that flight through Houston') # Should return True!

"""Add more tests of CKYRecognizer here."""



# Extra Credit: Add tests of CKYParse here.
