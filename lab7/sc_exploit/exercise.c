#include <stdio.h>
#include <string.h>

static char mybuf[4096];

void copy(char *str)
{
	char buf1[128];

	int i = 0;

	strcpy(buf1, str);

}

void f1(char *str)
{
	char buf1[128];
	copy(str);
}

int main(int argc, char **argv)
{
	if (fread(mybuf, sizeof(mybuf), 1, stdin) < 0) {
                perror("error reading input");
		return 1;
        }
	f1(mybuf);
	return 0;
}
