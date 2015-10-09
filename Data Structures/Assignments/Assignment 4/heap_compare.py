import random
import time
def max_heapify(a,i,k):
	'''Heapifies a node(i)'''
	global count
	l=k*i+1
	r=(i+1)*k
	lar=i
	for j in range(l,r+1):
		count+=1
		if j<size and a[j]>a[lar]:
			lar=j
	if lar!=i:
		a[i],a[lar]=a[lar],a[i]
		max_heapify(a,lar,k)
def build_max_heap(a,k):
	'''Builds a max heap for the array a'''
	size=len(a)
	for i in range((len(a)/k),-1,-1):
		max_heapify(a,i,k)
def heapsort(a,k):
	build_max_heap(a,k)
	array_sort_out(a,k)
def pop_max(a,k):
	global size
	if size<1:
		print "Heap error!"
	m=a[0]
	a[0]=a[size-1]
	size=size-1
	max_heapify(a,0,k)
	return m
def array_sort_out(a,k):
	b=[]
	for i in range(0,len(a)):
		b.append(pop_max(a,k))
def compare(a):
	global count
	x=a[:]
	p=time.time()
	heapsort(a,2)
	print "No of iterations for binary heap: ",count
	q=time.time()
	print "Time taken for binary heap: ",(q-p)
	global size
	size=len(x)
	count=0
	heapsort(x,3)
	r=time.time()
	print "No of iterations for ternary heap: ",count
	print "Time taken for ternary heap: ",(r-q)
n=input("Enter the length of random array desired: ")
a=[]
for o in range(0,n):
	a.append(random.randrange(0,1500))
#print "The random array to be sorted is:\n",a
size=len(a)
count=0
compare(a)