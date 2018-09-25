#!/usr/bin/env python
# -*- coding: utf-8 -*-
#



def main(args):
    start=int(input("podaj 1, liczbę: "))
    stop=int(input("podaj 2, liczbę; "))
    
    if start>= stop:
        print("błędne dane")
        exit(0)
    
    for i in range(start, stop + 1) :
        if i % 2 == 0:
          print(i)
        else:
            print("Liczba nieparzysta")
            
    return 0
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
