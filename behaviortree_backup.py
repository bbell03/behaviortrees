# Caroline Vanderlee and Brandon Bell

import time
import sys

# Blackboard: Brandon, Caroline has started for testing
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


# Battery Functions: Caroline
# Roomba will always check battery first, then call cleaning function
def battery_check(blackboard):
    print "Battery level is " + str(blackboard.BATTERY_LEVEL)

    if blackboard.BATTERY_LEVEL < 30:
        print "Needs charging"
        go_home(blackboard)
        print "Battery level " +  str(blackboard.BATTERY_LEVEL) + "% sufficient"
    else:
        print "Charge sufficient to begin cleaning"

    # Cleaning begins once charge is sufficient in both cases
    cleaning_function(blackboard)
    return;


# Battery charge function
# Called within go_home, after roomba has found home and docked
def battery_charge(blackboard):
    print "Beginning charging process"
    i = blackboard.BATTERY_LEVEL
    for j in range(i,100):
        blackboard.BATTERY_LEVEL = j + 1
        # Delay; flush printed output for testing purposes
        sys.stdout.flush()
        time.sleep(0.1)
        print "Charging: " + str(blackboard.BATTERY_LEVEL) + "%"
    print "Fully charged at " + str(blackboard.BATTERY_LEVEL) + "%"
    return;


# Go Home: Brandon
def go_home(blackboard):
    print "Go Home Start"
    if blackboard.HOME_PATH:
        print "Navigating to home location at " + str(blackboard.HOME_PATH)
        dock(blackboard)
    return;


# Dock: Brandon
def dock(blackboard):
        battery_charge(blackboard)
        return;


# Cleaning Function: Caroline
def cleaning_function(blackboard):
    print "Checking for cleaning"
    if blackboard.SPOT == False and blackboard.GENERAL == False:
        print "No cleaning command requested"
    else:
        print "A clean has been requested"

        # Run spot check first
        if blackboard.SPOT == True:
            print "A spot check has been requested"
            # Spot cleaning: 20 second intensive
            spot_check(blackboard, 20)
            print "Spot check completed: spot is " + str(blackboard.SPOT)

        # Run general clean
        print "Beginning general clean"

        # While loop for repetitive clean
        while blackboard.GENERAL == True:
            # Manually check battery level and charge if needed
            if blackboard.BATTERY_LEVEL < 30:
                print "Needs charging"
                go_home(blackboard)
                print "Battery level " +  str(blackboard.BATTERY_LEVEL) + "% sufficient"
            # Check for dusty spot
            if blackboard.DUSTY_SPOT == True:
                print "Dusty spot detected"
                # Dusty spot: 35 second intensive
                spot_check(blackboard, 35)
                print "Intensive cleaning completed: Dusty spot " + str(blackboard.DUSTY_SPOT)
            # Check if everything is clean
            if blackboard.DUSTY_SPOT == False:
                # Done with general cleaning
                complete(blackboard)
        # End while loop

        print "General clean completed"
        print "Battery at " + str(blackboard.BATTERY_LEVEL)
    return;

# Spot Check: Both
def spot_check(blackboard, secs):
    print "Running spot check: " + str(secs) + " seconds"
    # Flush printed output
    sys.stdout.flush()
    time.sleep(secs)
    # 20 seconds for normal spot check, else 35 seconds for dusty spot
    if secs == 20:
        blackboard.SPOT = False
    else:
        blackboard.DUSTY_SPOT = False
    # Deplete battery for each clean
    battery_deplete(blackboard, secs)
    return;

# Return general clean complete
def complete(blackboard):
    blackboard.GENERAL = False
    return;

# Battery depletion
def battery_deplete(blackboard, val):
    blackboard.BATTERY_LEVEL = blackboard.BATTERY_LEVEL - val
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
