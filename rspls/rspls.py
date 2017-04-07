import random


# dicts to simplify name_to_number and number_to_name
name_number = {"rock": 0, "Spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
number_name = {0: "rock", 1: "Spock", 2: "paper", 3: "lizard", 4: "scissors"}


def name_to_number(name):
    """ Maps name to its number
        Well, I am not sure if we was supposed to use if/elif/else here,
        so I decided to user dicts, it makes the code so much simpler
    """
    return name_number[name]


def number_to_name(number):
    """ Maps number to its name. See name_to_number comments above
    """
    return number_name[number]


def rpsls(player_choice):
    print
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    comp2player_diff = (comp_number - player_number) % 5
    if (comp2player_diff == 0):
        print "Player and computer tie!"
    elif ((comp2player_diff == 1) or (comp2player_diff == 2)):
        print "Computer wins!"
    else:
        print "Player wins!"


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
