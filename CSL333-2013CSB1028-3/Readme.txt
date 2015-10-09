#########################################
#	CSL333: Assignment 3		#
#	Name: Rishabh Pahwa		#
#	Entry No: 2013CSB1028		#
#########################################

The project consists of the following files:

1. starvation.c
	
	This is the main functional unit of the project. It sorts the task according to:
		1. Favor the highest priority tasks. 				
		2. Minimize the response time.					
		3. Favor the task asking for maximum amount of resources.	
	
	It asks for the input on the number of resources to be allocated and the maximum number of tasks 
	to be allocated.
	Some assumptions made:
		a. The cost and capacity of resources is decided randomly while the resource is created.
		b. The size of the task is decided randomly and resource allocation to a task too is done
		   by choosing random number of instances of a particular resource.
	
	The program then implements a queue to manage the tasks assigned by the system. 
	It first assigns the task with higher initial priority as the task towards the front of the queue.
	If the priorities of two tasks is same, it assigns the task with less number of resources requested
	as the one in the front of the queue (ie. the one which will be executed first).
	If the resources requested too are same, it builds the queue according to first-come-first-serve basis.
	

2. Design_Document.txt
	
	This explains the intrinsic details of the working of the program, assumptions made, what the output
	represents and what all choices I made while designing the project.
	It also discusses the comparison of the above implemeted algorithm with Round-Robin, shortest remaining
	time first and FCFS methods of scheduling tasks.
	
3. Readme.txt

	This is the current file.
	
Additionally the project may contain compiled versions of the starvation.c code along with the above mentioned files.


How to Run? (Sample Input and outputs)

	1. navigate to the working directory using the cd commands in the terminal.
	2. $ gcc starvation.c -o starvation
	3. $ ./starvation

Suitable Test scenarios:

Sample Input:

$ Enter the number of resource types: 19
$ Enter the maximum number of tasks to allocate: 14

Sample output:

Order of execution of tasks:

Priority: 17	Cost: 151	Task ID: 9
Priority: 17	Cost: 156	Task ID: 2
Priority: 13	Cost: 121	Task ID: 3
Priority: 13	Cost: 122	Task ID: 8
Priority: 13	Cost: 122	Task ID: 10
Priority: 13	Cost: 127	Task ID: 13
Priority: 13	Cost: 146	Task ID: 11
Priority: 12	Cost:  72	Task ID: 14
Priority: 12	Cost:  85	Task ID: 6
Priority: 12	Cost: 118	Task ID: 7
Priority: 7	Cost:  20	Task ID: 12
Priority: 7	Cost:  29	Task ID: 5
Priority: 7	Cost:  43	Task ID: 1
Priority: 6	Cost:  26	Task ID: 4

	PS: A floating point exception may arise due to random values being generated and used (Its caused due to division by 0).
	    I've tried my best to resolve the same, but still randomness might generate it. Please re-run the code (with 
	    the same input values too, if you please) and it'll execute just fine.

-Rishabh Pahwa.
Entry no: 2013CSB1028
Institute: IIT-Ropar.
