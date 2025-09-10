#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct course
{
    int S, T;
};

struct cmp
{
    bool operator()(course a, course b)
    {
        // 강의 종료시간 기준 오름차순 정렬
        // 즉, 강의 종료시간이 빠른순으로 꺼내진다.
        return a.T > b.T;
    }
};

bool compare(course a, course b)
{
    return a.S < b.S; //시작 시간 오름차순 정렬
}

int N;
int available_rooms;
int occupied_rooms;
priority_queue<course, vector<course>, cmp> pq;
vector<course> v;

int main()
{
    freopen("input.txt", "r", stdin);
    //강의실 개수 입력 받음
    cin >> N;

    //강의실 개수만큼 반복
    for (int i = 0; i < N; i++)
    {
        int S, T;
        cin >> S >> T;
        v.push_back({ S, T });
    }
    sort(v.begin(), v.end(), compare);

    for (int i = 0; i < v.size(); i++)
    {
        pq.push({ v[i].S, v[i].T });

        //사용가능한 강의실이 몇개인지 체크
        while (pq.top().T <= v[i].S)
        {
            pq.pop();
            //사용 가능한 방 +1
            available_rooms++;
            occupied_rooms--;
        }

        //사용 가능한 강의실이 존재한다면
        if (available_rooms)
        {
            available_rooms--;
            occupied_rooms++;
        }
        //사용 가능한 강의실이 존재하지 않는다면
        else
            //강의실 추가 배정
            occupied_rooms++;
    }
    cout << available_rooms + occupied_rooms << '\n';

    return 0;
}