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
EXEFILES = test_display test_logic test_rule test_rule

##################################
#            Default             #
##################################

all : $(EXEFILES)

##################################
#        Compiling rules         #
##################################

%.o : $(LIB)%.c
	@echo "Compiling package "$*
	@$(CC) -c $(CMPOPT) $<

%.o : $(EXE)%.c
	@echo "Compiling test "$*
	@$(CC) -c $(CMPOPT) $<

% : %.o
	@echo "Creating executable "$@
	@$(CC) $^ $(LNKOPT) -o $@

##################################
#      Project compilation       #
##################################

###############
#   Package   #
###############

# package.o : package.c header.h
# package2.o : package2.c header2.h package.o

tetravex.o : $(LIB)tetravex.c $(INC)tetravex.h
test_display.o : $(EXE)test_display.c tetravex.o
logic.o : $(LIB)logic.c $(INC)logic.h tetravex.o
test_logic.o : $(EXE)test_logic.c logic.o tetravex.o
test_rule.o : $(EXE)test_rule.c logic.o tetravex.o

###############
# Executables #
###############

# executable : package.o package2.o

test_display : test_display.o tetravex.o
test_logic : test_logic.o logic.o tetravex.o
test_rule : test_rule.o logic.o tetravex.o

##################################
#      Directory Cleaning        #
##################################

clean :
	@echo "Cleaning .o files"
	@rm -f *.o 2>/dev/null

clear :
	@echo "Cleaning executables"
	@rm -f $(EXEFILES) 2>/dev/null