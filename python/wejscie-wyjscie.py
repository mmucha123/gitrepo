#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py




def main(args):
    a = input ("podaj 1. liczbę: ")
    b = input ("podaj 2. liczbę: ")
    print(a)
    print(b)
    
    print ("Suma;", a+b)
    print ("różnica:", a-b)
    print ("iloczyn;", a*B)
    print ("iloraz;", a/b)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
