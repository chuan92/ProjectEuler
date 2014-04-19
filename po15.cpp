#include <iostream>
using namespace std;

const int edge = 20;
//watch the array lenght!!
//in fact (0,0) to (a,b) is (a+b) choose a
long long int mem[edge + 1][edge + 1];

long long int start(long long int a, long long int b)
{
	if(a > edge || b > edge)
		return 0;
	else if(a == edge && b == edge){
		mem[a][b] = 1;
		return 1;
	}
	else if(mem[a][b] != 0)
		return mem[a][b];
	else{
		mem[a][b] = start(a+1, b) + start(a, b+1);
		return mem[a][b];
	}
}

int main()
{
	cout << start(0, 0) << endl;
	return 0;
}
