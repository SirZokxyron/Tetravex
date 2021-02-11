##################################
#             Vars               #
##################################

# C Compiler
CC = clang

# Path to header files
INC = ./includes/

# Path to package files
LIB = ./libraries/

# Path to test files
EXE = ./tests/

# Link editing options
LNKOPT = -L$(LIB) -lm

# Header and Object file search
INCOPT = -I$(INC)

# General compiling options
CMPOPT = -g -Wall $(INCOPT)

# Executable files
EXEFILES = test_name

##################################
#            Default             #
##################################

all : $(EXEFILES)

##################################
#        Compiling rules         #
##################################

%.o : $(LIB)%.c
	@echo "Compiling package "$*
	$(CC) -c $(CMPOPT) $<

%.o : $(EXE)%.c
	@echo "Compiling test "$*
	$(CC) -c $(CMPOPT) $<

% : %.o
	@echo "Creating executable "$@
	$(CC) $^ $(LNKOPT) -o $@

##################################
#      Project compilation       #
##################################

###############
#   Package   #
###############

# package.o : package.c header.h
# package2.o : package2.c header2.h package.o

###############
# Executables #
###############

# executable : package.o package2.o

##################################
#      Directory Cleaning        #
##################################

clean :
	@echo "Cleaning .o files"
	rm -f *.o 2> /dev/null

clear :
	@echo "Cleaning executables"
	rm -f $(EXEFILES) 2> /dev/null