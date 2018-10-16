#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  oblicznie potęgi podstawy podniesionej do wykładnika  


def potega_it(a, n):
    wynik = 1
    
    for i in range(n):
        #print(wynik)
        wynik = wynik * a
        
        
    
    return wynik
    



def main(args):
    #a=int(input("Podaj liczbę; "))
    #n=int(input("Podaj liczbę2; "))
    #print("Potęga {} do {} wynosi {}".format(a, n, potega_it(a, n)))
    assert(potega_it(1, 1) == 1)
    assert(potega_it(4, 4) == 256) 
    assert(potega_it(1, 0) == 1)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
