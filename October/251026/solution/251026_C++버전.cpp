#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int h, w;
	cin >> h >> w;
	vector<int> height(w);
	for (int i = 0; i < w; i++) cin >> height[i];

	vector<int> left_max(w), right_max(w);

	// 왼쪽 최대 누적
	left_max[0] = height[0];
	for (int i = 1; i < w; i++) {
		left_max[i] = max(left_max[i-1], height[i]);
	}

	// 오른쪽 최대 누적
	right_max[w-1] = height[w-1];
	for (int i = w - 2; i >= 0; i--) {
		right_max[i] = max(right_max[i+1], height[i]);
	}

	int total_water = 0;
	for (int i = 0; i < w; i++) {
		total_water += min(left_max[i], right_max[i]) - height[i];
	}

	cout << total_water << "\n";
	return 0;
}