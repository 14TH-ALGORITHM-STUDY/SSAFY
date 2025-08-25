#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int N;
int ans = 1;

int main()
{
	cin >> N;
	for (int i = N; i > 0; i--)
		ans *= i;

	cout << ans << '\n';
	return 0;
}