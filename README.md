# general-purpose-sw-material
Repository containing sw components for different purposes, like coding tests etc.

This repository contains currently two subdirs: cpp and python. They have been created for the c++ and python files, respectively.
There are currently one .cpp and a couple of .py files in those subdirs.

Example: How to run program python/MultipleofXandY.py?

Create an input file containing the x and y values, as well the upper limit:

emacs input_file.txt

2 5 11
14 23 56

Run the program by giving name of the output file in the command:

python.exe MultipleofXandY.py input_file.txt output_file.txt

11: 10 8 6 5 4 2
56: 46 42 28 23 14


Outputfile contents : output_file.txt
11: 10 8 6 5 4 2
56: 46 42 28 23 14

Outputfile  closed : True
Inputfile closed : True

Example: How to run program Pythagoras.cpp?

Create an input file containing legs of the triangle:

emacs Input.dat

legA    legB
17.2457 29.6788
14.5789 24.4326
15.7677 24.1234
17.6677 25.4567

Run the program by giving name of the output file in the command:

$ g++ -o Pythagora Pythagoras.cpp

$ ./Pythagora Input.dat Output.dat

$ cat Output.dat

legA    legB      hypotenusa
4.44365 7.44706   8.67206
4.80599 7.35281   8.78416

These instructions to be added to branch modification_of_MultipleofXandY.
