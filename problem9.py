 #number 9
for a in range(1,333):
    for b in range(a+1,500):
        for c in range(333,a+b):
            if (a+b+c==1000)&(a**2 + b**2 == c**2):
                print a*b*c
                print a,b,c
                break
