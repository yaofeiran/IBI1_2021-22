def count_nucleo(DNA):
    """Input:DNA,a string
       Count A,a,T,t,C,c,G,g
       Add them up and divide by the lengths
       Return percentage
    """
    A=DNA.count("A")
    a=DNA.count("a")
    T=DNA.count("T")
    t=DNA.count("t")
    C=DNA.count("C")
    c=DNA.count("c")
    G=DNA.count("G")
    g=DNA.count("g")
    nucleotide=A+a+T+t+C+c+G+g
    percentage=nucleotide/len(DNA)
    return percentage

DNA=input("DNA strand: ")
a=count_nucleo(DNA)
print('percent:{:.2f}%'.format(a*100))

#example:
#input your DNA strand
#conut_nucleo(DNA)
#It returns the precenatge of nucleotide

