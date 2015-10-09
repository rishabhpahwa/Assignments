import random
def twochk(a,alp):
	for i in range(alp):
		x=random.randrange(0,len(a))
		y=random.randrange(0,len(a))
		if y>x and a[x]>a[y]:
			a[x],a[y]=a[y],a[x]
			i=i+1
		elif x>y and a[y]>a[x]:
			a[x],a[y]=a[y],a[x]
			i=i+1
		else:
			continue
	
	print "The randomly sorted array is:\n",a
n=input("Enter the array elements separated by spaces\n")
r=int(raw_input("Enter the value of alpha: "))
twochk(n,r)
