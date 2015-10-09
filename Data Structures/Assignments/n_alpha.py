import random
import time
import matplotlib.pyplot as plt
plt.ion()
def gen_ran(l,max_e):
	a=[]
	for i in range(0,l-1):
		a.append(random.randrange(0,max_e))
	return a
def two_chk(a):
	count=0
	while True:
		count+=1
		x=random.randrange(0,len(a))
		y=random.randrange(0,len(a))
		if y>x and a[x]>a[y]:
			a[x],a[y]=a[y],a[x]
		elif x>y and a[y]>a[x]:
			a[x],a[y]=a[y],a[x]
		if chk_sort(a)==True:
			return count
		else:
			continue
def chk_sort(ar):
	flag=0
	for i in range(0,len(ar)-1):
		if ar[i]>ar[i+1]:
			flag=0
			break
		elif ar[i]<ar[i+1]:
			flag=1
			continue
	if flag==1:
		return True
	else:
		return False
print "Random arrays are being checked, stay patient! :)"
j=0
c=[]
for i in range(50,300):
	sum=0
	for j in range(0,20):
		a=gen_ran(i,1000)
		sum=sum+two_chk(a)
	c.append(sum/20)
	print "Array elements: ",i,"\tIterations: ",c[i-50]
plt.plot(c)
plt.show()
plt.savefig('plot.png')