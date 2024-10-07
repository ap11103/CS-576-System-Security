CC=gcc
LDFLAGS=-no-pie
CFLAGS=-fno-stack-protector -O0 -g
DEMO_TGTS=vuln
DEMO_TARGETS64=$(addsuffix -64, $(DEMO_TGTS))

all: $(DEMO_TARGETS64)

$(DEMO_TARGETS64): %-64: %.c
	$(CC) -m64 $(LDFLAGS) $(CFLAGS) -o $@ $^

.PHONY: clean cleanall

clean:
	rm -f *.o $(DEMO_TARGETS32) $(DEMO_TARGETS64)
