#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0,0,-1, 1 };

struct mirror {
	int y, x;
	int cnt;
};

struct cmp {
	bool operator() (mirror a, mirror b) {
		return a.cnt > b.cnt;
	}
};

int m, n;
int map[100][100];
int dist[100][100];

void dijkstra(int sy, int sx) {
	priority_queue<mirror, vector<mirror>, cmp> pq;
	pq.push({ sy, sx, 0 });
	dist[sy][sx] = 0;

	while (!pq.empty()) {
		mirror now = pq.top();
		pq.pop();
		
		for (int d = 0; d < 4; d++)
		{
			int ny = now.y + dy[d];
			int nx = now.x + dx[d];
			if (nx < 0 || ny < 0 || ny >= n || nx >= m) continue;
			
			int ncnt = now.cnt;
			if (map[ny][nx] == 1) ncnt++;
			
			if (ncnt < dist[ny][nx]) {
				dist[ny][nx] = ncnt;
				pq.push({ ny, nx, ncnt });
			}
		}
	}
}

int main() {
	cin >> m >> n;
	for (int i = 0; i < n; i++)
	{
		string mapline;
		cin >> mapline;
		for (int j = 0; j < m; j++)
		{
			map[i][j] = mapline[j]-'0';
			dist[i][j] = 21e8;
		}
	}

	dijkstra(0, 0);
	
	cout << dist[n - 1][m - 1];

	return 0;
}
