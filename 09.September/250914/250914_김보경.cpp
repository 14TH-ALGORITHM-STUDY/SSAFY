// 그 아이 친구들의 사탕도 모조리 뺏어버린다 -> ff
// 뺏은 아이의 개수가 k면 종료
// dfs + bfs(ff) -> 타임아웃 걱정

// 한명 사탕 뺏은 다음, 친구 탐색
// 친구 포함해서 사탕 뺏는 인원 k로 설정하기 어려워서
// k명 뽑은 다음에 사탕 계산할 때 판별하기로함

// 친구의 친구도 고려해야 됨 <- cur.size 말고 queue
// 대박 k명 이상!의 아이들이네요

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m, k;
vector<int> c;				// 아이들이 가지고 있는 사탕의 개수
vector<int> visited;
vector<vector<int>> f;				// 친구 정보
int stealn;
int s[30000];				// 뺏은 아이들 path
int svi[30000];
int stealcandy;
int before_stealcandy;
int max_stealcandy;

void stealing(int lev) {
	if (lev == k) {
		visited.resize(n, 0);
		stealn = 0;
		stealcandy = 0;

		int child;
		queue<int> q;
		for (int i = 0; i < k; i++)
		{
			child = s[i];
			if (visited[child]) continue;

			before_stealcandy = stealcandy;
			// 현재 아이가 친구가 몇명인지, 뺏어도 되는지 확인
			// if (stealn + child + f[child].size() >= k) continue;
			q.push(child);

			while (!q.empty()) {
				int node = q.front();
				q.pop();

				stealcandy += c[node];
				visited[node] = 1;
				stealn++;
				//if (stealn == k - 1) break;
				
				for (int j = 0; j < f[node].size(); j++)
				{
					int childf = f[node][j];
					if (visited[childf]) continue;
					
					q.push(childf);
				}

			}
			if (stealn >= k-1) break;
			// 만약 현재 k-2명이고, 이 뒤의 선택한 인원이 2명 이상이라면
			// 그땐 k-2명일때까지만 계산해야함
		}
		if (stealn >= k) stealcandy = before_stealcandy;
		if (stealcandy > max_stealcandy) max_stealcandy = stealcandy;
		
		return;
	}

	for (int i = 0; i < n; i++)
	{
		if (svi[i]) continue;
		s[lev] = i;
		svi[i] = 1;
		stealing(lev + 1);
		s[lev] = 0;
		svi[i] = 0;
	}
	
}

int main() {
	cin >> n >> m >> k;
	f.resize(n);

	int cand;
	for (int i = 0; i < n; i++)
	{
		cin >> cand;
		c.push_back(cand);
	}
	int from, to;
	for (int i = 0; i < m; i++)
	{
		cin >> from >> to;
		f[from - 1].push_back(to - 1);
		f[to - 1].push_back(from - 1);
	}

	stealing(0);
	
	cout << max_stealcandy;

	return 0;
}