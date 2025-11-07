#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct Bridge
{
    int a;
    int b;
    int cost;
};

struct Point
{
    int y, x;
};

bool compare(Bridge a, Bridge b)
{
    return a.cost < b.cost;
}

int N, M;
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };
int MAP1[10][10];
int MAP2[10][10];
int parent[7] = { 0, 1, 2, 3, 4, 5, 6 };
int assign = 1;
int ans = 0;
vector<Bridge> bridges;

void input()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> MAP1[i][j];
}

void numberInit(Point st)
{
    queue<Point> q;
    q.push(st);
    MAP2[st.y][st.x] = assign;

    while (!q.empty())
    {
        Point now = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            Point next = { now.y + dy[i], now.x + dx[i] };

            //배열의 범위를 벗어난다면
            if (next.y < 0 || next.x < 0 || next.y >= N || next.x >= M)
                continue;

            //바다라면
            if (!MAP1[next.y][next.x])
                continue;

            //이미 방문했다면
            if (MAP2[next.y][next.x])
                continue;

            q.push(next);
            MAP2[next.y][next.x] = assign;
        }
    }
}

//다리 찾기
void find_bridges()
{
    for (int i = 0; i < N; i++)
    {
        int dist = 0;
        int temp = -1;

        for (int j = 0; j < M; j++)
        {
            //섬을 처음 발견하였다면
            if (MAP2[i][j] && temp == -1)
                temp = MAP2[i][j];

            //다리 거리 계산
            if (!MAP2[i][j] && temp != -1)
                dist++;

            //같은 섬을 또 만났다면
            if (MAP2[i][j] == temp)
                dist = 0;

            //그 다음 섬을 발견하였다면
            if (MAP2[i][j] != temp && temp != -1 && MAP2[i][j])
            {
                if (dist > 1)
                    bridges.push_back({ temp, MAP2[i][j], dist });
                dist = 0;
                temp = MAP2[i][j];
            }
        }
    }

    for (int j = 0; j < M; j++)
    {
        int dist = 0;
        int temp = -1;

        for (int i = 0; i < N; i++)
        {
            //섬을 처음 발견하였다면
            if (MAP2[i][j] && temp == -1)
                temp = MAP2[i][j];

            //다리 거리 계산
            if (!MAP2[i][j] && temp != -1)
                dist++;

            //같은 섬을 또 만났다면
            if (MAP2[i][j] == temp)
                dist = 0;

            //그 다음 섬을 발견하였다면
            if (MAP2[i][j] != temp && temp != -1 && MAP2[i][j])
            {
                if (dist > 1)
                    bridges.push_back({ temp, MAP2[i][j], dist });
                dist = 0;
                temp = MAP2[i][j];
            }
        }
    }
}

int find(int tar)
{
    if (parent[tar] == tar)
        return tar;

    int ret = find(parent[tar]);
    parent[tar] = ret;
    return ret;
}

void setUnion(int a, int b)
{
    int t1 = find(a);
    int t2 = find(b);

    if (t1 == t2)
        return;

    parent[t2] = t1;
}

void kruskal()
{
    int a;
    int b;
    int cost;
    int selectCnt = 0;

    for (Bridge bridge : bridges)
    {
        a = bridge.a;
        b = bridge.b;
        cost = bridge.cost;

        if (find(a) == find(b))
            continue;

        setUnion(a, b);
        selectCnt++;
        ans += cost;

        if (selectCnt == assign - 2)
            return;
    }
    ans = -1;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    input();

    //섬 나누기
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (MAP1[i][j] && !MAP2[i][j])
            {
                numberInit({ i, j });
                assign++;
            }
        }
    }

    find_bridges();
    sort(bridges.begin(), bridges.end(), compare);

    kruskal();
    
    cout << ans << '\n';
    return 0;
}