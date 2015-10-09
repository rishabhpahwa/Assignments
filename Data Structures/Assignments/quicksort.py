def partition(l,r,a):
	"""This function creates a partition taking the element at the index position r given in the function as partition(l,'r',{array}) as the pivot element, from the 'l' index to the r index, returning the correct position of the pivot in the sorted array."""
	mark=l
	for i in range(l,r):
		if a[i]<a[r]:
			a[i],a[mark]=a[mark],a[i]
			mark+=1
	a[r],a[mark]=a[mark],a[r]
	print a,"::",mark
	return mark
def quick_sort(left,right,a):
	"""The quick_sort algorithm begins. It accepts the beginning index and the index of last element in the array as quick_sort(left index,right index,{array}). It calls itself reccursively."""
	if left<right:
		alp=partition(left,right,a)
		quick_sort(left,alp-1,a)
		quick_sort(alp+1,right,a)
n=input("Enter the array:\n\n")
quick_sort(0,len(n)-1,n)
print "The sorted array is\n",n