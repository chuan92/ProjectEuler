//see the difference with problem 18
#include <iostream>
using namespace std;

int w[100][100];
int d[100][100];

int main()
{
	for(int i = 0; i < 100; i++)
		for(int j = 0; j <= i; j++)
			cin >> w[i][j];
	for(int i = 0; i < 100; i++)
		d[99][i] = w[99][i];
	for(int i = 98; i >= 0; i--)
		for(int j = 0; j <= i; j++)
			d[i][j] = w[i][j] + max(d[i+1][j], d[i+1][j+1]);
	cout << d[0][0];
}
