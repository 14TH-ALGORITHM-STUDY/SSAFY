#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct Edge
{
	int num;
	int cost;
};

struct Path
{
	int from;
	int to;
};

//cost기준 오름차순 정렬
struct compare
{
	bool operator()(Edge a, Edge b)
	{
		return a.cost > b.cost;
	}
};

int N, E;
//반드시 거쳐야 하는 정점
int A, B;
vector<Edge> v[801];
int dist[801];
int ans1, ans2, ans;

void init()
{
	for (int i = 1; i <= N; i++)
	{
		dist[i] = 21e8;
	}
}

void input()
{
	cin >> N >> E;

	int from, to, cost;
	for (int i = 0; i < E; i++)
	{
		cin >> from >> to >> cost;
		//양방향 저장
		v[from].push_back({ to, cost });
		v[to].push_back({ from, cost });
	}

	//반드시 거쳐야 하는 두 정점
	cin >> A >> B;
}

void dijkstra(int st)
{
	priority_queue<Edge, vector<Edge>, compare> pq;
	pq.push({ st, 0 });
	dist[st] = 0;

	while (!pq.empty())
	{
		Edge now = pq.top();
		pq.pop();

		if (dist[now.num] < now.cost)
			continue;

		for (int i = 0; i < v[now.num].size(); i++)
		{
			int tar = v[now.num][i].num;
			int nextCost = v[now.num][i].cost + now.cost;

			if (dist[tar] > nextCost)
			{
				pq.push({ tar, nextCost });
				dist[tar] = nextCost;
			}
		}
	}
}

int cal_path(int start, int end)
{
	dijkstra(start);
	int temp = dist[end];

	init();

	if (temp < 21e8)
		return temp;

	else
		return 0;
}

int cal_path(vector<Path> paths)
{
	int result = 0;
	int distance;

	for (Path p : paths)
	{
		distance = cal_path(p.from, p.to);

		if (!distance)
			return -1;

		else
			result += cal_path(p.from, p.to);
	}
	return result;
}

void answer()
{
	if (ans1 == -1 && ans2 == -1)
		ans = -1;
	else if (ans1 != -1 && ans2 == -1)
		ans = ans1;
	else if (ans1 == -1 && ans2 != -1)
		ans = ans2;
	else
		ans = min(ans1, ans2);

	if (E == 1)
		ans = v[1][0].cost;
}

int main()
{
	freopen("input.txt", "r", stdin);
	input();
	init();

	vector<Path> p1 = { {1, A}, {A, B}, {B, N} };
	vector<Path> p2 = { {1, B}, {B, A}, {A, N} };

	ans1 = cal_path(p1);
	ans2 = cal_path(p2);

	answer();

	cout << ans << '\n';

	return 0;
}