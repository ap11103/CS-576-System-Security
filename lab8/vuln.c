#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>


int vuln() {
   char buf[80];
   int r;
   r = read(0, buf, 400);
   printf("\nRead %d bytes. buf is %s\n", r, buf);
   return 0;
}

int main(int argc, char *argv[]) {
   vuln();
   return 0;
}
