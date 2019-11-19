"""
Resource file for calculating the statistics.
"""


from statistics import median
from statistics import mean


def calculate_sum(list_of_the_read_numbers):
    """ Function calculates sum of the numbers in the given list """

    return sum(list_of_the_read_numbers)


def calculate_mean(list_of_the_read_numbers):
    """ Function calculates mean of the numbers in the given list """

    return mean(list_of_the_read_numbers)


def calculate_median(list_of_the_read_numbers):
    """ Function calculates median from the numbers in the given list """

    return median(list_of_the_read_numbers)


def return_result_of_the_calculation(wanted_calculation, list_of_the_read_numbers):
    """ Function returns result of the wanted calculation: sum, mean or median,
        based on the list of the read input file numbers """

    if wanted_calculation == 'sum':
        calculation_result = calculate_sum(list_of_the_read_numbers)
    elif wanted_calculation == 'avg':
        calculation_result = calculate_mean(list_of_the_read_numbers)
    else:
        calculation_result = calculate_median(list_of_the_read_numbers)

    return calculation_result
