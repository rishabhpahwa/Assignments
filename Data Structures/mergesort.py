n=map(int,raw_input("Enter the array(array elements separated by spaces).\n").split())
def merge(a,b):
	i=0
	j=0
	res=[]
	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			res.append(a[i])
			i+=1
		elif b[j]<=a[i]:
			res.append(b[j])
			j+=1
	res+=a[i:]
	res+=b[j:]
	return res
def merge_sort(a):
	if len(a)>1:
		x=merge_sort(a[:len(a)/2])
		y=merge_sort(a[len(a)/2:])
		bc=merge(x,y)
		return bc
	else:
		return a
print merge_sort(n)