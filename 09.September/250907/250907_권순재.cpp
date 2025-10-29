/*
백준 2589번
보물섬
지도 : NXM (50이하)
육지(L) / 바다(W)
이동 : 상하좌우
1칸 이동시 1시간 소요
보물 : 최단거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안된다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct Point
{
	int y, x;
};

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

int N, M;
char MAP[55][55];
int visited[55][55];
int ans;
vector<Point> v;

void bfs(Point st)
{
	queue<Point> q;
	visited[st.y][st.x] = 1;
	q.push(st);

	while (!q.empty())
	{
		Point now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			Point next = { now.y + dy[i], now.x + dx[i] };

			//Out of Index
			if (next.y < 0 || next.x < 0 || next.y >= N || next.x >= M)
				continue;

			//바다라면
			if (MAP[next.y][next.x] == 'W')
				continue;

			//이미 방문했다면
			if (visited[next.y][next.x])
				continue;

			visited[next.y][next.x] = visited[now.y][now.x] + 1;
			q.push(next);

			ans = max(ans, visited[next.y][next.x]);
		}
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);

	cin >> N >> M;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
		{
			cin >> MAP[i][j];

			//육지라면
			if (MAP[i][j] == 'L')
				v.push_back({ i, j });
		}

	for (int i = 0; i < v.size(); i++)
	{
		Point st = { v[i].y, v[i].x };

		bfs(st);

		memset(visited, 0, sizeof(visited));
	}

	cout << ans - 1 << '\n';

    return 0;
}