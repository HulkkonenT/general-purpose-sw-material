#!/usr/bin/ python

import sys 

def main(argv):
    with open(sys.argv[1], 'r') as inputfile:
        with open(sys.argv[2], 'w') as outputfile:
            line = inputfile.readline()
            while line:
                elem_list= []
                j = 0
                nbr_list = line.split()
                outputfile.write(nbr_list[2])
                for i in range(2):
                    for z in range(1, int(nbr_list[2]) - 1 ):
                        if (z*int(nbr_list[i]) < int(nbr_list[2])):
                            elem_list.insert(j, z*int(nbr_list[i]))
                            j += 1
                elem_list.sort()
                print("{0}: {1}".format(int(nbr_list[2]),' '.join(map(str, elem_list))))
                outputfile.write(": ")
                outputfile.write(' '.join(map(str, elem_list)))
                outputfile.write("\n")
                line = inputfile.readline()
        print(outputfile.closed)
    print(inputfile.closed)

if __name__ == '__main__':
    main(sys.argv[1:])
