#ifndef _LOGIC_H_
#define _LOGIC_H_

#include "../includes/tetravex.h"

//* Return the string combination representing the CNJ form of coordinate unicity for each square
//TODO : Upgrade this algorithm, because it's absolutely mega ugly. We're going through each bool two times, need only 1.
void coord_unicity(grid tetravex, FILE * filepointer);

#endif