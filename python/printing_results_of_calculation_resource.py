def print_result_of_the_calculation(argument, calculation_result):
    """ Function prints result of the wanted calculation "sum", "avg" or "median"
        taking into account the possible comparison operator as input """

    if argument.gt or argument.lt or argument.eq:
        if argument.n:
            print("{0} is: {1}".format(argument.sum_avg_or_median, calculation_result))
            if argument.gt:
                if calculation_result > argument.n:
                    print("{0} is greater than {1}".format(calculation_result, argument.n))
                else:
                    print("{0} is not greater than {1}".format(calculation_result, argument.n))
            elif argument.lt:
                if calculation_result < argument.n:
                    print("{0} is less than {1}".format(calculation_result, argument.n))
                else:
                    print("{0} is not less than {1}".format(calculation_result, argument.n))
            elif calculation_result == argument.n:
                print("{0} is equal to {1}".format(calculation_result, argument.n))
            else:
                print("{0} is not equal to {1}".format(calculation_result, argument.n))
        else:
            print("Argument -n is missing")
    else:
        print("{0} is: {1}".format(argument.sum_avg_or_median, calculation_result))
