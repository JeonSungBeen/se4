import math
def soso(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			return 0
	return 1

tot =0
count=2
while count != 2000000:
	if soso(count)==1:
		tot = tot+count
	count = count+1

print tot
