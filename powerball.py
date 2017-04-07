# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
from random import randrange


def powerball():
    msg = "Today's numbers are " + \
           str(randrange(1, 60)) + ", " + \
           str(randrange(1, 60)) + ", " + \
           str(randrange(1, 60)) + ", " + \
           str(randrange(1, 60)) + ", and " + \
           str(randrange(1, 60)) + ". " + \
           "The Powerball number is " + str(randrange(1, 36)) + "."
    print msg


###################################################
# Tests
# Student should not change this code.

powerball()
powerball()
powerball()
