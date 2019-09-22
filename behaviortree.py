# Caroline Vanderlee and Brandon Bell

import time
import sys


# Blackboard
class blackboard:
    BATTERY_LEVEL = 0
    SPOT = False
    GENERAL = False
    DUSTY_SPOT = False
    HOME_PATH = 1

    def __init__(self, b_val, s_val, g_val, d_val, h_val):
        self.BATTERY_LEVEL = b_val
        self.SPOT = s_val
        self.GENERAL = g_val
        self.DUSTY_SPOT = d_val
        self.HOME_PATH = h_val


# Initial battery check
# Roomba will check battery first, then call cleaning function
def battery_check(blackboard):
    if blackboard.BATTERY_LEVEL < 30:
        go_home(blackboard)
    # Cleaning begins once charge is sufficient
    cleaning_function(blackboard)
    return;


# Go home
def go_home(blackboard):
    if blackboard.HOME_PATH:
        dock(blackboard)
    return;


# Dock
def dock(blackboard):
    battery_charge(blackboard)
    return;


# Battery charge
def battery_charge(blackboard):
    i = blackboard.BATTERY_LEVEL
    for j in range(i,100):
        blackboard.BATTERY_LEVEL = j + 1
        # Delay
        time.sleep(0.1)
    return;


# Cleaning Function
def cleaning_function(blackboard):

    # Complete if there is nothing to clean
    if blackboard.SPOT == False and blackboard.GENERAL == False:
        print "SUCCEEDED"
    else:
        # Run spot check first: 20 second intensive
        if blackboard.SPOT == True:
            spot_check(blackboard, 20)
            print "SUCCEEDED"

        # General clean runs after spot check; while-loop for repetition
        while blackboard.GENERAL == True:
            # Manually check battery level and charge if needed
            if blackboard.BATTERY_LEVEL < 30:
                go_home(blackboard)
            # Check for dusty spot: 35 second intensive
            if blackboard.DUSTY_SPOT == True:
                spot_check(blackboard, 35)
            # Check if everything is clean: done with general cleaning if so
            if blackboard.DUSTY_SPOT == False:
                complete(blackboard)
                print "SUCCEEDED"

    return;


# Spot Check
def spot_check(blackboard, secs):
    # 20 seconds for normal spot check, else 35 seconds for dusty spot
    print "RUNNING"
    sys.stdout.flush()
    time.sleep(secs)
    if secs == 20:
        blackboard.SPOT = False
    else:
        blackboard.DUSTY_SPOT = False
    # Deplete battery for each clean
    battery_deplete(blackboard, secs)
    return;


# Battery depletion
def battery_deplete(blackboard, val):
    blackboard.BATTERY_LEVEL = blackboard.BATTERY_LEVEL - val
    return;


# Return general clean complete
def complete(blackboard):
    blackboard.GENERAL = False
    return;



# Tests

# print "TEST ONE: Full battery, no commands"
# b_one = blackboard(100, False, False, False, 1)
# battery_check(b_one)
#
# print "\nTEST TWO: 30% battery, no commands"
# b_two = blackboard(30, False, False, False, 1)
# battery_check(b_two)
#
# print "\nTEST THREE: Low battery, no commands"
# b_three = blackboard(10, False, False, False, 1)
# battery_check(b_three)
#
# print "\nTEST FOUR: 30% battery, spot command"
# b_four = blackboard(30, True, False, False, 1)
# battery_check(b_four)
#
# print "\nTEST FIVE: 30% battery, general command"
# b_five = blackboard(30, False, True, False, 1)
# battery_check(b_five)
#
# print "\nTEST SIX: 30% battery, both general and spot commands"
# b_six = blackboard(30, True, True, False, 1)
# battery_check(b_six)
#
# print "\nTEST SEVEN: 10% battery, spot command"
# b_seven = blackboard(10, True, False, False, 1)
# battery_check(b_seven)
#
# print "\nTEST EIGHT: 10% battery, general command"
# b_eight = blackboard(10, False, True, False, 1)
# battery_check(b_eight)
#
# print "\nTEST NINE: 10% battery, both general and spot commands"
# b_nine = blackboard(10, True, True, False, 1)
# battery_check(b_nine)
#
# print "\nTEST TEN: 10% battery, general / spot / dusty commands"
# b_ten = blackboard(10, True, True, True, 1)
# battery_check(b_ten)
#
# print "\nTEST ELEVEN: 10% battery, general / spot / dusty commands, no recharge for battery before clean"
# b_eleven = blackboard(10, True, True, True, 1)
# cleaning_function(b_eleven)
#
# print "\nTEST TWELVE: 10% battery, recharging"
# b_twelve = blackboard(10, True, True, True, 1)
# battery_charge(b_twelve)

print "\nTEST THIRTEEN: 30% battery, general / spot / dusty commands"
b_thirteen = blackboard(30, True, True, True, 1)
battery_check(b_thirteen)
