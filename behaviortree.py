# Caroline Vanderlee and Brandon Bell

# Blackboard: Brandon, Caroline has started for testing
class blackboard:
    BATTERY_LEVEL = 100
    SPOT = False
    GENERAL = False
    DUSTY_SPOT = False
    HOME_PATH = 0

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

# Go Home: Brandon
def go_home(blackboard):
    print "Finding docking station to charge"
    # Once charged:
    print "Fully charged and ready to begin cleaning"
    cleaning_function(blackboard)
    return;

# Cleaning Functions: Caroline
def cleaning_function(blackboard):
    print "Beginning cleaning function"
    return;

# Spot Check: Both
def spot_check(blackboard):
    return;
