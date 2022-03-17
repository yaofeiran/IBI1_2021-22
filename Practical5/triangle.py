#Repeat 10 times
#y=1+2+3+...+n-1+n
#for (n-1)th triangle,y=x
#then for nth triangle,y=x+n
#set the last sum as x, the number of triangle as n,sum of the current triangle as y
#start as n=1,x=0
#end when n=10 
x=0
for n in range(1,11):
  y=x+n
#x becomes y,which is the last sum
  x=y
#repeat
  print(n,y)
  
 
