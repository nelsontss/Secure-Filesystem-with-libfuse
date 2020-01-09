 
IDIR=../include
ODIR=obj
CC=gcc
CFLAGS = -Wall `pkg-config fuse3 --cflags --libs` -I$(IDIR) -lm

DEPS=$(IDIR)/$(wildcard *.h)
SOURCES=$(wildcard *.c)
SOURCES_OBJ=$(patsubst %.c,$(ODIR)/%.o,$(SOURCES))
print-% : ; @echo $* = $($*)

$(ODIR)/%.o : %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS) 

program: $(SOURCES_OBJ)
	$(CC) $(wildcard $(ODIR)/*.o) -o secureFS $(CFLAGS)

clean:
	rm obj/*.o
	rm secureFS