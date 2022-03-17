a=19245301
b=4218520
c=271
d=b-c
print("2021-2020 difference d",d)
e=a-b
print("2022-2021 difference e",e)
if d==e:
 print("d=e")
elif d>e:
 print("d>e")
else:
 print("d<e")
#f is the rate of new cases in 2020, g is the rate of the cases in 2021
f=d/c
g=e/b
if f==g:
 print("the rate of new cases is the same")
elif f>g:
 print("2020 has the greater rate of new cases")
else:
 print("2021 has the greater rate of new cases")

X="111"
Y="222"
W=X and Y
print(W)

X="0"
Y="10000"
W=X and Y
print(W)

X=3
Y="string"
W=X and Y
print(W)

X=True
Y=False
W=X and Y
print(W)

X=False
Y=True
W=X and Y
print(W)

X="False"
Y="True"
W=X and Y
print(W)

X=0
Y=111
W=X and Y
print(W)

X=1
Y=111
W=X and Y
print(W)

X=0
Y="string"
W=X and Y
print(W)
