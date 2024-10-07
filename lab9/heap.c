#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

#define BUFSZ 512


struct heap_ptrs {
	long base;
	long *fun;
	long val;
};

char *echo_buf;
struct heap_ptrs *ptrs;
long last_num = 0;


void untouched(void)
{
	int r;
;
	printf("You shouldn't be here.\n");

	return;
}


void do_echo(const char *str)
{
	int i;

	for (i = 6; *str != '\n'; i++) {
		echo_buf[i] = *str++;
	}
	echo_buf[i] = '\0';

	puts(echo_buf);

	*ptrs->fun = ptrs->val;
}

int main(int argc, char **argv)
{
	char buf[BUFSZ];
	int r;

	echo_buf = malloc(142);
	if (!echo_buf)
		goto nomem;
	strcpy(echo_buf, "echo: ");

	ptrs = malloc(sizeof(*ptrs));
	if (!ptrs)
		goto nomem;

	ptrs->fun = &last_num;
	ptrs->val = rand();

	while (1) {
		r = read(STDIN_FILENO, buf, BUFSZ);
		if (r <= 0)
			break;
		do_echo(buf);
	}

	return EXIT_SUCCESS;

nomem:
	perror("malloc");
	return EXIT_FAILURE;
}
