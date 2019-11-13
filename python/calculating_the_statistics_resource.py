from statistics import median


def calculate_sum(list_of_the_read_numbers):
    """ Function calculates sum of the given numbers """

    total_sum = 0
    for each_number in list_of_the_read_numbers:
        total_sum += each_number
    return total_sum


def calculate_average(list_of_the_read_numbers):
    """ Function calculates average of the given numbers """

    return calculate_sum(list_of_the_read_numbers) / len(list_of_the_read_numbers)


def calculate_median(list_of_the_read_numbers):
    """ Function calculates median from the given numbers """

    return median(list_of_the_read_numbers)


def return_result_of_the_calculation(wanted_calculation, list_of_the_read_numbers):
    """ Function returns result of the wanted calculation: sum, average or median,
        based on the list of the read input file numbers """

    if wanted_calculation == 'sum':
        calculation_result = calculate_sum(list_of_the_read_numbers)
    elif wanted_calculation == 'avg':
        calculation_result = calculate_average(list_of_the_read_numbers)
    else:
        calculation_result = calculate_median(list_of_the_read_numbers)

    return calculation_result
