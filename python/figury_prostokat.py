#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_prostokat.py
#  
#  Copyright 2018  <>

def prostokat1(a, b, z):
    for i in range(a):
        for j in range(b):
            print(z, end='')
        print()
    
        
def prostokat2(a, b, z):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1:
                print(z, end='')
            else:
                print(" ", end=' ')
            print()
        


def main(args):
    a=int(input("podaj 1, liczbę: "))
    b=int(input("podaj 2, liczbę: "))
    z=(input("podaj znak: "))
    for i in range(a):
        for j in range(b):
            print(z, end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
