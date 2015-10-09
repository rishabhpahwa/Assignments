import string
import pdb
def sort_file(sherlock):
	'''This function reads the given text file and then converts the contents to lower case letters skipping any other characters found in the text. It also creates an array for the words occuring in the document and finally calls the sort function to sort the words alphabetically.'''
        a=open("sherlock.txt","r")
        lines=a.read()
	global i
	#print lines,"  ",len(lines)
	s=lines.lower()
	words=[]
        while i<len(s):
		if s[i]>='a' and s[i]<='z':
			words.append(next_word(s,i))
		i=i+1
	rst=heapsort(words)
	rst.reverse()
	print "The sorted words are:\n",rst
	x=raw_input("Enter the word you wish to search among the sorted words:\n")
	n_words=rst[:]
	match_found=binary_search(n_words,0,len(n_words)-1,x)
	print match_found
def next_word(s,q):
	'''Returns the current word as a character array to the calling routine.'''
	global i
	i=q
	stri=""
	while s[i]>='a' and s[i]<='z':
		#pdb.set_trace()
		stri+=s[i]		
		i+=1
	return stri
#def sort_str(words):
#	'''sorts the array of strings lexicographically.'''
#	for k in range(0,len(words)-1):
#		for l in range(0, len(words)-1-k):
#			if words[l]>words[l+1]:
#				words[l],words[l+1]=words[l+1],words[l]
def max_heapify(words,ris):
	l=2*ris+1
	r=2*ris+2
	if l<size and words[l]>words[ris]:
		lar=l
	else:
		lar=ris
	if r<size and words[r]>words[lar]:
		lar=r
	if lar!=ris:
		words[ris],words[lar]=words[lar],words[ris]
		max_heapify(words,lar)
def build_max_heap(words):
	size=len(words)
	for ris in range((len(words)/2),-1,-1):
		max_heapify(words,ris)
def heapsort(words):
	global size
	size=len(words)
	build_max_heap(words)
	result=array_sort_out(words)
	return result
def pop_max(words):
	global size
	if size<1:
		print "Heap error!"
	m=words[0]
	words[0]=words[size-1]
	size=size-1
	max_heapify(words,0)
	return m
def array_sort_out(words):
	b=[]
	for ris in range(0,len(words)):
		b.append(pop_max(words))
	return b
def binary_search(n_words,l,r,x):
	'''Performs binary search on the sorted strings.'''
	index=(l+r)/2
	#pdb.set_trace()
	if x>n_words[index] and index>0:
		binary_search(n_words,index,r,x)
	if x<n_words[index] and index>0:
		binary_search(n_words,l,index,x)
	if x==n_words[index]:
		print "Match found at index: ",index
		return index
	elif index<0:
		print "Word is not found."
i=0
sherlock=1
sort_file(sherlock)
