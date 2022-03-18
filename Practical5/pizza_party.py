#Repeat:
#p=(n**2+n+2)/2
#When complete?
#once p>=64
# If p less than 64:Keep calculating and print p,n increases
# once p>=64:stop and output a sentence indicating the n enables p>=64
#start as n=0,p=1
n=0
p=(n**2+n+2)/2
while p<64:
  p=(n**2+n+2)/2
  t="when n is "+str(n)+",p is "+str(p)
  print(t)
  n=n+1
  if p>=64:
  #n is n+1 at last step,so minus 1
    n=n-1
    print'when number is straight cut is '+str(n)+', we have enough pieces for each member of IBI class.'
    break
