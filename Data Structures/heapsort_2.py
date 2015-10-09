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
	array_sort_out(a)
def pop_max(a):
	global size
	if size<1:
		print "WTF! heap is fucked up!"
	m=a[0]
	a[0]=a[size-1]
	size=size-1
	max_heapify(a,0)
	return m
def array_sort_out(a):
	b=[]
	for i in range(0,len(a)):
		b.append(pop_max(a))
	print b
a=input("Enter the array to be sorted:\n")
size=len(a)
heapsort(a)