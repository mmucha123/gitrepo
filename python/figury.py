#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  



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
