"""!/usr/bin/ python"""

# Program parses the command line arguments, reads numbers from a given
# input file, calculates the sum, average or median from the numbers, and
# compares the result to a number given in the command line. Finally it
# prints out the result of the wanted comparison.
# This program requires at least python version 3.4, containing the
# statistics.median function.


import sys
from argument_parser_resource import parse_arguments
from reading_the_input_data_resource import read_numbers_from_the_inputfile
from calculating_the_statistics_resource import return_result_of_the_calculation
from printing_results_of_calculation_resource import print_result_of_the_calculation


def main(argv):
    """ The main function for reading the input file and printing out """
    #pylint: disable=unused-argument

    arguments = parse_arguments()
    numbers_read_from_the_inputfile = []
    numbers_read_from_the_inputfile = read_numbers_from_the_inputfile(arguments.InputFileName)
    result_of_the_calculation = return_result_of_the_calculation(arguments.sum_avg_or_median,
                                                                 numbers_read_from_the_inputfile)
    print_result_of_the_calculation(arguments, result_of_the_calculation)


if __name__ == '__main__':
    main(sys.argv[1:])
