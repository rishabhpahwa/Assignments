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
	return a
def inser_sort(a):
        count=0
	for i in range(1,len(a)):
		j=i
		temp=a[i]
		while j>0 and temp<a[j-1]:
		      count+=1
		      a[j]=a[j-1]
		      j=j-1
		a[j]=temp
	return count  
def gen_ran(size,max_e):
        a=[]
        for i in range(0,size):
            a.append(random.randrange(0,max_e))
        return a
def compare(n,r):
	m=n[:]
	c=twochk(m,r)
	t1=inser_sort(n)
	t2=inser_sort(c)
	return (t1,t2)
s=input("Enter the size of the random array desired: ")
r=int(raw_input("Enter the value of alpha: "))
n=gen_ran(s,1000)
t=compare(n,r)
print t