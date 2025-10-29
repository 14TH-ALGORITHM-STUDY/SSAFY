#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

// 부모 노드
int parent[10];
// 각 사람의 생일을 나타내는 배열
int birthdays[10] = { 8, 2, 2, 8, 3, 3, 12, 12, 6, 8 };

int find(int tar)
{
    if (tar == parent[tar])
        return tar;

    return find(parent[tar]);
}

void setUnion(int a, int b)
{
    int t1 = find(a);
    int t2 = find(b);

    if (t1 == t2)
        return;

    parent[t2] = t1;
}

int main()
{
    // freopen("sample_input.txt", "r", stdin);
    for (int i = 0; i < 10; i++)
    {
        parent[i] = i;
    }

    // 생일이 같은 사람들끼리 집합을 만듭니다.
    for (int i = 0; i < 10; i++)
    {
        for (int j = i + 1; j < 10; j++)
        {
            if (birthdays[i] == birthdays[j])
            {
                setUnion(i, j);
            }
        }
    }

    // 각 사람이 어떤 집합에 속하는지 출력합니다.
    for (int i = 0; i < 10; i++)
    {
        cout << i << "는" << find(i) << "그룹에 속해있습니다.\n";
    }

    return 0;
}
