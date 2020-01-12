 
IDIR=../include
ODIR=obj
CC=gcc
CFLAGS = -Wall `pkg-config fuse3 --cflags --libs` -I$(IDIR) -lm
LDIR=lib
OLDIR=$(ODIR)/lib

DEPS=$(IDIR)/$(wildcard *.h)
SOURCES=$(wildcard *.c)
MY_LIBS=$(wildcard $(LDIR)/*.c)
SOURCES_OBJ=$(patsubst %.c,$(ODIR)/%.o,$(SOURCES))
MY_LIBS_OBJ=$(foreach o, $(patsubst %.c,%.o,$(MY_LIBS)), $(ODIR)/$o)
LIBS = `pkg-config --libs glib-2.0`

print-% : ; @echo $* = $($*)

$(ODIR)/%.o : %.c $(DEPS)
	$(CC) `pkg-config --cflags glib-2.0` -c -o $@ $< $(CFLAGS) 

program: $(SOURCES_OBJ)
	$(CC) `pkg-config --cflags glib-2.0` $(wildcard $(ODIR)/*.o) -o secureFS $(CFLAGS)  $(LIBS)

clean:
	rm obj/*.o
	rm secureFS