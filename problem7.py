#number 7
import math

def soso(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1


count=0
a=1
while count!=10001:
    a=a+1
    if soso(a)==1:
        count=count+1
    
print a
