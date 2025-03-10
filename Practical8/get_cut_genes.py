import re
fr=open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#read original file
fw=open('cut_genes.fa','w')#output the results in a new fasta file

seq={}
for line in fr:
    if line.startswith('>'):#find out gene name
        name ="".join(re.findall(r"gene:([^ ]+) gene_biotype", line))
        seq[name]=""
        #put gene name in the dictionary seq
    else:
        seq[name]+=line.replace('\n','')
        #sequence in several lines combine into single line
        #put them into a dictionary
fr.close()

for i in list(seq.keys()):
    if not 'GAATTC' in seq[i]:
        del seq[i]
        continue# delete genes that cannot be cut by EcoRI
x={}
x=seq#key: gene name, value: sequence
for q in x.keys():
    fw.write('>')
    fw.write(q)
    a=len(x[q])
    b=str(a)
    fw.write(' ')
    fw.write(b)
    fw.write('\n')
    fw.write(x[q])
    fw.write('\n')
fr.close()
