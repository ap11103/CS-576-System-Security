#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>

#define BUFF_SZ  128

extern int READ_SZ, usefulGadget(); // from useful.s

struct data {
    char buffer[BUFF_SZ];
};

struct fp {
    void (*fp)();
};

void win() {
    printf("\nYou win!\n");
}

void lose() {
    printf("\nYou lose...\n");
}

void vuln_func(){

    struct data *d;
    struct fp *f;

    d = malloc(sizeof(struct data));
    f = malloc(sizeof(struct fp));
    f->fp = lose;

    read(STDIN_FILENO, d->buffer, READ_SZ);  // 400

    printf(d->buffer);

    f->fp();
}

int main(int argc, char *argv[]){
    
    while(1){
    	vuln_func();
    }    
    return 0;
}
