chd={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
print(chd)
import numpy as np
import matplotlib.pyplot as plt
N=10
chd=(1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)
age=(30,35,40,45,50,55,60,65,70,75)
plt.scatter(chd,age,marker='o')
plt.title('Paternal age on offspring health')
plt.xlabel('paternal age')
plt.ylabel('chd')
plt.show()
