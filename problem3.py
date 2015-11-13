#number3
import math

def soso(num):
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1


a=600851475143
b=int(math.sqrt(a))
while b!=1:
    if a%b==0:
        if soso(b)==1:
            print b      
    b= b-1
