#number2
tot=2
x1=1
x2=2
x3=0
while x3<4000000:
    if x3%2==0:
        tot= tot+x3
    x3=x1+x2
    x1=x2
    x2=x3
print tot
