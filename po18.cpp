//see the no recursion version in problem 67
//if recursion, use dynamic programming.
#include <iostream>
using namespace std;

int w[15][15];
int d[15][15];

int MaxPath(int i, int j)
{
	if(i == 14)
		return w[i][j];
	if (d[i][j] == 0)
		d[i][j] = w[i][j] + max(MaxPath(i+1, j), MaxPath(i+1, j+1));
	return d[i][j];
}

int main()
{
	for(int i = 0; i < 15; i++)
		for(int j = 0; j <= i; j++)
			cin >> w[i][j];
	cout << MaxPath(0,0);
}
