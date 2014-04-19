#include <iostream>
using namespace std;
int mem[1000001];

int lenOfCollatzSeq(long long n)
{
	if(mem[n] != 0)
		return mem[n];
	int len = 1;
	while(n != 1){
		if(n % 2 == 0){
			n /= 2;
			if(n <= 1000000 && mem[n] != 0){
				return len + mem[n];
			}
		}
		else{
			n = 3 * n + 1;
			if(n <= 1000000 && mem[n] != 0){
				return len + mem[n];
			}
		}
		len++;
	}
	return len;
}

int main()
{
	int len,max,index;
	len = max = 0;
	for(int i = 1; i <= 1000000; i++){
		len = lenOfCollatzSeq(i);
		mem[i] = len;
		if(len > max){
			max = len;
			index = i;
		}
	}
	cout << index << endl;
}
