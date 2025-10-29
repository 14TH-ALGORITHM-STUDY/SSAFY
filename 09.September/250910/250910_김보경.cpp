// 시간표처럼 배열에 넣는건 어떨까. 근데 n개를 최대 n번 탐색해야하므로 시간초과 예상
// 그러면 작은 순서대로 비교하는게 좋을것 같은데? pq
// 시작시간보다 끝나는 시간이 기준이므로 끝나는 순서로 정렬
// -> 빨리 끝나는 순으로 정렬, 시간을 합쳐서 끝나는 시간 업데이트 식
// 즉 pq 안에 들어있는게 강의실 개수

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct classes {
	int from;
	int to;
};

bool comparef(classes a, classes b) {
	if (a.from == b.from) return a.to < b.to;	// 동일 시작시간, 빠른 종료시간
	return a.from < b.from;
}

struct comparet {
	bool operator() (classes a, classes b) {
		return a.to > b.to;
	}
};

priority_queue<classes, vector<classes>, comparet> pq;

void findclass(int a, int b) {
	classes now = { a, b };		// 현재 수업

	if (pq.empty()) {
		pq.push(now);
		return;
	}

	classes early = pq.top();	// 시간표상 이전 수업
	if (early.to <= now.from) {
		//now.from = early.from;
		pq.pop();				// early 값 날리고 now로 다시 넣기 (업데이트)
		pq.push(now);
		
	}
	else	// 현재 수업 시작 시간이 이전수업시간보다 전일 경우
	{
		pq.push(now);
	}
}

int main() {
	int n;
	cin >> n;
	int st, et;
	vector<classes> time(n);
	for (int i = 0; i < n; i++)
	{
		cin >> time[i].from >> time[i].to;
	}

	sort(time.begin(), time.end(), comparef);	// 시작 시간 순으로 정렬

	for (int i = 0; i < n; i++)
	{
		findclass(time[i].from, time[i].to);
	}
	
	cout << pq.size();
	
}
