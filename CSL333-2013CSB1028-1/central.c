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

typedef struct 				// Struct defined for storing the temperature and pid's of processes,
{					// be it central or external. Multiple instances of the same would be
	long priority;			// created and used for the purpose.
	int temp;
	int pid;
	int stable;
} msgp;

int main(int argc, char *argv[])	// Main execution begins.
{
	int inp=atoi(argv[1]);		// converts the 1st command line argument (initial temperature) to integer. 
	msgp central_t, external_t1, external_t2, external_t3, external_t4;	// Multiple instances of struct to store data,
	central_t.priority=2, external_t1.priority=2, external_t2.priority=2, external_t3.priority=2, external_t4.priority=2;
	int msqid, msqid1, msqid2, msqid3, msqid4;	// To store Queue ID's of message queues created.
	key_t key, key1, key2, key3, key4;		// Key values for the message queues to be created.
	key=70;
	key1=71;
	key2=72;
	key3=73;
	key4=74;
	central_t.temp=inp;				// Central temperature initialized to input temperature.
	if ((msqid1=msgget(key1, 0666 | IPC_CREAT))<0)	// To create 1st external queue. Central process sends messages to 1st 
	{						// external process via this queue.
		perror("msgget");
		exit(1);				// Exit if error in queue creation.
	}
	if ((msqid2=msgget(key2, 0666 | IPC_CREAT))<0)	// To create 2nd external queue. Central process sends messages to 2nd
	{						// external process via this queue.
		perror("msgget");
		exit(1);				
	}
	if ((msqid3=msgget(key3, 0666 | IPC_CREAT))<0)	// To create 3rd external queue. Central process sends messages to 3rd
	{						// external process via this queue.
		perror("msgget");
		exit(1);
	}
	if ((msqid4=msgget(key4, 0666 | IPC_CREAT))<0)	// To create 4th external queue. Central process sends messages to 4th
	{						// external process via this queue.
		perror("msgget");
		exit(1);
	}
	if ((msqid=msgget(key, 0666 | IPC_CREAT))<0)	// To create queue for central process. External processes send info
	{						// to central process via this queue.
		perror("msgget");
		exit(1);
	}
	int flag=0;			// Variables for logical
	int sum=0;			// reasons.
	int prev[4]={0};
	do 					// Do-While loop begins.
	{
		sum=0;
		if (msgrcv(msqid, &external_t1, (sizeof(msgp)-sizeof(long)), 2, 0)<0)	// Receieve 1st External Temperature.
		{
			perror("msgrcv\n");
			exit(1);
		}
		sum+=external_t1.temp;
		
		if (msgrcv(msqid, &external_t2, (sizeof(msgp)-sizeof(long)), 2, 0)<0)	// Receieve 2nd External Temperature.
		{
			perror("msgrcv\n");
			exit(1);
		}
		sum+=external_t2.temp;
		if (msgrcv(msqid, &external_t3, (sizeof(msgp)-sizeof(long)), 2, 0)<0)	// Receieve 3rd External Temperature.
		{
			perror("msgrcv\n");
			exit(1);
		}
		sum+=external_t3.temp;
		if (msgrcv(msqid, &external_t4, (sizeof(msgp)-sizeof(long)), 2, 0)<0)	// Receieve 4th External Temperature.
		{
			perror("msgrcv\n");
			exit(1);
		}
		sum+=external_t4.temp;
		
		if(prev[0]==external_t1.temp && prev[1]==external_t2.temp && prev[2]==external_t3.temp && prev[3]==external_t4.temp)						// Check stability.
		{
			printf("\nStability attained at center. Now terminating.\nTempratures:\nCentral: %d\nExternal_1: %d\nExternal_2: %d\nExternal_3: %d\nExternal_4: %d\n",central_t.temp, external_t1.temp, external_t2.temp, external_t3.temp, external_t4.temp);
			external_t1.temp=-1;
			external_t2.temp=-1;
			external_t3.temp=-1;
			external_t4.temp=-1;
			if (msgsnd(msqid1, &external_t1, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 1st external process.
				perror("msgsnd (71)\n");
				exit(1);
			}
			if (msgsnd(msqid2, &external_t2, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 1st external process.
				perror("msgsnd (71)\n");
				exit(1);
			}
			if (msgsnd(msqid3, &external_t3, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 1st external process.
				perror("msgsnd (71)\n");
				exit(1);
			}
			if (msgsnd(msqid4, &external_t4, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 1st external process.
				perror("msgsnd (71)\n");
				exit(1);
			}
			flag=1;
			break;
		}
		else
		{
			prev[0]=external_t1.temp;
			prev[1]=external_t2.temp;
			prev[2]=external_t3.temp;
			prev[3]=external_t4.temp;
			central_t.temp = ((2*central_t.temp + sum)/6);		// New Central temperature calculated.
			if (msgsnd(msqid1, &central_t, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 1st external process.
				perror("msgsnd (71)\n");
				exit(1);
			}
			if (msgsnd(msqid2, &central_t, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 2nd external process.
				perror("msgsnd (72)\n");
				exit(1);
			}
			if (msgsnd(msqid3, &central_t, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 3rd external process.
				perror("msgsnd (73)\n");
				exit(1);
			}
			if (msgsnd(msqid4, &central_t, (sizeof(msgp)-sizeof(long)), IPC_NOWAIT)<0)	// Send new Central temperature
			{										// to 4th external process.
				perror("msgsnd (74)\n");
				exit(1);
			}
		}
	} while(1);		// Do-While loop condition test to check stability.
	if (flag==1)		// To delete the message queues.
	{					
		char r1[100]="ipcrm -q ";
		char buf1[100];
		sprintf(buf1, "%d", msqid);
		strcat(r1,buf1);				// PS: The msgctl command was seemingly not working for me so
		system(r1);					// I used the system command of ipcrm itself.
		char r2[100]="ipcrm -q ";
		char buf2[100];
		sprintf(buf2, "%d", msqid1);
		strcat(r2,buf2);
		system(r2);
		char r3[100]="ipcrm -q ";
		char buf3[100];
		sprintf(buf3, "%d", msqid2);
		strcat(r3,buf3);
		system(r3);
		char r4[100]="ipcrm -q ";
		char buf4[100];
		sprintf(buf4, "%d", msqid3);
		strcat(r4,buf4);
		system(r4);
		char r5[100]="ipcrm -q ";
		char buf5[100];
		sprintf(buf5, "%d", msqid4);
		strcat(r5,buf5);
		system(r5);
	}
	return 0;	// Ends here.
}
