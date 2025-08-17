/*백준 16507번 - 어두운 건 무서워
R(행) / C(열) 1 ~ 1,000
Q(사진 일부분의 밝기 평균을 알아볼 개수) 1~10,000
R개의 줄에 걸쳐 RXC 크기의 사진 정보가 주어진다.
사진의 각 픽셀에는 밝기를 의미하는 정수 K 1~1,000이 주어진다.
Q개의 두 꼭짓점을 의미하는 정수쌍이 주어진다.
직사각형의 밝기 평균을 출력해라. 평균은 정수 나눗셈으로 몫만 취한다!*/


//백준 채점시 73% 정도에서 시간초과 발생
//가장 중요한 포인트가 새로운 영역을 계산할 때, 앞전에 계산한 영역이 겹친다면 값을 활용하는 방법인거 같음.
//어떻게 그걸 표현할 수 있을지 고민해도 모르겠음.
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

struct Point 
{
	int r1, c1, r2, c2;
};

int R, C, Q;
int picture[1001][1001];
Point sub_picture[10001];
int ans[10001];
int total_sum;

void solve()
{
	for (int i = 1; i <= Q; i++)
	{
		int sum_pixel = 0;
		int r1 = sub_picture[i].r1;
		int r2 = sub_picture[i].r2;
		int c1 = sub_picture[i].c1;
		int c2 = sub_picture[i].c2;
		int area = (r2 - r1 + 1) * (c2 - c1 + 1);

		if (r1 == 1 && r2 == 1000 && c1 == 1 && c2 == 1000)
		{
			ans[i] = total_sum / area;
			continue;
		}

		if (area > ((R * C) - area) ) // 구하고자 하는 영역이 사진의 절반보다 크다면
		{
			for (int r = 1; r < r1; r++)
				for (int c = 1; c <= C; c++)
					sum_pixel += picture[r][c];

			for (int r = (r2 + 1); r <= R; r++)
				for (int c = 1; c <= C; c++)
					sum_pixel += picture[r][c];

			for (int c = 1; c < c1; c++)
				for (int r = r1; r <= r2; r++)
					sum_pixel += picture[r][c];

			for (int c = (c2 + 1); c <= C; c++)
				for (int r = r1; r <= r2; r++)
					sum_pixel += picture[r][c];

			ans[i] = ((total_sum - sum_pixel) / area);

		}

		else // 구하고자 하는 영역이 사진의 절반보다 작다면
		{
			for (int r = r1; r <= r2; r++)
				for (int c = c1; c <= c2; c++)
					sum_pixel += picture[r][c];

			ans[i] = (sum_pixel / area);
		}
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);
	cin >> R >> C >> Q;

	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cin >> picture[i][j];
			total_sum += picture[i][j];
		}
	}

	for (int k = 1; k <= Q; k++)
	{
		int r1, c1, r2, c2;
		cin >> r1 >> c1 >> r2 >> c2;
		sub_picture[k] = { r1, c1, r2, c2 };
	}

	solve();

	for (int p = 1; p <= Q; p++)
	{
		cout << ans[p] << "\n";
	}
	return 0;
}