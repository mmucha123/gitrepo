#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3.py
#  
def liczby3():
    
   
    licznik = 0
    for i in range(1, 10):        # pętla setek
        for j in range(10):        # pętla dziesiątek   
            for k in range(10):     # pętla jedności  
                if i != j != k != i:                                   
                    print("{}{}{} ".format(i, j, k), end=" ")
                    licznik = licznik + 1 
    return licznik
            


def main(args):
    print("liczby 3-cyfrowe",liczby3())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
