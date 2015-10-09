import rubik

class node:
	'''A basic class for a node. Contains all node functions which might be required.'''
	def __init__(self,data):
		self.data=data
		self.c1=None
		self.c2=None
		self.c3=None
		self.c4=None
		self.c5=None
		self.c6=None
		self.parent=None
		self.ht=0
def shortest_path(start, end):
	"""
	Using 2-way BFS, finds the shortest path from start_position to
	end_position. Returns a list of moves. 
	Assumes the rubik.quarter_twists move set.
	"""
	root1=node(start)
	root2=node(end)
	arr1=[[] for wqw in range(8)]
	arr2=[[] for qwq in range(8)]
	ser1=[[] for lp in range(100000)]
	ser2=[[] for lp in range(100000)]
	arr1[0].append(root1)
	arr2[0].append(root2)
	ser1[(hash(start))%100000].append(start)
	ser2[(hash(end))%100000].append(end)
	flag=0
	chk=None
	for h in range(0,7):
		chk=check_match(arr1[h],arr2[h])
		if not chk is None:
			flag=1
			break
		else:
			for w in range(len(arr1[h])):
				fin=insert_e(arr1[h][w].data,h+1,arr1,ser1)
				arr1=fin[0]
				ser1=fin[1]
		chk=check_match(arr2[h],arr1[h+1])
		if not chk is None:
			flag=2
			break
		else:
			for q in range(len(arr2[h])):
				fim=insert_e(arr2[h][w].data,h+1,arr2,ser2)
				arr2=fim[0]
				ser2=fim[1]
	if flag==1:
		while not chk[0].parent is None:
			res1.append(chk[0].parent.data)
			chk[0]=chk[0].parent
		res+=res1.reverse()
		res.append(chk[1])
		while not chk[1].parent is None:
			res2.append(chk[1].parent.data)
			chk[1]=chk[1].parent
		return res
	elif flag==2:
		while not chk[1].parent is None:
			res1.append(chk[1].parent.data)
			chk[1]=chk[1].parent
		if not res1 is None:
			res+=res1.reverse()
		res.append(chk[0])
		while not chk[0].parent is None:
			res2.append(chk[0].parent.data)
			chk[0]=chk[0].parent
		return res
	else:
		print "The given configuration is not solvable/wrong."
def check_match(x,y):
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i].data == y[j].data:
				return [x[i],y[j]]
	return None
def insert_e(x,h,arr,ser):
	if h<8:
		flag=0
		z=rubik.perm_apply(rubik.F,x)
		x.c1=node(z)
		y=(hash(z))%100000
		for i in range(0,len(ser[y])):
			if z is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z)
			arr[h].append(x.c1)
			x.c1.parent=x
			x.c1.ht=h
		z2=rubik.perm_apply(rubik.Fi,x)
		x.c2=node(z2)
		flag=0
		y=(hash(z2))%100000
		for i in range(0,len(ser[y])):
			if z2 is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z2)
			arr[h].append(x.c2)
			x.c2.parent=x
			x.c2.ht=h
		z3=rubik.perm_apply(rubik.L,x)
		x.c3=node(z3)
		flag=0
		y=(hash(z3))%100000
		for i in range(0,len(ser[y])):
			if z3 is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z3)
			arr[h].append(x.c3)
			x.c3.parent=x
			x.c3.ht=h
		z4=rubik.perm_apply(rubik.Li,x)
		x.c4=node(z4)
		flag=0
		y=(hash(z4))%100000
		for i in range(0,len(ser[y])):
			if z4 is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z4)
			arr[h].append(x.c4)
			x.c4.parent=x
			x.c4.ht=h
		z5=rubik.perm_apply(rubik.U,x)
		x.c5=node(z5)
		flag=0
		y=(hash(z5))%100000
		for i in range(0,len(ser[y])):
			if z5 is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z5)
			arr[h].append(x.c5)
			x.c5.parent=x
			x.c5.ht=h
		z6=rubik.perm_apply(rubik.Ui,x)
		x.c6=node(z6)
		flag=0
		y=(hash(z6))%100000
		for i in range(0,len(ser[y])):
			if z6 is ser[y][i]:
				flag=1
				break
			else:
				flag=0
		if flag==0:
			ser[y].append(z6)
			arr[h].append(x.c6)
			x.c6.parent=x
			x.c6.ht=h
	return [arr,ser]