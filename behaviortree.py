# Caroline Vanderlee and Brandon Bell

import time
import sys

# Blackboard: Brandon, Caroline has started for testing
class blackboard:
    BATTERY_LEVEL = 0
    SPOT = False
    GENERAL = False
    DUSTY_SPOT = False
    HOME_PATH = 0

    def __init__(self, b_val, s_val, g_val, d_val, h_val):
        self.BATTERY_LEVEL = b_val
        self.SPOT = s_val
        self.GENERAL = g_val
        self.DUSTY_SPOT = d_val
        self.HOME_PATH = h_val

# Battery Functions: Caroline
def battery_check(blackboard):
    print "Battery level is " + str(blackboard.BATTERY_LEVEL)
    if blackboard.BATTERY_LEVEL < 30:
        print "Needs charging"
        go_home(blackboard)
    else:
        print "Charge sufficient to begin cleaning"
    cleaning_function(blackboard)
    return;

def battery_charge(blackboard):
    print "Beginning charging process"
    i = blackboard.BATTERY_LEVEL
    for j in range(i,100):
        blackboard.BATTERY_LEVEL = j + 1
        # Delay
        sys.stdout.flush()
        time.sleep(0.1)
        print "Charging: " + str(blackboard.BATTERY_LEVEL) + "%"
    print "Fully charged at " + str(blackboard.BATTERY_LEVEL) + "%"
    return;

# Go Home: Brandon
def go_home(blackboard):
    print "Finding docking station to charge"
    # Once charged:
    blackboard.BATTERY_LEVEL = 100
    print "Ready to begin cleaning"
    return;

# Cleaning Functions: Caroline
def cleaning_function(blackboard):
    print "Checking for cleaning"
    if blackboard.SPOT == False and blackboard.GENERAL == False:
        print "No cleaning command requested"
    else:
        print "A clean has been requested"
        if blackboard.SPOT == True:
            print "A spot check has been requested"
            # Done spot
            blackboard.SPOT == False
            print "Spot check completed"
        print "Beginning general clean"
        if blackboard.BATTERY_LEVEL < 30:
            print "Needs charging"
            go_home(blackboard)
        if blackboard.DUSTY_SPOT == True:
            print "Dusty spot detected"
            # Done intensive
            blackboard.DUSTY_SPOT == False
            print "Intensive cleaning completed"
        # Done general
        blackboard.GENERAL == False
        print "General clean completed"
    return;

# Spot Check: Both
def spot_check(blackboard):
    return;


# Tests
#
# print "TEST ONE: Full battery, no commands"
# b_one = blackboard(100, False, False, False, 0)
# battery_check(b_one)
#
# print "\nTEST TWO: 30% battery, no commands"
# b_two = blackboard(30, False, False, False, 0)
# battery_check(b_two)
#
# print "\nTEST THREE: Low battery, no commands"
# b_three = blackboard(10, False, False, False, 0)
# battery_check(b_three)
#
# print "\nTEST FOUR: 30% battery, spot command"
# b_four = blackboard(30, True, False, False, 0)
# battery_check(b_four)
#
# print "\nTEST FIVE: 30% battery, general command"
# b_five = blackboard(30, False, True, False, 0)
# battery_check(b_five)
#
# print "\nTEST SIX: 30% battery, both general and spot commands"
# b_six = blackboard(30, True, True, False, 0)
# battery_check(b_six)
#
# print "\nTEST SEVEN: 10% battery, spot command"
# b_seven = blackboard(10, True, False, False, 0)
# battery_check(b_seven)
#
# print "\nTEST EIGHT: 10% battery, general command"
# b_eight = blackboard(10, False, True, False, 0)
# battery_check(b_eight)
#
# print "\nTEST NINE: 10% battery, both general and spot commands"
# b_nine = blackboard(10, True, True, False, 0)
# battery_check(b_nine)
#
# print "\nTEST TEN: 10% battery, general / spot / dusty commands"
# b_ten = blackboard(10, True, True, True, 0)
# battery_check(b_ten)
#
# print "\nTEST ELEVEN: 10% battery, general / spot / dusty commands, no recharge for battery before clean"
# b_eleven = blackboard(10, True, True, True, 0)
# cleaning_function(b_eleven)

print "\nTEST TWELVE: 10% battery, recharging"
b_twelve = blackboard(10, True, True, True, 0)
battery_charge(b_twelve)
