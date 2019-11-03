#!/usr/bin/ python

#Program parses first the command ine arguments. Then it calculates the sum,
#average or median from the numbers in a given input file.
#Thereafter it compares the result to a number given in the command line and 
#prints out the result of the wanted comparison.
#The read numbers first are collected into a list.
#This program is made using the python 3.8.0 version containing the 
#statistics.median function. It is available from version 3.4 onwards.


import sys, argparse, statistics 

parser = argparse.ArgumentParser()
parser.add_argument('InputFileName', help='name of the input file')
parser.add_argument('sum_avg_or_median', choices=['sum', 'avg', 'median'], help="Calculation choices are: sum, average or median")
parser.add_argument('-gt', action='store_true', help="comparison operator greater than")
parser.add_argument('-lt', action='store_true', help="comparison operator less than")
parser.add_argument('-eq', action='store_true', help="comparison operator equal to")
parser.add_argument('-n', type=float, help="decimal number to be compared with the result")

args = parser.parse_args()

def calculate_sum(list_of_the_read_numbers):
#Function calculates sum of the integer type items 
#using the given list as input.
    total_sum = 0
    for each_number in list_of_the_read_numbers:
        total_sum += each_number
    return total_sum

def calculate_average(list_of_the_read_numbers):
#Function calculates average of the numbers given as the input list.
    return (calculate_sum(list_of_the_read_numbers)) / len(list_of_the_read_numbers)

def calculate_median(list_of_the_read_numbers):
#Function calculates median from the given list of numbers by sorting
#it first in ascending order.
    list_of_the_read_numbers.sort()
    return statistics.median(list_of_the_read_numbers)

def print_result_of_the_comparison(result_of_the_calculation):
#Function prints result of the comparision according to the given 
#comparison operator, provided that that argument '-n' is given.
#Otherwise, text of missing argument is printed out.
#If no comparison operator is given then result of the choice
#given as command line argument is printed out.
    if (args.gt or args.lt or args.eq):
        if (args.n):
            print("{0} is {1}".format(args.sum_avg_or_median,result_of_the_calculation))
            if (args.gt):
                if (result_of_the_calculation > args.n):
                    print("{0} is greater than {1}".format(result_of_the_calculation,args.n))
                else:
                    print("{0} is not greater than {1}".format(result_of_the_calculation,args.n))
            elif (args.lt):
                if (result_of_the_calculation < args.n):
                    print("{0} is less than {1}".format(result_of_the_calculation,args.n))
                else:
                    print("{0} is not less than {1}".format(result_of_the_calculation,args.n))
            elif (result_of_the_calculation == args.n):  #args.eq
                print("{0} is equal to {1}".format(result_of_the_calculation,args.n))
            else:
                print("{0} is not equal to {1}".format(result_of_the_calculation,args.n))
        else:
            print("Argument -n is missing")
    else:
        print("{0} is {1}".format(args.sum_avg_or_median,result_of_the_calculation))

def print_results_of_the_calculations(list_of_the_read_numbers):
#Function prints first the wanted calculation choice and then the detailed
#information, whether the result is greater or less than or equal to the
#optionally given number.
    if (args.sum_avg_or_median == 'sum'):
        calculation_result = calculate_sum(list_of_the_read_numbers)
        print_result_of_the_comparison(calculation_result)
    elif (args.sum_avg_or_median == 'avg'):
        calculation_result = calculate_average(list_of_the_read_numbers)
        print_result_of_the_comparison(calculation_result)
    else:
        calculation_result = calculate_median(list_of_the_read_numbers)
        print_result_of_the_comparison(calculation_result)

def main(argv):
    with open(args.InputFileName, 'r') as inputfile: #open the input data file
        line_to_be_read = inputfile.readline().strip("\n")
        integer_list_of_the_numbers = []
        while line_to_be_read.strip("\n").isdigit(): #assure digits in the string
            integer_list_of_the_numbers.append(int(line_to_be_read.strip("\n")))
            line_to_be_read = inputfile.readline().strip("\n")
        print_results_of_the_calculations(integer_list_of_the_numbers)
    print("Inputfile",args.InputFileName,"closed?",inputfile.closed)

if __name__ == '__main__':
    main(sys.argv[1:])
