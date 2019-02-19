#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Kompresja.py
#  


def wspolczynnik1(Vk, Vnk):
    return Vk / Vnk * 100

def wspolczynnik1(Vk, Vnk):
    return (1 - Vk / Vnk) * 100


def main(args):
    Vk= float(input('rozmiar danych skomprewsowanych: '))
    Vnk =  float(input('Rozmiar danych nieskompresowanych: '))
    print("Dane zmiejszyły się o: ", wspolczynnik1(Vk, Vkn))
    print("Zaoszczędone miejsce: ", wspolczynnik1(Vk, Vkn))
    
    return 0
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
