#include <iostream>
using namespace std;
#define EDGE_LEN 20

int main()
{
	int i, j;
	int a[EDGE_LEN][EDGE_LEN];
	for(i = 0; i < EDGE_LEN; i++)
		for(j = 0; j < EDGE_LEN; j++)
			cin >> a[i][j];

	int down, right, ddiag, udiag, maxprod = 0;
	for(i = 0; i < EDGE_LEN; i++)
		for(j = 0; j < EDGE_LEN; j++){
			down = right = ddiag = udiag = 0;
			if( i + 3 < EDGE_LEN)
				down = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j];
			if( j + 3 < EDGE_LEN)
				right = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3];
			if( i + 3 < EDGE_LEN && j + 3 <= EDGE_LEN)
				ddiag = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3];
			if( j + 3 < EDGE_LEN && i - 3 >= 0)
				udiag = a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3];
			if( down > maxprod)
				maxprod = down;
			if( right > maxprod)
				maxprod = right;
			if(ddiag > maxprod)
				maxprod = ddiag;
			if(udiag > maxprod)
				maxprod = udiag;
		}
	cout << maxprod << endl;
	return 0;
}
