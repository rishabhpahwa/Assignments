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