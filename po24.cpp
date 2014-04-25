#include <iostream>
#include <algorithm>
using namespace std;

int num = 0;
// swap!
void perm(int a[], int start, int end)
{
	if(start == end && ++num == 1000000){
		for(int i = 0; i <= end; i++)
			cout << a[i];
		cout << endl;
		return;
	}

	// we should ensure the swap according to sort
	int tmp[10];
	for(int i = 0; i < 10; i++)
		tmp[i]=a[i];
	
	sort(tmp + start, tmp + end + 1);

	for(int i = start; i <= end; i++){
		int j = start;
		for(j = start; j <= end; j++){
			if(tmp[i] == a[j]){
				break;
			}
		}
		swap(a[start], a[j]);
		perm(a, start+1, end);
		swap(a[start], a[j]);
	}
}

int main()
{
	int a[] = {0,1,2,3,4,5,6,7,8,9};
	perm(a, 0, 9);
}

