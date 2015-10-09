def insertion_sort_asc():
	n=list(input("Enter the array to be sorted\n\n"))
	for i in range(1,len(n),1):
		j=i
		temp=n[i]
		while j>0 and n[j-1]>temp:
			n[j]=n[j-1]
			j=j-1
		n[j]=temp
	print "The sorted array is:\n\n",n
def insertion_sort_desc():
	n=list(input("Enter the array to be sorted\n\n"))
	for i in range(1,len(n),1):
		j=i
		temp=n[i]
		while j>0 and n[j-1]<temp:
			n[j]=n[j-1]
			j=j-1
		n[j]=temp
	print "The sorted array is:\n\n",n
c=int(raw_input("1. Ascending Order.\n2. Descending Order.\n\nChoice: "))
if c==1:
	insertion_sort_asc()
elif c==2:
	insertion_sort_desc()
else:
	print "invalid input"