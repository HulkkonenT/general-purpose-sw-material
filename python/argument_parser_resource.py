"""
Resource file for parsing the comman line arguments.
"""


import argparse


def parse_arguments():
    """ Function parses arguments given on the command line """

    parser = argparse.ArgumentParser()
    parser.add_argument('InputFileName', help='name of the input file')
    parser.add_argument('sum_avg_or_median', choices=['sum', 'avg', 'median'],
                        help="Calculation choices are: sum, average or median")
    parser.add_argument('-gt', action='store_true', help="comparison operator greater than")
    parser.add_argument('-lt', action='store_true', help="comparison operator less than")
    parser.add_argument('-eq', action='store_true', help="comparison operator equal to")
    parser.add_argument('-n', type=float, default=10.0,
                        help="number to be compared with the result: default is 10.0")

    return parser.parse_args()
