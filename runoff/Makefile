# set the compiler
CC := clang

# set the compiler flags
CFLAGS := 

# add header files here
HDRS := cs50.h

# add source files here
SRCS := runoff.c

# generate names of object files
OBJS := $(SRCS:.c=.o)

# name of executable
EXEC := runoff

# default recipe
all: $(EXEC)

# recipe for building the final executable
$(EXEC): $(OBJS) $(HDRS) Makefile
	$(CC) -o $@ $(OBJS) $(CFLAGS)

# recipe for building object files
#$(OBJS): $(@:.o=.c) $(HDRS) Makefile
#	$(CC) -o $@ $(@:.o=.c) -c $(CFLAGS)

# recipe to clean the workspace
clean:
	rm -f $(EXEC) $(OBJS)

.PHONY: all clean
