#!/usr/bin/ python

from Resource_fct_file import fct2, fct3

def fct1():
    a=2
    b=4
    c=a*b+6
    print(c) 
    d=pow(2,c-10)
    print(d)
    e=pow(d,a,b+1)
    print(e)

if __name__ == '__main__':
    fct1()
    fct2()
    fct3()
