#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct edge {
	int point;
	int cost;
};

struct cmp {
	bool operator() (edge a, edge b) {
		return a.cost > b.cost;
	}
};

int n, e;
vector<vector<edge>> v;
int dist[801];

void dijkstra(int st) {
	priority_queue<edge, vector<edge>, cmp> pq;
	pq.push({ st, 0 });
	dist[st] = 0;

	while (!pq.empty()) {
		edge now = pq.top();
		pq.pop();

		if (dist[now.point] < now.cost) continue;
		
		for (int i = 0; i < v[now.point].size(); i++)
		{
			edge next = { v[now.point][i].point, v[now.point][i].cost + now.cost };
			
			if (next.cost < dist[next.point]) {
				dist[next.point] = next.cost;
				pq.push(next);
			}
		}
	}
}

void resetdist() {
	for (int i = 0; i <= n; i++)
	{
		dist[i] = 21e8;
	}
}

int main() {
	cin >> n >> e;
	v.resize(n + 1);
	int from, to, d;
	for (int i = 0; i < e; i++)
	{
		cin >> from >> to >> d;
		v[from].push_back({ to, d });
		v[to].push_back({ from, d });
	}


	int node[4] = { 1, 0, 0, n };
	cin >> node[1] >> node[2];
	
	int distance[2] = { 0 };
	for (int d = 0; d < 2; d++)
	{
		for (int i = 0; i < 3; i++)		// 시작점은 3개
		{	// 시작점은 i, 도착점은 i+1
			resetdist();
			dijkstra(node[i]);
			// cout << dist[node[i+1]] << " ";
			if (dist[node[i + 1]] == 21e8) {
				distance[d] = -1;
				break;
			}
			distance[d] += dist[node[i + 1]];
		}
		
		int swp = node[1];		// 어짜피 2번 반복하므로 한번만 적용
		node[1] = node[2];
		node[2] = swp;
	}
	if (distance[0] != -1 && distance[0] < distance[1]) cout << distance[0];
	else if (distance[1] != -1) cout << distance[1];
	else cout << -1;


/////////////////////////////////////
/* 개인 코멘트...
- v.resize(n+1); 보통 n번째 노드까지 사용하므로 n+1으로 사이즈 설정

 

처음엔 1번에서 V1, V2, N 까지 다익스트라를 3번 호출했는데, 형식이 동일하므로 21e8초기화 함수 빼고 for문안에 넣음

매번 dist가 21e8인지 확인하지 않으면 overflow발생, 매번 확인하면 너무 길어짐,,

 

* 반복문에서 일정한 규칙의 원소들이 줄지어 있을 때 배열에 넣는게 좋음 = node[4] 선언

 

- 이때 시작점이 3개이므로 도착점이 i+1으로 설정해야한다는 것

 

1트 후

V1 다음 V2가 아니라 그냥 지나기만 하는거라 순서가 상관없음을 깨달음

그렇다면 V1 -> V2 와 V2 -> V1 을 비교해서 최솟값을 찾으면 되는건가?

 

distance[2]으로 변경해서 최소한의 수정을 찾았음

 

node를 이차원 배열로 변경하기 귀찮았음..

그래서 어짜피 d가 2번이고 한번만 변경되므로, 첫번째 반복문이 끝날 때 swp 사용해서 V1과 V2을 변경

 

 

node 이차원 배열로 변경한다면?

    int node[2][4] = { 1, 0, 0, n, 1, 0, 0, n };
    cin >> node[0][1] >> node[0][2];
    node[1][1] = node[0][2];
    node[1][2] = node[0][1];

    int distance[2] = { 0 };
    for (int d = 0; d < 2; d++)
    {
        for (int i = 0; i < 3; i++)		// 시작점은 3개
        {	// 시작점은 i, 도착점은 i+1
            resetdist();
            dijkstra(node[d][i]);
            // cout << dist[node[i+1]] << " ";
            if (dist[node[d][i + 1]] == 21e8) {
                distance[d] = -1;
                break;
            }
            distance[d] += dist[node[d][i + 1]];
        }
    }
 

 

근데 포인트는 굳이 다익스트라 함수를 6번이나 호출할 필요가 있는가?

어짜피 양방향 노드이므로, V1에서 V2 최소 거리는 동일함

심지어 최소 거리만 알면 되므로 순서가 중요하지 않음

그렇다면, 다익스트라 3번만 호출해서 두가지 경우를 구할 수 있음

 

시작점 : 1, V1, V2

도착점 : V1, V2, N or V2, V1, N

 

    int distance[2] = { 0 };
    for (int i = 0; i < 3; i++)		// 시작점은 3개
    {
        resetdist();
        dijkstra(node[0][i]);
        for (int d = 0; d < 2; d++)
        {
            if (distance[d] == -1) continue;		// -1 이면 계산 X
            if (dist[node[d][i + 1]] == 21e8) distance[d] = -1;
            distance[d] += dist[node[d][i + 1]];
        }
    }
 

for가 불가피하지만, 다익스트라를 3번만 호출했다는데 의의..

 

대신에 이전 사용하던 break는 통하지 않음

한번 호출해서 더하는 과정이므로, 이전에 길이 없었다면 그냥 -1이도록 유지하는 수 밖에 없음

*/

	return 0;
}
