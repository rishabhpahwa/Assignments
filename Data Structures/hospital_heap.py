import random
def max_heapify(a,i):
	l=2*i+1
	r=2*i+2
	if l<size and a[l]>a[i]:
		lar=l
	else:
		lar=i
	if r<size and a[r]>a[lar]:
		lar=r
	if lar!=i:
		a[i],a[lar]=a[lar],a[i]
		max_heapify(a,lar)
def build_max_heap(a):
	size=len(a)
	for i in range((len(a)/2),-1,-1):
		max_heapify(a,i)
def heapsort(a):
	build_max_heap(a)
	pop_max(a)
def pop_max(a):
	global size
	if size<1:
		print "Hospital is completely empty!"
	m=a[0]
	print "patient with criticality ",m," is now treated and hence leaves. :)"
	a.pop(0)
	size=len(a)
	inc_criticality(a,size)
	build_max_heap(a)
	new_in=in_patient(a)
	size=len(a)
	if size >hos_lim:
		print "Max patient limit reached. The hospital now breaks down."
	elif size<=hos_lim:
		for q in range(size-1,size-new_in-1,-1):
			up_heapify(a,q)
		print "Current patients:\n",a,"\n"
		pop_max(a)
def in_patient(a):
	i=random.randrange(0,5)
	print i," patient(s) are entering the hospital for treatment. :)"
	for j in range(0,i):
		a.append(random.randrange(1,101))
	return i
def up_heapify(a,i):
	p=i/2
	if p>=0 and a[i]>a[p]:
		a[i],a[p]=a[p],a[i]
		up_heapify(a,p)
def inc_criticality(a,size):
	ran1=random.randrange(0,size)
	for i in range(0,ran1):
		ran2=random.randrange(0,size)
		a[ran2]=random.randrange(ran2,101)
a=[]
hos_lim=input("Please enter the hospital limit: ")
for h in range(0,5):
	a.append(random.randrange(1,101))
print "The initial patients are:\n",a
size=len(a)
heapsort(a)