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

==================================================================================

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


=================================================================================

Example: How to run program Codingtest.py?

Create an input file containing even amount of numbers:
emacs test.txt &
123
521
324
12
3
56
900
78

Run program Codingtest.py using different arguments:

c:\python38\python.exe Codingtest.py
usage: Codingtest.py [-h] [-gt] [-lt] [-eq] [-n N] InputFileName {sum,avg,median}
Codingtest.py: error: the following arguments are required: InputFileName, sum_avg_or_median


c:\python38\python.exe Codingtest.py -h
usage: Codingtest.py [-h] [-gt] [-lt] [-eq] [-n N] InputFileName {sum,avg,median}

positional arguments:
  InputFileName     name of the input file
  {sum,avg,median}  Calculation choices are: sum, average or median

optional arguments:
  -h, --help        show this help message and exit
  -gt               comparison operator greater than
  -lt               comparison operator less than
  -eq               comparison operator equal to
  -n N              decimal number to be compared with the result


c:\python38\python.exe Codingtest.py test.txt
usage: Codingtest.py [-h] [-gt] [-lt] [-eq] [-n N] InputFileName {sum,avg,median}
Codingtest.py: error: the following arguments are required: sum_avg_or_median


c:\python38\python.exe Codingtest.py test.txt sum
sum is 2017
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt -gg
usage: Codingtest.py [-h] [-gt] [-lt] [-eq] [-n N] InputFileName {sum,avg,median}
Codingtest.py: error: the following arguments are required: sum_avg_or_median


c:\python38\python.exe Codingtest.py test.txt sum -gt
Argument -n is missing
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt sum -gt -n 78
sum is 2017
2017 is greater than 78.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt sum -gt -n 7788
sum is 2017
2017 is not greater than 7788.0
Inputfile test.txt closed? True

c:\python38\python.exe Codingtest.py test.txt sum -lt 34
usage: Codingtest.py [-h] [-gt] [-lt] [-eq] [-n N] InputFileName {sum,avg,median}
Codingtest.py: error: unrecognized arguments: 34


c:\python38\python.exe Codingtest.py test.txt sum -lt -n 34
sum is 2017
2017 is not less than 34.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt sum -lt -n 3444
sum is 2017
2017 is less than 3444.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt sum -eq -n 2017
sum is 2017
2017 is equal to 2017.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt sum -eq -n 20170
sum is 2017
2017 is not equal to 20170.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg
avg is 252.125
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -gt -n 45
avg is 252.125
252.125 is greater than 45.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -gt -n 4556
avg is 252.125
252.125 is not greater than 4556.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -lt -n 56
avg is 252.125
252.125 is not less than 56.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -lt -n 5667
avg is 252.125
252.125 is less than 5667.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -eq -n 252
avg is 252.125
252.125 is not equal to 252.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt avg -eq -n 252.125
avg is 252.125
252.125 is equal to 252.125
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median
median is 100.5
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -gt -n 56
median is 100.5
100.5 is greater than 56.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -gt -n 5678
median is 100.5
100.5 is not greater than 5678.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -lt -n 900
median is 100.5
100.5 is less than 900.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -lt -n 90
median is 100.5
100.5 is not less than 90.0
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -eq -n 100.5
median is 100.5
100.5 is equal to 100.5
Inputfile test.txt closed? True


c:\python38\python.exe Codingtest.py test.txt median -eq -n 101
median is 100.5
100.5 is not equal to 101.0
Inputfile test.txt closed? True


Change test.txt to have odd amount of numbers:
emacs test.txt &
56
21
899
9326
1
88
43

c:\python38\python.exe Codingtest.py test.txt median
median is 56
Inputfile test.txt closed? True

c:\python38\python.exe Codingtest.py test.txt median -gt -n 21
median is 56
56 is greater than 21.0
Inputfile test.txt closed? True

C:\Users\Käyttäjä\eclipse-workspace\Coding_test_numbers\src>c:\python38\python.exe Codingtest.py test.txt median -lt -n 155
median is 56
56 is less than 155.0
Inputfile test.txt closed? True

C:\Users\Käyttäjä\eclipse-workspace\Coding_test_numbers\src>c:\python38\python.exe Codingtest.py test.txt median -eq -n 56
median is 56
56 is equal to 56.0
Inputfile test.txt closed? True
