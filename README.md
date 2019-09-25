# behaviortrees
###### COMP 131: Artificial Intelligence
###### Homework 1: Behavior Trees
###### Tufts University

###### Please note that this project does not run on an actual Romba robot and was made strictly for academic purposes.

# README

### Author(s): Caroline Vanderlee and Brandon Bell


### CODE DETAILS

  #### IMPLEMENTATION:
    We expect that our solution has been completely and correctly implemented.

  #### ARCHITECTURE:
    Our solution makes use of modularity and object oriented design to
    implement the various functions of a Rommba robot.

    All functions take a blackboard object as input complete with attributes
    which correspond to those of the Roomba robot:
      * BATTERY_LEVEL,
      * SPOT,
      * GENERAL,
      * DUSTY_SPOT,
      * HOME_PATH,

    This object is parsed on program start, and its attributes are used heavily
    in functions throughout.

  #### Function(s) Implemented Include:
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
      * inputs:
      * outputs:
      * functionality:
    * battery_deplete,
