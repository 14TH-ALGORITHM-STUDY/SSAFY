// 0 중에 1이 될 칸 3개를 선택, 2 위치를 ff로 변경 후 개수 최솟값인 걸 세는 것
// 1이 될 칸 선택하는 과정을 dfs 로 하면 timeout
// 1이 될 칸 선택하는 방법 - 2를 가둘 수 있는 방향으로
// -> 0인 칸을 리스트에 넣기

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

int map[8][8];
int simulmap[8][8];
int n, m;
int visited[8][8];
int num;
int safearea;
int max_safearea;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

struct point {
	int y, x;
};

void simulation() {	// 2 찾기
	queue<point> q;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (simulmap[i][j] == 2) {
				q.push({ i,j });
			}
		}
	}

	while (!q.empty()) {
		point now = q.front();
		q.pop();

		for (int d = 0; d < 4; d++)
		{
			point next = { now.y + dy[d], now.x + dx[d] };
			if (next.y < 0 || next.x < 0 || next.y >= n || next.x >= m) continue;
			if (simulmap[next.y][next.x] != 0) continue;
			simulmap[next.y][next.x] = 2;
			q.push(next);
		}
	}

	safearea = 0;		// 안전영역 계산
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (simulmap[i][j] == 0) safearea++;
		}
	}
	if (safearea > max_safearea) max_safearea = safearea;
	
}

void pickwall(int lev, int point) {
	if (lev == 3) {
		memset(simulmap, 0, sizeof(simulmap));
		for (int i = 0; i < n; i++)		// map 본뜨기
		{
			for (int j = 0; j < m; j++)
			{
				simulmap[i][j] = map[i][j];
			}
		}
		
		simulation();

		return;
	}
	
	for (int i = point+1; i < n*m; i++)
	{
		int y = i / m;
		int x = i % m;
		if (map[y][x] != 0) continue;
		map[y][x] = 1;
		pickwall(lev + 1, i);
		map[y][x] = 0;
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
		}
	}
	
	pickwall(0, -1);

	cout << max_safearea;

	return 0;
}