import re
fr=open(r'cut_genes.fa','r')
fw=open('data.fa','w')#output the results in a new fasta file

seq1={}
for line in fr:
    if line.startswith('>'):#find out gene name
        name=line.split()[0]
        seq1[name]=''#put gene name in the dictionary seq1
    else:
        seq1[name]+=line.replace('\n','')
        #sequence in several lines combine into single line
        #put them into a dictionary

for i in seq1.keys():
    x=str(seq1[i])
    cut=x.count('GAATTC')
    c=str(cut+1)#number of fragments
    fw.write(i)
    fw.write(' ')
    fw.write(c)
    fw.write('\n')
    fw.write(seq1[i])
    fw.write('\n')
fr.close()


