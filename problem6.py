#number6
def sumsqu(num):
    a=0
    for i in range(num+1):
        a=a+i
    return a**2
    

def squsum(num):
    a=0
    for i in range(num+1):
        a=a+i*i
    return a
    
print sumsqu(100)-squsum(100)
