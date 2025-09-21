/*
도시 분할 계획
마을(N개의 집, M개의 길(양방향), 유지비)
임의의 두 집 사이에 경로가 항상 존재한다. (항상 이어져있다.)
목적 : 마을을 두 개의 분리된 마을로 분할(마을이 너무 크다)
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되야함
마을에는 집이 하나 이상 있어야 한다.
분리된 두 마을 사이에 있는 길들은 필요 없다.
분리된 마을도 MST를 만족하면 된다.
길의 유지비의 합을 최소로 하고 싶다.

아이디어 : parent 배열에서 집합이 2개가 형성될때 STOP
즉, parent 배열에서 집합이 2개가 되었다는걸 감지할 함수를 생성
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge
{
	int a;
	int b;
	int cost;
};

bool compare(Edge a, Edge b)
{
	//비용 기준 오름차순 정렬
	return a.cost < b.cost;
}

int N, M;
int ans;
vector<Edge> v;
int parent[100005];

void init()
{
	//부모 배열 초기화
	for (int i = 1; i <= N; i++)
		parent[i] = i;

	//ans 초기화
	ans = 0;
}

void input()
{
	//마을의 개수, 길의 개수 입력
	cin >> N >> M;

	//길 정보 입력
	int a, b, cost;
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b >> cost;
		v.push_back({ a, b, cost });
	}
}

int find(int tar)
{
	//자기 자신이 대표라면
	if (parent[tar] == tar)
		return tar;

	//경로 압축
	int ret = find(parent[tar]);
	parent[tar] = ret;
	return ret;
}

void setUnion(int a, int b)
{
	int r1 = find(a);
	int r2 = find(b);
	
	//이미 같은 집합에 속해있다면
	if (r1 == r2)
		return;

	//대표끼리 연결한다.
	parent[r2] = r1;
}

void kruskal()
{
	int cnt = 0;

	//v벡터를 순회
	for (Edge sel : v)
	{
		int a = sel.a;
		int b = sel.b;
		int cost = sel.cost;
		//이미 집합 관계라면
		if (find(a) == find(b))
			continue;
		//집합 관계 아니라면, 연결
		setUnion(a, b);
		cnt++;
		//ans에 비용 누적
		ans += cost;
		if (cnt == N - 1)
		{
			ans -= cost;
			break;
		}
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);
	input();
	init();
	//cost를 오름차순으로 정렬한다.
	sort(v.begin(), v.end(), compare);
	kruskal();
	cout << ans << '\n';
	return 0;
}