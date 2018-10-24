#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw2.py
#  
#

def main(args):
    
    n = int(input("podaj 1. liczbę: "))
    while n < 1:
        print("Błedne dane")
        n = int(input("podaj 1. liczbę: "))
        
    m = int(input("podaj 2.liczbę: "))
    while m <= n:
        print("błędne dane")
        m = int(input("podaj 2. liczbę: "))
        
    for liczba in range(n, m + 1):
        print(liczba, " ",end=" ")
    

if __name__ == '__main__': 
    import sys
    sys.exit(main(sys.argv))
   
