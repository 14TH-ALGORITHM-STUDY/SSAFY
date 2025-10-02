#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Point
{
	int y;
	int x;
};

struct Edge
{
	Point p;
	int cost;
};

struct compare
{
	bool operator()(Edge a, Edge b)
	{
		//비용기준 오름차순
		return a.cost > b.cost;
	}
};

int N, M;
int MAP[101][101];
int dist[101][101];
//상, 하, 좌, 우
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

void input()
{
	cin >> M >> N;
	
	string line;
	for (int i = 1; i <= N; i++)
	{
		cin >> line;
		for (int j = 1; j <= M; j++)
		{
			MAP[i][j] = line[j - 1] - '0';
		}
	}
}

void init()
{
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
			dist[i][j] = 21e8;
}

void dijkstra(Point st)
{
	priority_queue<Edge, vector<Edge>, compare> pq;
	//(1, 1)은 항상 뚫려있으므로 0대입
	pq.push({ st, 0 });
	dist[st.y][st.x] = 0;

	while (!pq.empty())
	{
		Edge now = pq.top();
		pq.pop();

		if (dist[now.p.y][now.p.x] < now.cost)
			continue;

		for (int i = 0; i < 4; i++)
		{
			int ny = now.p.y + dy[i];
			int nx = now.p.x + dx[i];

			if (ny < 1 || nx < 1 || ny > N || nx > M)
				continue;

			int nextCost = now.cost + MAP[ny][nx];

			if (dist[ny][nx] > nextCost)
			{
				dist[ny][nx] = nextCost;
				pq.push({ {ny, nx}, nextCost });
			}
		}
	}

}

int main()
{
	//freopen("input.txt", "r", stdin);
	input();
	init();
	dijkstra({ 1,1 });
	cout << dist[N][M] << '\n';
	return 0;
}
