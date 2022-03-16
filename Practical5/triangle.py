#Repeat,set the last sum as x, the number of triangle as n,sum of the current triangle as y
x=0
for n in range(1,11):
#x is the bridge
  y=x+n
#x becomes y,which is the last sum
  x=y
#Done!
  print(n,y)
  
 
