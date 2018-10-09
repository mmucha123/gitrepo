#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_prostokat.py
#  
#  Copyright 2018  <>

def prostokat1(a, b, znak):
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()
    
        
def prostokat2(a, b, znak, znak2):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(znak, end='')
            else:
                print(znak2, end=' ')
        print()
        
def choinka(h,znak):
    for i in range(h):
        for i in range(h)
           

    
def main(args):
    a=int(input("podaj 1, liczbę: "))
    b=int(input("podaj 2, liczbę: "))
    znak=(input("podaj znak: "))
    znak2=(input("podaj 2znak: "))
    h=int(input("podaj wysokość: "))
    prostokat1(a, b, znak)
    print(" ")
    print(" ")
    prostokat2(a, b, znak, znak2)
    choinka(h,znak)
    print(" ")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
