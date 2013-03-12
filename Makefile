CFLAGS += $(RPM_OPT_FLAGS) -Wall -D_GNU_SOURCE

PROGS = usleep
mandir = /usr/share/man

all: $(PROGS)

clean:
	rm -f $(PROGS) *.o

install:
	mkdir -p $(DESTDIR)/bin
	install -m 755 usleep $(DESTDIR)/bin/usleep
	mkdir -p $(DESTDIR)/$(mandir)/man1
	install -m 644 usleep.1 $(DESTDIR)/$(mandir)/man1/

USLEEP_OBJS = usleep.o
usleep: $(USLEEP_OBJS)
	$(CC) $(LDFLAGS) -o $@ $(USLEEP_OBJS) -lpopt

