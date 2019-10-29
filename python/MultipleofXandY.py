#!/usr/bin/ python

#This program reads ordinary numbers from a given input file.
#There are three numbers in each line of the file. Multiples
#shall be calculated from the first two numbers in such a way
#that the result is always less than the third number.
#Finally, the multiples will be sorted in descending order,
#then printed out on the screen and saved into an output file.

import sys

list_of_x_and_y = []
going_through_two_values__x_and_y = 2

def return_list_of_multiples_of_x_and_y( x_or_y, last_item_in_input_line_list ):
#Go through the inputfile list and multiply its first two items with ordinary numbers starting
#from one. Append each matching result into the list, provided that it is not already there.
    if (last_item_in_input_line_list > 1):
        for multiplier_of_x_or_y in range(1, (last_item_in_input_line_list - 1)):
            result_of_multiplication = multiplier_of_x_or_y * int(x_or_y)
            if (result_of_multiplication < last_item_in_input_line_list and list_of_x_and_y.count(result_of_multiplication)==0):
                list_of_x_and_y.append(result_of_multiplication)
    else:
        print("No multiplies for this input file data:",int(x_or_y))

def print_contents_of_output_file(original_output_file_as_a_string):
#Procedure opens the original output file again and prints out its
#contents.
    print("\n")
    print("Outputfile contents :",original_output_file_as_a_string)
    with open(original_output_file_as_a_string, 'r') as new_input_file:
        file_contents = new_input_file.read()
        print(file_contents)

def print_list_of_multiples( last_input_list_item, sorted_list_of_xy_multiples, output_file_name ):
#Procedure prints the given list of xy multiplies on screen and into a file.
    print("{0}: {1}".format(last_input_list_item,' '.join(map(str, sorted_list_of_xy_multiples))))
    output_file_name.write(str(last_input_list_item))
    output_file_name.write(": ")
    output_file_name.write(' '.join(map(str,  sorted_list_of_xy_multiples)))
    output_file_name.write("\n")
    
def main(argv):
    with open(sys.argv[1], 'r') as inputfile:
        with open(sys.argv[2], 'w') as outputfile:
            str_file_name = sys.argv[2]
            line_to_be_read = inputfile.readline()
            while line_to_be_read:
                input_line_as_a_list = line_to_be_read.split()
                last_input_list_item = int(input_line_as_a_list[-1])
                for list_item in range(going_through_two_values__x_and_y):
                    return_list_of_multiples_of_x_and_y( input_line_as_a_list[list_item], last_input_list_item )
                list_of_x_and_y.sort(reverse = True)
                print_list_of_multiples( last_input_list_item, list_of_x_and_y, outputfile )
                del list_of_x_and_y[:]
                line_to_be_read = inputfile.readline()
        print_contents_of_output_file(str_file_name)
        print("Outputfile  closed :",outputfile.closed)
    print("Inputfile closed :",inputfile.closed)

if __name__ == '__main__':
    main(sys.argv[1:])
