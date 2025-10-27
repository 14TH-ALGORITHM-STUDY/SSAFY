#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int N;
int ans;
//0 카운트
int zero_cnt;
int M[2000];
//임시저장 변수
int temp = 21e8;
//N 저장 벡터
vector<int> MAP;
//GOOD 조합 set자료형
set<int> s;

int main()
{
	freopen("input.txt", "r", stdin);

	cin >> N;

	int num;
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		M[i] = num;
		//0의 개수를 카운트
		if (num == 0)
		{
			zero_cnt++;
			continue;
		}

		MAP.push_back(num);
	}

	//MAP 오름차순 정렬
	sort(MAP.begin(), MAP.end());

	//0이 하나라도 존재한다면
	if (zero_cnt)
	{
		//오름차순 되었기에, 작은값부터 차례대로 꺼내게 된다.
		for (auto it = MAP.begin(); it != MAP.end(); it++)
		{
			//중복되는 값은 GOOD 조합에 넣는다.
			if (temp == *it)
				s.insert(*it);

			//중복되지 않는다면
			else
				//temp값 업데이트
				temp = *it;
		}
	}

	//0의 개수가 3개 이상이라면
	if (zero_cnt >= 3)
		s.insert(0);
	
	/* 0에 의한 방해요소 기본 세팅 완료 */
	//GOOD 조합 계산
	for (int i = 0; i < MAP.size(); i++)
		for (int j = i + 1; j < MAP.size(); j++)
			s.insert(MAP[i] + MAP[j]);

	//평가
	for (int i = 0; i < N; i++)
	{
		if (s.find(M[i]) != s.end())
			ans++;
	}

	cout << ans << '\n';

	return 0;
}