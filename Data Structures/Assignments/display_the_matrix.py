import random
count=[[ 0 for row in range(0,20)]for col in range(0,20)]
def partition(l,r,a):
	"""This function creates a partition taking the element at the index position r given in the function as partition(l,'r',{array}) as the pivot element, from the 'l' index to the r index, returning the correct position of the pivot in the sorted array."""
	mark=l
	for i in range(l,r):
		count[a[i]][a[r]]+=1
		count[a[r]][a[i]]+=1
		if a[i]<a[r]:
			a[i],a[mark]=a[mark],a[i]
			mark+=1
	a[r],a[mark]=a[mark],a[r]
	return mark
def quick_sort(left,right,a):
	"""The quick_sort algorithm begins. It accepts the beginning index and the index of last element in the array as quick_sort(left index,right index,{array}). It calls itself reccursively."""
	if left<right:
		alp=partition(left,right,a)
		quick_sort(left,alp-1,a)
		quick_sort(alp+1,right,a)
def gen_ran(size):
        a=[]
        for i in range(0,size):
            a.append(i)
        return a
def prin(array):
	for i in array:
		print i		
for i in range(0,1000):
	m=gen_ran(20)
	random.shuffle(m)
	quick_sort(0,len(m)-1,m)
prin(count)