#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void);

/**
 * main - creates 5 zombie processes
 * Return: Always 0
 */
int main(void)
{
	pid_t zpid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zpid = fork();
		if (zpid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - pauses the program indefinitly
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
