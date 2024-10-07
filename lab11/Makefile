CC=gcc
CXX=g++
CFLAGS=-O1 -Wno-format-security -Wno-format -fstack-protector 
CXXFLAGS=-O0
DEMO_TGTS_MARCH=fmt_victim
DEMO_TGTS_32=$(addsuffix -32, $(DEMO_TGTS_MARCH))
DEMO_TGTS_64=$(addsuffix -64, $(DEMO_TGTS_MARCH))
DEMO_PIE=fmt_examples-pie
DEMO_FS=fmt_examples-fs
DEMO_CPP=virtual

all: $(DEMO_TGTS_32)

$(DEMO_TGTS_32): %-32: %.c
	$(CC) -m32 -g -no-pie $(CFLAGS) -U_FORTIFY_SOURCE -o $@ $^

.PHONY: clean cleanall

clean:
	rm -f *.o $(DEMO_TGTS) $(DEMO_PIE) $(DEMO_FS) $(DEMO_CPP)


cleanall: clean
	rm -f $(DEMO_TGTS_64) $(DEMO_TGTS_32)
