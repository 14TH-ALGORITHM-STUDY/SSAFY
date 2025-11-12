#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int INF = 1e9; // 무한대

int N, E;
vector<vector<pair<int, int>>> graph;

// 다익스트라 함수
vector<int> dijkstra(int start) {
    vector<int> dist(N + 1, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (dist[now] < cost) continue;

        for (auto& edge : graph[now]) {
            int next = edge.first;
            int nextCost = edge.second + cost;

            if (nextCost < dist[next]) {
                dist[next] = nextCost;
                pq.push({nextCost, next});
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> E;
    graph.assign(N + 1, vector<pair<int, int>>());

    for (int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c}); // 양방향
    }

    int v1, v2;
    cin >> v1 >> v2;

    // 다익스트라 3회 실행
    vector<int> dist1 = dijkstra(1);
    vector<int> distV1 = dijkstra(v1);
    vector<int> distV2 = dijkstra(v2);

    // 두 경로 계산
    long long path1 = (long long)dist1[v1] + distV1[v2] + distV2[N];
    long long path2 = (long long)dist1[v2] + distV2[v1] + distV1[N];

    long long result = min(path1, path2);

    if (result >= INF) cout << -1 << "\n";
    else cout << result << "\n";

    return 0;
}
