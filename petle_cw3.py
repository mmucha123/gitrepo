#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw2.py
#  
#

def main(args):
    
    m = int(input("podaj 1. liczbę: "))
    while m < 1:
        print("Błedne dane")
        m = int(input("podaj 1. liczbę: "))
        
    
        
    for liczba in range(0, m + 1):
        print(liczba * liczba, " ",end=" ")
    

if __name__ == '__main__': 
    import sys
    sys.exit(main(sys.argv))
   
