# behaviortrees
###### COMP 131: Artificial Intelligence
###### Homework 1: Behavior Trees
###### Tufts University


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
    in functions throughout throughout.

  #### Function(s) Implemented Include:
    * battery_check,
    * go_home,
    * dock,
    * battery_charge,
    * cleaning_function,
    * spot_check,
    * battery_deplete,
    * complete,
