/*
 * szyfr_cezara.cpp
 * 
 * Copyright 2019  <>
 * 

 */


#include <iostream>
using namespace std;
#define MAKS 100

void szyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0'){
        kod = (int)tb[i];
        kod += klucz;
        cout<<(char)kod;
        i++;
        
        
        
        }
    
    
    }



int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    cout << "Podaj tekst:\n";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz:\n";
    cin >> klucz;
    szyfruj(tekst, klucz);
    
    
	
	return 0;
}

