#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

int H, W;
int midx;
int result;
int MAP[500];

int main()
{
	freopen("input.txt", "r", stdin);

	cin >> H >> W;

	int max_height = -1;

	for (int i = 0; i < W; i++)
	{
		cin >> MAP[i];
		if (max_height <= MAP[i])
		{
			//최대 높이 갱신
			max_height = MAP[i];
			//최대 높이를 가지는 index값 저장
			midx = i;
		}
	}
	
	int left_max = -1;
	// ->
	for (int i = 0; i <= midx; i++)
	{
		if (left_max <= MAP[i])
		{
			left_max = MAP[i];
			continue;
		}

		if (left_max > MAP[i])
			result += left_max - MAP[i];
	}
	
	int right_max = -1;
	// <-
	for (int i = (W - 1); i >= midx; i--)
	{
		if (right_max <= MAP[i])
		{
			right_max = MAP[i];
			continue;
		}

		if (right_max > MAP[i])
			result += right_max - MAP[i];
	}

	cout << result << '\n';

	return 0;
}