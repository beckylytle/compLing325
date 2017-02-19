t = "The government's borrowing authority dropped at midnight Tuesday to 2.80 trillion dollars. Legislation to lift the debt ceiling is ensnarled in the fight over cutting taxes. The House has voted to raise the ceiling to 3.1 trillion dollars, but the Senate isn't expected to act until next week at the earliest. The Treasury said the United States will default if Congress doesn't act. Vitulli was named senior vice president and general manager of the United States sales and marketing arm of Japanese auto maker Mazda. In the new position he will oversee Mazda's American sales, service, parts, and marketing operations."

t2 = [('The', 'AT'), ("government's", 'NN$'), ('borrowing', 'VBG'), ('authority', 'NN'), ('dropped', 'VBD'), ('at', 'IN'), ('midnight', 'NN'), ('Tuesday', 'NN'), ('to', 'IN'), ('2.80', 'CD'), ('trillion', 'CD'), ('dollars', 'NNS'), ('.','.'),('Legislation', 'NN'), ('to', 'TO'), ('lift', 'VB'), ('the', 'AT'), ('debt', 'NN'), ('ceiling', 'NN'), ('is', 'BEZ'), ('ensnarled', 'VBN'), ('in', 'IN'), ('the', 'AT'), ('fight', 'NN'), ('over', 'IN'), ('cutting', 'VBG'), ('taxes', 'NNS'), ('.','.'), ('The', 'AT'), ('House', 'NP'), ('has', 'VBZ'), ('voted', 'VBN'), ('to', 'TO'), ('raise', 'VB'), ('the', 'AT'), ('ceiling', 'NN'), ('to', 'IN'), ('3.1', 'CD'), ('trillion', 'CD'), ('dollars', 'NNS'), (',',','), ('but', 'CC'), ('the', 'AT'), ('Senate', 'NNP'), ('is', 'BEZ'),("n't",'*'), ('expected', 'VBD'), ('to', 'TO'), ('act', 'VB'), ('until', 'IN'), ('next', 'JJ'), ('week', 'NN'), ('at', 'IN'), ('the', 'AT'), ('earliest', 'JJT'),('.','.'), ('The', 'AT'), ('Treasury', 'NNP'), ('said', 'VBD'), ('the', 'AT'), ('United', 'NNP'), ('States', 'NNPS'), ('will', 'MD'), ('default', 'VB'), ('if', 'CS'), ('Congress', 'NNP'), ('does', 'DOZ'),("n't",'*'),('act', 'VB'),('.','.'),('Vitulli', 'NNP'), ('was', 'BEDZ'), ('named', 'VBN'), ('senior', 'JJ'), ('vice', 'NN'), ('president', 'NN'), ('and', 'CC'), ('general', 'JJ'), ('manager', 'NN'), ('of', 'IN'), ('the', 'AT'), ('United', 'NNP'), ('States', 'NNPS'), ('sales', 'NNS'), ('and', 'CC'), ('marketing', 'NN'), ('arm', 'NN'), ('of', 'IN'), ('Japanese', 'JJ'), ('auto', 'NN'), ('maker', 'NN'), ('Mazda', 'NNP'),('.','.'), ('In', 'IN'), ('the', 'AT'), ('new', 'JJ'), ('position', 'NN'), ('he', 'PRP'), ('will', 'MD'), ('oversee', 'VB'), ("Mazda's", 'NNP'), ('American', 'JJ'), ('sales', 'NNS'),(',',','), ('service', 'NN'),(',',','), ('parts,', 'NNS'),(',',','), ('and', 'CC'), ('marketing', 'NN'), ('operations', 'NNS'),('.','.')]
t3 = [('The', 'AT'), ("government's", 'NN$-TL'), ('borrowing', 'VBG'), ('authority', 'NN'), ('dropped', 'VBD'), ('at', 'IN'), ('midnight', 'NN'), ('Tuesday', 'NR'), ('to', 'TO'), ('2.80', 'UNK'), ('trillion', 'CD'), ('dollars', 'NNS'), ('.', '.'), ('Legislation', 'NN'), ('to', 'TO'), ('lift', 'VB'), ('the', 'AT'), ('debt', 'NN'), ('ceiling', 'NN'), ('is', 'BEZ'), ('ensnarled', 'UNK'), ('in', 'IN'), ('the', 'AT'), ('fight', 'NN'), ('over', 'IN'), ('cutting', 'VBG'), ('taxes', 'NNS'), ('.', '.'), ('The', 'AT'), ('House', 'NN'), ('has', 'HVZ'), ('voted', 'VBD'), ('to', 'TO'), ('raise', 'VB'), ('the', 'AT'), ('ceiling', 'NN'), ('to', 'TO'), ('3.1', 'CD'), ('trillion', 'CD'), ('dollars', 'NNS'), (',', ','), ('but', 'CC'), ('the', 'AT'), ('Senate', 'NN-TL'), ('is', 'BEZ'), ("n't", '*'), ('expected', 'VBN'), ('to', 'TO'), ('act', 'NN-TL'), ('until', 'CS'), ('next', 'AP'), ('week', 'NN'), ('at', 'IN'), ('the', 'AT'), ('earliest', 'JJT'), ('.', '.'), ('The', 'AT'), ('Treasury', 'NN-TL'), ('said', 'VBD'), ('the', 'AT'), ('United', 'VBN-TL'), ('States', 'NNS-TL'), ('will', 'MD'), ('default', 'NN'), ('if', 'CS'), ('Congress', 'NP'), ('does', 'DOZ'), ("n't", '*'), ('act', 'NN-TL'), ('.', '.'), ('Vitulli', 'UNK'), ('was', 'BEDZ'), ('named', 'VBN'), ('senior', 'JJ'), ('vice', 'NN'), ('president', 'NN-TL'), ('and', 'CC'), ('general', 'JJ'), ('manager', 'NN'), ('of', 'IN'), ('the', 'AT'), ('United', 'VBN-TL'), ('States', 'NNS-TL'), ('sales', 'NNS'), ('and', 'CC'), ('marketing', 'VBG'), ('arm', 'NN'), ('of', 'IN'), ('Japanese', 'JJ'), ('auto', 'NN'), ('maker', 'NN'), ('Mazda', 'UNK'), ('.', '.'), ('In', 'IN'), ('the', 'AT'), ('new', 'JJ'), ('position', 'NN'), ('he', 'PPS'), ('will', 'MD'), ('oversee', 'UNK'), ("Mazda's", 'UNK'), ('American', 'JJ'), ('sales', 'NNS'), (',', ','), ('service', 'NN'), (',', ','), ('parts', 'NNS'), (',', ','), ('and', 'CC'), ('marketing', 'VBG'), ('operations', 'NNS'), ('.', '.')]

countC = {}
countW = {}
for i in range(1,len(t2)-1):
    if not t2[i][1] == t3[i][1] and not t3[i][1] == 'UNK':
        print i
        #print 'Correct',t2[i][1]
        #print 'Wrong',t3[i][1]
        if t2[i][1] in countC.keys():
            countC[t2[i][1]]+=1
        else:
            countC[t2[i][1]]=1
        if t3[i][1] in countW.keys():
            countW[t3[i][1]]+=1
        else:
            countW[t3[i][1]]=1
        if t2[i][1] == 'NNP':
            print t3[i][1]
            print t2[i-1][1],t2[i+1][1]
print countC
print countW
