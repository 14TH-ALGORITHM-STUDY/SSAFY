#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int cap[52][52];
int flow[52][52];		// 현재 물의 흐름
int visited[52];		// 방문여부 & 도착 지점 (경로 추적 가능)
int total_flow;


int findway(int from, int to) {		// BFS
	memset(visited, -1, sizeof(visited));	// -1으로 초기화

	queue<int> q;
	q.push(from);
	visited[from] = from;	// 시작점이므로

	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int i = 0; i < 52; i++)
		{
			if (cap[now][i] - flow[now][i] > 0 && visited[i] == -1) {
				q.push(i);
				visited[i] = now;
				if (i == to) break;	// 도착점이라면 종료
			}
			
		}
		if (visited[to] != -1) break;	// 도착점이라면 while도 종료
	}
	
	if (visited[to] == -1) {	// 'Z'에 도달하지 못했다면
		return 0;
	}

	// 'Z'에 도달했다면 : 유량 확인
	int path = 21e8;
	int v = 'Z'-'A';
	while (v != from) {
		int w = visited[v];
		path = min(path, cap[w][v] - flow[w][v]);

		v = visited[v];
	}
	
	v = to;
	while (v != from) {
		int w = visited[v];
		
		flow[w][v] += path;	// 정방향
		flow[v][w] -= path;	// 역방향

		v = visited[v];
	}

	return path;
}

int main() {
	ios::sync_with_stdio(false); // 속도 향상
	cin.tie(NULL);

	cin >> n;
	char fr, to;
	int fl;
	for (int i = 0; i < n; i++)
	{
		cin >> fr >> to >> fl;
		
		int u, v;
		if (fr >= 'A' && fr <= 'Z') u = fr - 'A';      // A-Z -> 0-25
		else u = fr - 'a' + 26;                         // a-z -> 26-51

		if (to >= 'A' && to <= 'Z') v = to - 'A';      // A-Z -> 0-25
		else v = to - 'a' + 26;                         // a-z -> 26-51

		cap[u][v] += fl;	// 여러개 파이프가 있을 수 있으므로
		cap[v][u] += fl;
	}

	while (1) {
		int path = findway(0, 'Z' - 'A');
		
		if (path == 0) {
			break;
		}
		
		total_flow += path;
	}
		
	cout << total_flow << '\n';

	return 0;
}
