def read_numbers_from_the_inputfile(input_file_name):
    """ Function reads numbers from the given input file and returns
        them as a list of integers """

    with open(input_file_name, 'r') as inputfile: #open the input data file
        line_to_be_read = inputfile.readline().strip("\n")
        integer_list_of_the_numbers = []
        while line_to_be_read.strip("\n").isdigit(): #assure digits in the string
            integer_list_of_the_numbers.append(int(line_to_be_read.strip("\n")))
            line_to_be_read = inputfile.readline().strip("\n")

    return integer_list_of_the_numbers
