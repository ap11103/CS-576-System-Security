CC=gcc
LDFLAGS=-no-pie
CFLAGS=-fstack-protector -O1 -U_FORTIFY_SOURCE -Wno-format-security -Wno-format
CFLAGS_FS=-fstack-protector -O1 -Wno-format-security
DEMO_TGTS=heap-stack-pivot
DEMO_TARGETS64_FS=$(addsuffix -64fs, $(DEMO_TGTS))
DEMO_TARGETS64=$(addsuffix -64, $(DEMO_TGTS))


all: $(DEMO_TARGETS64) 

$(DEMO_TARGETS64): %-64: %.c
	$(CC) -m64 $(LDFLAGS) $(CFLAGS) -g -o $@ $^

.PHONY: clean cleanall

clean:
	rm -f *.o

cleanall: clean
	rm -f $(DEMO_TARGETS64) $(DEMO_TARGETS64_FS)
