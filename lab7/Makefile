CC=gcc
TARGETS=exercise-64 execve

all: $(TARGETS)

exercise-64: exercise.c
	$(CC) -o $@ -static -m64 -fno-stack-protector -g -z execstack -O0 -no-pie exercise.c
execve: execve.c
	$(CC) -o $@ execve.c
clean:
	rm -rf $(TARGETS) *.o
