#number5
def soso(num):
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1

a=1
for i in range(2,21):
    if soso(i)==1:
        a=a*i

for j in range(2,21):
    if a%j!=0:
        if j%2==0:
            a=a*2
        if j%3==0:
            a=a*3
        
print a
