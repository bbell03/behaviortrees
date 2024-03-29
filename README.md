# behaviortrees
###### COMP 131: Artificial Intelligence
###### Homework 1: Behavior Trees
###### Tufts University

###### Please note that this project does not run on an actual Roomba robot and was made strictly for academic purposes.

# README

### Author(s): Caroline Vanderlee and Brandon Bell


### CODE DETAILS

  #### IMPLEMENTATION:
    We expect that our solution has been completely and correctly implemented.
    This code was written in Python 2.7.8.

  #### ARCHITECTURE:
    Our solution makes use of modularity and object oriented design to
    implement the various functions of a Roomba robot.

    All functions take a blackboard object as input complete with attributes
    which correspond to those of the Roomba robot:
      * BATTERY_LEVEL,
      * SPOT,
      * GENERAL,
      * DUSTY_SPOT,
      * HOME_PATH,

    This program gives the option for user input to populate the attribtues of
    the blackboard object.

    Otherwise, it populates blackboard with default test values and then begins roomba procedure.

    This object is parsed on program start, and its attributes are used heavily
    in functions throughout.

  #### FUNCTION(S) IMPLEMENTED INCLUDE:
    * battery_check,
      * inputs: blackboard object
      * outputs: none
      * functionality: Checks if the BATTERY_LEVEL attribute of blackboard
      is less than 30 and if so calls go_home, and in any case, subsequently
      calls the cleaning_function
    * go_home,
      * inputs: blackboard object
      * outputs: none
      * functionality: If a HOME_PATH exists, the Roomba will navigate to its
      home location and subsequently call dock
    * dock,
      * inputs: blackboard object
      * outputs: none
      * functionality: Makes call to battery charge
    * battery_charge,
      * inputs: blackboard object
      * outputs: none
      * functionality: Saves BATTERY_LEVEL blackboard attribute to a variable,
      and ensures that BATTERY_LEVEL is 100 before returning
    * cleaning_function,
      * inputs: blackboard object
      * outputs: none
      * functionality: Encompasses major functionality of this program --
      First checks for SPOT == FALSE, and GENERAL == FALSE to evaluate whether
      cleaning is even necessary. If no clean is necessary the function prints
      succeeded and returns. Otherwise, when SPOT == TRUE and while GENERAL ==
      TRUE the program executes general cleaning procedure, making calls to
      functions go_home, spot_check, and complete
    * spot_check,
      * inputs: blackboard objects, secs
      * outputs: none
      * functionality: prints message "RUNNING", flushes the system, and
      runs processes according to a time conditional -- if secs == 20
      the program executes a normal clean otherwise it executes a deep clean
    * battery_deplete,
      * inputs: blackboard object and a value representing the amount of total
      battery missing.
      * outputs: none
      * functionality: Updates BATTERY_LEVEL attribute as battery depletes
    * complete
      * inputs: blackboard object
      * outputs: none
      * functionality: Sets the value of GENERAL to FALSE on clean complete

  #### METHODOLOGY:
    Our program is implemented according to the behavior tree
    diagram present in the homework specification found at
    https://canvas.tufts.edu/courses/9172/assignments/55650
    In our implementation, the battery_check portion of the tree is handled
    by the battery_check function and relevant functions within its body
    while the cleaning portion of the tree is handled by the cleaning_function
    and those functions which it calls.
