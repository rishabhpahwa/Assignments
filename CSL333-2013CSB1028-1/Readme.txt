/*
#########################################
#	CSL-333: Lab Assignment 1	#
#	Name: Rishabh Pahwa.		#
#	Entry No: 2013CSB1028		#
#########################################	
*/

============================================================================================

The Project consists of the following files as it's parts:

1. central.c
	
	This is the program for the central process and accepts an initial temperature value
	as a command line argument which is assigned to the central process. Additionally it
	creates message(POSIX) queues for itself and each of the external processes to which
	it communicates. It receives messages on queue created using the key number = 70 and
	sends its updated temperature value to each of the external process on queue numbers
	71,72,73 and 74 in succession. It also deletes the created queues after each of the
	processes attain stability.

2. external.c
	
	This is the program for the external processes and accept two command line arguments
	in the form of it's initial temperature and a unique ID which is specific to each of
	the external process and is also used to create message (POSIX) queue for themselves.
	Additionally it also creates a message (POSIX) queue for the central process if the
	same doesn't already exist. It communicates to the central process by receiving it's
	updated temperature value on either of the queue (71, 72, 73, 74) depending upon the
	queue it has created/has corresponding to it's unique ID. It also sends it's updated
	temperature to the central process on queue number = 70. It exits when the central
	process signals it to by sending a temperature value = -1.

3. Unit_Testing.sh
	
	This is a simple bash script file to test the project with some sample temperature values
	for each of the central and the 4 external processes.
	The sample values are: 
		a. 100 for the 1st external process.
		b. 22 for the 2nd external process.
		c. 50 for the 3rd external process.
		d. 40 for the 4th external process.
		e. 60 for the central process.

4. Readme.txt
	
	This is the file you are currently viewing.
	
5. 'external' and 'central'
	
	These are the compiled c programs which might be present if you decide to view the folder
	after executing the project atleast once.

===================================================================================================

To Run:
	1. Navigate to the project directory on your system using the cd command in the terminal.
	2. Type the following command in the terminal: bash Unit_Testing.sh
	3. The output would then display the stable temperatures of the central and each of the four
	   external processes.
	4. Press 'Enter' again to exit the bash.
	
	
Author: ®Rishabh Pahwa
	
