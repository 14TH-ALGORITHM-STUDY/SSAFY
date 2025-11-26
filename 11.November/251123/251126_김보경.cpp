#include <iostream>
using namespace std;

int n;
int t;

int withtwoandone(int num) {
	if (num % 2 == 0) {
		return num / 2 + 1;
	}
	else return (num + 1) / 2;
}

int main() {
	cin >> t;
	int cnt = 0;
	for (int tc = 0; tc < t; tc++)
	{
		cnt = 0;
		cin >> n;
		int three = n / 3;
		for (int i = 0; i <= three; i++)
		{
			cnt += withtwoandone(n - i * 3);
		}
		cout << cnt << '\n';
	}
	return 0;
}
