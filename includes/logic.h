#ifndef _LOGIC_H_
#define _LOGIC_H_

#include "../includes/tetravex.h"

//* Return the string combination representing the CNJ form of the "header" for the file
void header(grid tetravex, FILE * filepointer);

//* Return the string combination representing the CNJ form of "coordinate unicity" for each square
void coord_unicity(grid tetravex, FILE * filepointer);

//* Return the string combination representing the CNJ form of "non superposition" for each square combo
void non_superposition(grid tetravex, FILE * filepointer);

//* Return the string combination representing the CNJ form of "number logic" for each square
void number_logic(grid tetravex, FILE * filepointer);

#endif