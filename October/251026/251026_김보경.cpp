#include <iostream>
using namespace std;

int h, w;
int map[500][500];

int main() {
	cin >> h >> w;
	int height;
	for (int i = 0; i < w; i++)
	{
		cin >> height;
		for (int j = 0; j < height; j++)
		{
			map[h - j-1][i] = 1;
		}
	}
	

	
	for (int row = 0; row < h; row++)
	{
		int mode = 0;	// 행별 리셋
		int mark = 0;

		for (int c = 0; c < w; c++)
		{
			if (map[row][c] == 1 && mode ==0) {
				mode = 1;
				mark = c;
				
			}
			if (map[row][c] == 1 && mode == 1) {
				if (c == mark + 1) {
					mark = c;
					continue;	// 연속 제외
				}

				for (int m = mark+1; m < c; m++)
				{
					map[row][m] = 2;
				}
				mark = c;
			}
		}
	}


	int cnt = 0;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			// cout << map[i][j];
			if (map[i][j] == 2) cnt++;
		} // cout << '\n';
	}

	cout << cnt;
	return 0;
}
