paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
D=dict(zip(paternal_age, chd))#D is the dictionary
print(D)

import numpy as np
import matplotlib.pyplot as plt
N=10#10 ages and relative rate of chd are given
chd=(1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)
age=(30,35,40,45,50,55,60,65,70,75)
# Construct a scatter plot use matplotlib.
plt.scatter(chd,age,marker='o')
plt.title('Paternal age on offspring health')
plt.xlabel('paternal age')
plt.ylabel('chd')
plt.show()
#A variable of the requested paternal age that can be modified
age=30 # This can be modified

#use dictionary to find out the relative rate of chd
print("Paternal age:",age,", rate of congenital heart disease:",D[age])
