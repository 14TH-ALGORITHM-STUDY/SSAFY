#include <iostream>
using namespace std;

struct conv {
	int gage;
	int in;
};

int n, k;
conv trail[201];

int main() {
	cin >> n >> k;
	for (int i = 1; i <= 2 * n; i++)
	{
		cin >> trail[i].gage;
	}

	int tr = 1;
	while (1) {
		// 1번
		conv swp = trail[2 * n];
		for (int i = 0; i < 2*n-1; i++)
		{
			trail[2 * n - i] = trail[2 * n - 1 - i];
		}
		trail[1] = swp;

		// 2번
		for (int i = n-1; i > 0; i--)
		{
			if (trail[n].in) trail[n].in = 0;	// 내리는 위치	<- 바로 즉시 확인!!
			if (trail[i].in) {
				if (trail[i+1].gage && trail[i + 1].in == 0) {
					trail[i + 1].gage -= 1;
					trail[i + 1].in = 1;
					trail[i].in = 0;
				}
			}
		}
		
		// 3번
		if (trail[1].gage) {
			trail[1].gage -= 1;
			trail[1].in = 1;
		}
		
		// 4번
		int cnt = 0;
		for (int i = 1; i <= 2*n; i++)
		{
			if (trail[i].gage == 0) cnt++;
		}

		if (cnt >= k) break;
		tr++;
	}

	cout << tr << '\n';
}
