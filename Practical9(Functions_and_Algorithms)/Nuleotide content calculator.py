def count_nucleo(DNA):
    """Input:DNA,a string
       Count A,a,T,t,C,c,G,g
       Add them up and divide by the lengths
       Return percentage
    """
    A=DNA.count("a")
    T=DNA.count("t")
    C=DNA.count("c")
    G=DNA.count("g")
    a=A/len(DNA)
    t=T/len(DNA)
    c=C/len(DNA)
    g=G/len(DNA)
    print('percent of A:{:.2f}%'.format(a*100))
    print('percent of T:{:.2f}%'.format(t*100))
    print('percent of C:{:.2f}%'.format(c*100))
    print('percent of G:{:.2f}%'.format(g*100))

DNA1=input("DNA strand: ")
DNA=DNA1.lower()
count_nucleo(DNA)


#example:
#input: Atcatcatc
#It returns :
#percent of A:33.33%
#percent of T:33.33%
#percent of C:33.33%
#percent of G:0.00%

