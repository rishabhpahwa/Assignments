/*
#########################################
#	CSL333: Assignment 3		#
#	Name: Rishabh Pahwa		#
#	Entry No: 2013CSB1028		#
#########################################
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>

typedef struct res				// Details for the resources stored here. Multiple instances of the same
{						// are created in the program.
	int id;
	int cost;
	int cap_ips;
} resource;

typedef struct task				// Details for the task stored here. Multiple instances of the same are 
{						// created in the program.
	struct task *front;
	struct task *back;
	int p;
	int s;
	int task_id;
	int resources[];
} task;

void q_insert(task *t, task *head)		// function to insert and arrange tasks in the queue.
{
	task *current;
	current=head;
	int flag=0;
	for ( ; (current->back) != NULL ; )		// Checks for the end of the queue.
	{
		current = current->back;
		if ((current->p) < (t->p))		// Initial priority of the processes compared and tasks are arranged.
		{
			(current->front)->back=t;
			task *temp;
			temp=current->front;
			current->front = t;
			t->back = current;
			t->front = temp;
			flag=1;
			break;
		}
		else if((current->p) == (t->p))		// If the priorities are same.
		{
			if ((current->s) > (t->s))	// Check for the amount of resources requested. Put the task with lesser
			{				// resource request in front of the queue.
				(current->front)->back=t;
				task *temp;
				temp=current->front;
				current->front = t;
				t->back = current;
				t->front = temp;
				flag=1;
				break;
			}
			else if((current->task_id) > (t->task_id))	// If above are equal, sort according to FCFS.
			{
				(current->front)->back=t;
				task *temp;
				temp=current->front;
				current->front = t;
				t->back = current;
				t->front = temp;
				flag=1;
				break;
			}
		}
	}
	if (flag ==0)			// Inserting element at the end of the queue, if we reach the end and
	{				// the task is not yet allocated.
		current->back=t;
		t->front = current;
		t->back = NULL;
	}
}


int main(int argc, char *argv[])	// Main execution begins.
{
	int r_no, t_no;
	printf("Enter the number of resource types: ");
	scanf("%d", &r_no);			// No. of resource types input.
	printf("Enter the maximum number of tasks to allocate: ");
	scanf("%d", &t_no);			// Max no of tasks input.
	resource res[r_no];
	int i,total_cap=0;
	int x;
	for (i=0 ; i<r_no ;)			// Creating resources.
	{
		srand(time(NULL)+i);
		if (x=rand()%r_no != 0)
			res[i].cap_ips=x+10;
		else
			continue;
		srand(time(NULL)+i+1);
		res[i].cost=(rand()%(r_no-1))+2;
		res[i].id=i;
		total_cap+=(res[i].cost);
		i++;
	}
	int n_tasks;
	task head;				// Defining the head in the queue.
	head.front = NULL;			// It remains unchanged as an unchanged entry point to the queue was needed.
	head.back = NULL;
	head.p=INT_MAX;
	head.s=INT_MAX;
	head.task_id=0;
	task tasks[t_no];
	
	int sum,choice,j,count;
	for (n_tasks=1;n_tasks<=t_no;)		// Creating new tasks.
	{
		srand(time(NULL)+n_tasks);
		tasks[n_tasks].s=rand()%(total_cap);
		int limit=tasks[n_tasks].s;
		tasks[n_tasks].p=0;
		tasks[n_tasks].task_id=n_tasks;
		for (j=0,sum=0,count=0; limit > 0;j++)		// Allocating resources to the tasks.
		{
			srand(time(NULL)+j);
			choice=rand()%r_no;
			if (choice > 0)
			{
				int instances=rand()%(4);
				sum+=(res[choice].cost)*instances;
				tasks[n_tasks].resources[count]=choice;
				count++;
				limit-=(res[choice].cost)*instances;
			}
		}
		tasks[n_tasks].p=(int)sum/(count+1);
		q_insert(&tasks[n_tasks], &head);		// Call to the queuing function for arranging the new task.
		n_tasks++;
	}
	printf("Order of execution of tasks:\n\n");
	task *current;
	current=&head;
	for (;(current->back)!=NULL;)				// Executes the task by printing the order in which they are executed.
	{
		current = current->back;
		printf("Priority: %d\tCost: %3d\tTask ID: %d\n",current->p,current->s,current->task_id);
	}
	return 0;
}
