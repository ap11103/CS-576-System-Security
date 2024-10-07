#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <ctype.h>

#define BUFSZ 512


struct heap_ptrs {
	void (*f)(const char *);
	int id;
};

char *echo_buf;
struct heap_ptrs *ptrs;
int ptrnum = 2;

int spare_func2(int n)
{
	int i, nc = 0;

	for (i = 0; i < n; i++) {
		nc += printf("%d You Win!\n", i);
	}
	return nc;
}

void echo1(const char *s)
{
	printf("echo1 %s\n", s);
}

void echo2(const char *s)
{
	printf("echo2 ");
	while (*s != '\0') {
		putchar(toupper(*s));
		s++;
	}
	putchar('\n');
}

void do_echo(const char *str)
{
	int id, i;

	for (i = 0; *str != ' '; i++) {
		echo_buf[i] = *str++;
	}
	echo_buf[i] = '\0';
	id = atoi(echo_buf);

	for (str++, i = 0; *str != '\n'; i++) {
		echo_buf[i] = *str++;
	}
	echo_buf[i] = '\0';

	for (i = 0; i < ptrnum; i++) {
		if (ptrs[i].id == id) {
			ptrs[i].f(echo_buf);
			break;
		}
	}
}

int main(int argc, char **argv)
{	
	char buf[BUFSZ];
	int r;

	echo_buf = malloc(64);
	if (!echo_buf)
		goto nomem;

	ptrs = malloc(2 * sizeof(struct heap_ptrs));
	if (!ptrs)
		goto nomem;


	ptrs[0].id = 1;
	ptrs[0].f = echo1;
	ptrs[1].id = 2;
	ptrs[1].f = echo2;

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
