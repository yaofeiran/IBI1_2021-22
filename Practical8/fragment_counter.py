import re
seq ='ATGCAATCGACTACGATCAATCGAGGGCC'
cut=seq.count("GAATTC")
fragment=cut+1
print('the number of fragments is ',fragment)
