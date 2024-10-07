#include <sys/syscall.h>
#include <unistd.h>

int main()
{
	char *argv[] = { "/bin/cat", "/etc/passwd", NULL };

	syscall(SYS_execve, argv[0], argv, NULL);
	return 0;
}
