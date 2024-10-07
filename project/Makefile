AS = gcc -c
ASFLAGS = -g    
CC=gcc
CFLAGS=-fstack-protector-all -z noexecstack -O0 -g
LDFLAGS_PIE=-pie -Wl,-z,relro,-z,now
TGTS=vuln
TARGETS64=$(addsuffix -64, $(TGTS))

%.o: %.s
	$(AS) $(ASFLAGS) -o $@ $<

all: $(TARGETS64)

$(TARGETS64): %-64: %.c aux.o
	$(CC) -m64 $(LDFLAGS_PIE) $(CFLAGS) -o $@ $^

.PHONY: clean cleanall

clean:
	rm -f $(TARGETS64) aux.o
