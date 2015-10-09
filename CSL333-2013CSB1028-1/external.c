/*
#########################################
#	CSL-333: Lab Assignment 1	#
#	Name: Rishabh Pahwa.		#
#	Entry No: 2013CSB1028		#
#########################################	
*/

#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <mqueue.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>
#include <stdlib.h>

#define MSG_S 512

typedef struct 					// Struct defined for storing the temperature and pid's of processes,
{						// be it central or external. Multiple instances of the same would be
	long priority;				// created and used for the purpose.
	int temp;
	int pid;
	int stable;
} msgp;

int main(int argc, char *argv[])		// Main execution begings.
{
	int inp=atoi(argv[1]);			// 1st Input argument (Initial Temperature) converted to Integer.
	int inp2=atoi(argv[2]);			// Unique ID for the external process is supplied as 2nd input.
	msgp central_t, external_t1;
	central_t.priority=2, external_t1.priority=2;	// Priority of the processes is set to 2.
	int msqid, msqid1;
	key_t key, key1;
	key=70;
	key1=70+inp2;				// The key supplied to msgget is modified according to the input parameter to indentify
	external_t1.temp=inp;			// external processes' individual queues.
	if ((msqid1=msgget(key1, 0666 | IPC_CREAT))<0)	// First queue created to receieve central temperature.
	{
		perror("msgget");
		exit(1);
	}
	if ((msqid=msgget(key, 0666 | IPC_CREAT))<0)	// Second queue created to send external temperature to central process.
	{
		perror("msgget");
		exit(1);
	}
	if (msgsnd(msqid, &external_t1, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send initial temperature to central process.
	{
		perror("msgsnd (70)\n");
		exit(1);
	}
	
	while(1)		// Looping contruct. Would end conditionally within the loop.
	{
		if (msgrcv(msqid1, &central_t, (sizeof(msgp)-sizeof(long)), 2, 0)<0)	// Receieves temperature from central process.
		{
			perror("msgrcv\n");
			exit(1);
			
		}
		if (central_t.temp==-1)		// Checks for the termination temperature sent by the central process.
		{
			printf("Stability attained for External process number: %d. Temperature: %d\n",inp2, external_t1.temp);
			break;
		}
		else
		{
			external_t1.temp=(3*external_t1.temp + 2*central_t.temp)/5;	// Calculates new external temperature.
			if (msgsnd(msqid, &external_t1, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Sends new external temp to centre
			{
				perror("msgsnd (71)\n");
				exit(1);
			}
		}
	}
	return 0;		// Ends here.
}
