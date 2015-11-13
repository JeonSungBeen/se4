#number4
def pen(num):
    a=len(str(num))
    if num/(10**(a-1)) == num%10:
        if (num/(10**(a-2)))%10 == ((num%100)/10):
            if (num/(10**(a-3)))%10 == ((num%1000)/100):
                return 1
    else:
        return 0
    
max=0    
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if pen(i*j)==1:
            if max< i*j:
                max=i*j
                print i*j
