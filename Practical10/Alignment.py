import pandas as pd
import re
seq1=open('DLX5_human.fa','r')
seq2=open('DLX5_mouse.fa','r')
seq3=open('RandomSeq(1).fa','r')
#read sequence as string
def read(seq):
    for line in seq:
        line = line.rstrip()
        if line.startswith('>'):
            continue
        else:
            seq=line.replace('\n','')
        return seq
#use function
seq1=read(seq1)
seq2=read(seq2)
seq3=read(seq3)  
#read BLOSUM62 matrix
blo=pd.read_excel('BLOSUM.xlsx')
#compare each amino acid
def score(a,b):
     value=0
     for i in range(len(a)):
         X=a[i]
         Y=b[i]
         #location in the BLOSUM62 excel
         Z=blo.loc[blo['First']==X,Y]#Z indicates the score
         score=int(Z)#integar
         value +=score
     return value
#use function for  each pairwise
hm=score(seq1,seq2)
hr=score(seq1,seq3)
mr=score(seq2,seq3)
print("alignment socre of human-mouse:",hm)
print("alignment score of human-random:",hr)
print("alignment score of mouse-random:",mr)
#compute the percentage of indentical amino acid
def percentage(c,d):
    p=0
    for i in range(len(c)):
        if c[i]==d[i]:
            p +=1
        percentage=p/len(c)
    return percentage
hm1=percentage(seq1,seq2)
hr1=percentage(seq1,seq3)
mr1=percentage(seq2,seq3)
print("Identical amino acid percentage of human-mouse:",'percent:{:.2%}'.format(hm1))
print("Identical amino acid percentage of human-random:",'percent:{:.2%}'.format(hr1))
print("Identical amino acid percentage of mouse-random:",'percent:{:.2%}'.format(mr1))
