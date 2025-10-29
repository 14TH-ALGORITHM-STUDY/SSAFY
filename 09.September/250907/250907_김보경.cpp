// 보물상자의 위치는 맵에서 거리를 파악해봐야 알 수 있는 것이므로, 맵 전체를 파악해야 됨
// 육지와 육지 사이의 거리는, 한 점을 기준으로의 거리 FF 로 파악하기 (각 점에서의 거리가 다르므로)
// 최대 거리만 출력하므로, dist에 map 거리 저장, min_dist 로 최대거리 저장

#include <iostream>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

struct point {
	int y, x;
};

int map[50][50];
int dist[50][50];
int h, w;
int max_dist;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void dimapping(int y, int x) {		// 현재 좌표에서 육지까지의 거리 dist에 구하기
	queue<point> q;
	q.push({y,x});
	dist[y][x] = 0;					// 시작점 표시
	
	while (!q.empty()) {
		point now = q.front();
		q.pop();

		if (dist[now.y][now.x] > max_dist) max_dist = dist[now.y][now.x];	// 노드의 거리 최대값 찾기

		for (int d = 0; d < 4; d++)
		{
			point next = { now.y + dy[d], now.x + dx[d] };
			if (next.y < 0 || next.x < 0 || next.y >= h || next.x >= w) continue;
			if (!map[next.y][next.x]) continue;
			if (dist[next.y][next.x] != -1) continue;					// 거리 계산 여부

			dist[next.y][next.x] = 1 + dist[now.y][now.x];
			q.push(next);
		}
	}

	/* cout << '\n';
	for (int s = 0; s < h; s++)
	{
		for (int t = 0; t < w; t++)
		{
			cout << dist[s][t];
		} cout << '\n';
	} */
}

void landing() {
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			if (map[i][j]) {
				memset(dist, -1, sizeof(dist));
				dimapping(i, j);
			}
		}
	}
}

int main() {
	cin >> h >> w;
	string mapr;
	for (int i = 0; i < h; i++)
	{
		cin >> mapr;
		char m;
		for (int j = 0; j < w; j++)
		{
			m = mapr[j];
			if (m == 'W') map[i][j] = 0;
			else if (m == 'L') map[i][j] = 1;
		}
	}

	landing();
	
	cout << max_dist;

	return 0;
}