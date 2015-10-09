def gen_mat(size):
	'''Generates a random matrix of size=size(User Defined).'''
	a=[[0 for x in range(size)] for y in range(size)]
	q=1
	for i in range(0,size):
		for j in range(0,size):
			a[i][j]=q
			q+=1
	return a
def spiral(a):
	'''Prints the array elements spirally where the array elements are stored in ascending order horizontally as we write in a book(i.e. left to right and the down)'''
	i=int(len(a)/2)
	j=int(len(a)/2)
	m=int(len(a)/2)
	for b in range(0,len(a)-1):
		c=b
		if i==j and i>=m:
			while c>=0:
				print a[i][j]
				c-=1
				j-=1
		elif i==j and i<m:
			while c>=0:
				print a[i][j]
				c-=1
				j+=1
		c=b
		if i>j and abs(i-j)%2==1:
			while c>=0:
				print a[i][j]
				c-=1
				i-=1
		elif i<j and abs(i-j)%2==0:
			while c>=0:
				print a[i][j]
				c-=1
				i+=1
	for q in range(j,-1,-1):
		print a[i][q]
n=input("Enter the size of square matrix: ")
a=gen_mat(n)
spiral(a)
