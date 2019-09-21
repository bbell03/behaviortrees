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

# Tests
batt_full = blackboard(100, False, False, False, 0)
batt_30 = blackboard(30, False, False, False, 0)
batt_low = blackboard(10, False, False, False, 0)

battery_check(batt_full)
battery_check(batt_30)
battery_check(batt_low)
