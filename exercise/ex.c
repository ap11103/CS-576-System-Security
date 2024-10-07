#include <stdio.h>
#include <string.h>

void f1(const char *str)
{
	char buf[16];

	strcpy(buf, str);

	puts(buf);
}

int main(int argc, char **argv)
{
	if (argc < 2)
		return 1;
	f1(argv[1]);
	return 0;
}
