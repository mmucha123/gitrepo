/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 * 
 */





#include <iostream>

using namespace std;





int zlicz(char tab[]){
    int i = 0; // indeks znaków w tablicy
    while (tab[i] != '\0') i++;
    return i;
}

void drukuj(char tab [], int roz) {
    
    for(int i=0; i<roz; i++){
        cout << tab[i] << " ";
        }
    }
    
void ascii(char tab [], int roz) {
    int kod = 0; //kod ascii znaku
    for(int i=0; i<roz; i++){
        kod = (int)tab[i];
        if (kod > 96 && kod < 123)
            cout << (char)(kod - 32) << " ";
        else
            cout << (int)tab[i] << " ";
        }
    }    
    
    
    
    
void liczznkai(char tab[], int roz){
    int spacje = 0;
    int interpunkcja = 0;
    int symbole = 0;
    int reszta = 0;
    for(int i=0; i<roz; i++){
        //~if (tab [i] == ' ') spacje ++;
        //~else if (tab[i] == '.' || tab[i] == ',')
            //~interpunckja++;
        //~else if (tab[i] == '(' || tab[i] == ')') symbole++;
        // todo: instrukcja switch
        switch(tab[i]){
            case ' ':
            case '\t':
                spacje++;
            break;
            case '.':
            case ',':
                interpunkcja++;
            break;
            case '(':
            case ')':
                symbole++;
            break;
            default:
                reszta++;
        }

        
        
    }
    cout << "Spacje:"<< spacje << endl;
    cout << "Interpunkcja:"<< interpunkcja << endl;
    cout << "Symbole:"<< symbole << endl;
    cout << "Reszta:"<< reszta << endl;
    }


int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char tab[rozmiar];
    cout << "Jak się nazywasz?" << endl;    
    //cin >> tab;
    cin.getline(tab, rozmiar);
    //cout << "Cześć "<< tab << "!"<< endl;
    ascii(tab, zlicz(tab));
    liczznkai(tab, zlicz(tab));
    return 0;
}

