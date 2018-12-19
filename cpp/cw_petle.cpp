/*
 * cw_petle.cpp
 * 
 * Copyright 2018  <>
  
 * 
 */


#include <iostream>
using namespace std;

void cw01(){
    int n = 0;
    int suma = 0;
    while(suma < 75){
        cout << "Podaj cyfrę; ";
        cin >> n;
        suma = suma + n;
        
        
        }
    cout << suma << endl;
   }
    
void cw02(){
    int n = 0;
    int m = 0;
    cout << "Podaj przedział; ";
    cin >> n;
    cout << "Podaj przedział; ";
    cin >> m;
    
    for(int i = n; i <=m; i++){
        cout << i << endl;
        }
    
    
    
    }

void cw03(){
    int n = 0;
    cout << "Podaj liczbę: ";
    cin >> n;
    int suma = 0;
    for(int i = 0; i<=n; i++){
        
        suma = i*i;
        cout <<"kwadrat liczb: " << suma << endl;
        }
}





int main(int argc, char **argv)
{
    cw01();
	cw02();
    cw03();
    
	return 0;
}

