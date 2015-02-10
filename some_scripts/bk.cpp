#include <iostream> // PRODUS CARTEZIAN
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

std::ofstream g("out-1.txt", std::ofstream::out);
using namespace std;
int kkk = 1;
unsigned char n = 7,v[8],w[8] = {15, 15, 15, 15, 15, 15, 15, 15};
int nr = 0; //n-nr. de mulţimi, v-vectorul soluţie, w-conţine nr. de elemente di
//fiecare mulţime Sk

void BK(int k);
void afisare(int k);
int solutie(int k);
int main()
{
	g.open ("out-1.txt", std::ofstream::out);
	BK(1); //apelăm funcţia BK pentru selectarea primului element în v
	cout << nr << '\n';
	return 0;
}
void BK(int k) //funcţia becktreacking
{int i;
for (i=0;i<=w[k];i++) //parcurgem mulţimea Sk ={1,2,3,...,wk}
 {v[k]=i; //selectăm elementul i din mulţimea Sk
//nu avem funcţie de validare- nu avem condiţii de continuare
 if (solutie(k)){ //verificăm dacă am obţinut o soluţie
 afisare(k); //afişăm soluţia
 nr++;
}

else
 BK(k+1); //reapelăm funcia BK pentru completarea poziţiei următoare în
// vectorul v
 } //se închide un nivel de stivă si astfel se ajunge la poziţia k-1 în v
}

int solutie(int k) //funcţia soluţie determină momentul în care se ajunge la o soluţie
{if (k==n) //obţinem o soluţie dacă am dpus în vectorul v, n elemente
	return 1;
	return 0;
}
void afisare(int k) //afuşează o soluţie
{

	if(nr % 100000 == 0) {
		g.flush();
		g.close();
		kkk++;
		std::string titlu ("");
		titlu += "out-";
		char buffer[5];
		snprintf(buffer, sizeof(buffer), "%d", kkk);	
		titlu += (string)buffer;
		titlu += ".txt";
		g.open (titlu.c_str(), std::ofstream::out);
	}

	int p1 = (v[1] << 4) | v[2];
	int p2 = (0x1 << 4) | v[3];
	int p3 = (v[4] << 4) | v[5];
	int p4 = (0xB << 4) | v[6];
	int p5 = (v[7] << 4) | 0x5;
	g <<"{"<< 0xc1 << "," << p1 << "," << p2 << "," << p3 << "," << p4 << "," << p5 << "},";
}
