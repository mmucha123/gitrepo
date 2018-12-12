/*
 * sortowanie.cpp
 * 
 * Copyright 2018  <>

 */


#include <iostream>
#include <csstdlib>

using namespace std;


void wypelnij(int tab [], int roz) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    cout << "Wprowadż " << roz << " liczb: " << endl;
    for(int i=0; i<roz; i++){
        tab[i] = rand() % 101; // liczby od zera do 100
        }
    }


void drukuj(int tab [], int roz) {
    
    for(int i=0; i<roz; i++){
        cout << tab[i] << " ";
        }
    }

int main(int argc, char **argv)
{
	
	return 0;
}

