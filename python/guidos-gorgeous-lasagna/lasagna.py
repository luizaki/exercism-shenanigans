"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers to add to the lasagna.
    :return: int - time (in minutes) it takes to make them.

    Function that takes the number of layers planned to add to the lasagna
    as an argument and returns how many minutes it will take to make them
    based on `PREPARATION_TIME`.
    """

    return PREPARATION_TIME * number_of_layers

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time in minutes.

    :param number_of_layers: int - number of layers to add to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time (in minutes) spent to cook the lasagna.

    Function that takes the number of layers planned to add to the lasagna
    and the actual minutes the lasagna has been in the oven as arguments
    and returns how many minutes have already elapsed in cooking.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time