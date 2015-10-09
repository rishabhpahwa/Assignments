a=[]#right=dir 1, left = dir 3, down= dir 2, rot 1=clock, rot 2= anti
begin_x=1
begin_y=1
def block(begin_x,begin_y,direction,rotation):
	if direction==1 and rotation==1:
		a.append((begin_x,begin_y))
		begin_y+=1
		a.append((begin_x,begin_y))
		begin_x+=1
		a.append((begin_x,begin_y))
		begin_y-=1
		a.append((begin_x,begin_y))
		#begin_x+=1
	if direction==2 and rotation==2:
		a.append((begin_x,begin_y))
		begin_x+=1
		a.append((begin_x,begin_y))
		begin_y+=1
		a.append((begin_x,begin_y))
		begin_x-=1
		a.append((begin_x,begin_y))
		#begin_y+=1
	if direction==3 and rotation==1:
		a.append((begin_x,begin_y))
		begin_y-=1
		a.append((begin_x,begin_y))
		begin_x-=1
		a.append((begin_x,begin_y))
		begin_y+=1
		a.append((begin_x,begin_y))
		begin_y+=1
def chunk():
	global begin_x
	global begin_y
	block(begin_x,begin_y,1,1)
	begin_x+=1
	block(begin_x,begin_y,2,2)
	begin_y+=1
	block(begin_x,begin_y,2,2)
	begin_x+=1
	block(begin_x,begin_y,3,1)
	#begin_y+=1
def SFC(n):
	if n==1:
		block(1,1,1,1)
	elif n>1:
		for j in range(1,(4**(n-2))+1):
			chunk()
m=input("Enter the order of printing")
SFC(m)
print a