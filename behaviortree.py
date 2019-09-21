# Caroline Vanderlee and Brandon Bell

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

# Go Home: Brandon
def go_home(blackboard):
    print "Finding docking station to charge"
    # Once charged:
    blackboard.BATTERY_LEVEL = 100
    print "Fully charged and ready to begin cleaning"
    cleaning_function(blackboard)
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
        print "Beginning general clean"
    return;

# Spot Check: Both
def spot_check(blackboard):
    return;

# Tests
print "TEST ONE: Full battery, no commands"
batt_one = blackboard(100, False, False, False, 0)
battery_check(batt_one)

print "TEST TWO: 30% battery, no commands"
batt_two = blackboard(30, False, False, False, 0)
battery_check(batt_two)

print "TEST THREE: Low battery, no commands"
batt_three = blackboard(10, False, False, False, 0)
battery_check(batt_three)

print "TEST FOUR: 30% battery, spot command"
batt_four = blackboard(30, True, False, False, 0)
battery_check(batt_four)

print "TEST FIVE: 30% battery, general command"
batt_five = blackboard(30, False, True, False, 0)
battery_check(batt_five)

print "TEST SIX: 30% battery, both general and spot commands"
batt_six = blackboard(30, True, True, False, 0)
battery_check(batt_six)

print "TEST SEVEN: 10% battery, spot command"
batt_seven = blackboard(10, True, False, False, 0)
battery_check(batt_seven)

print "TEST EIGHT: 10% battery, general command"
batt_eight = blackboard(10, False, True, False, 0)
battery_check(batt_eight)

print "TEST NINE: 10% battery, both general and spot commands"
batt_nine = blackboard(10, True, True, False, 0)
battery_check(batt_nine)
