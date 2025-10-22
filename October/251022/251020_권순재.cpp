#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>

using namespace std;

struct conveyor
{
    int durability;
    bool isRobot;
};

int N, K;
int step;
//Load Position(적재 위치)
//Unload Position(하역 위치)
int load_position, unload_position;
vector<conveyor> v;

//로봇 하역 함수
void unloadRobot()
{
    //하역 위치에 로봇이 존재한다면
    if (v[unload_position].isRobot)
        //로봇 하역
        v[unload_position].isRobot = false;
}

//로봇 적재 함수
void loadRobot()
{
    //적재 위치의 내구도가 0이 아니라면
    if (v[load_position].durability > 0)
    {
        //로봇 적재
        v[load_position].isRobot = true;

        //내구도 -1
        v[load_position].durability -= 1;

        //내구도가 0이 된다면
        if (v[load_position].durability == 0)
            K--;
    }
}

//로봇 이동 함수
void moveRobot()
{
    int idx_to, idx_from;

    for (int i = 1; i < N; i++)
    {
        idx_from = ((unload_position - i) % (2 * N) + (2 * N)) % (2 * N);
        idx_to = ((unload_position - i + 1) % (2 * N) + (2 * N)) % (2 * N);

        //움직일 로봇이 존재한다면
        if (v[idx_from].isRobot)
        {
            //이동하려는 위치에 로봇이 없으며, 내구성이 0이 아닐때
            if (!v[idx_to].isRobot && v[idx_to].durability > 0)
            {
                //로봇 1칸 이동
                v[idx_from].isRobot = false;
                v[idx_to].isRobot = true;

                //내구도 -1
                v[idx_to].durability -= 1;

                //내구도가 0이 된다면
                if (v[idx_to].durability == 0)
                    K--;
            }
        }
    }
}

//컨베이어 이동 함수
void moveConveyor()
{
    for (int i = 0; i < (2 * N); i++)
    {
        //Unload Position
        if ((i + step) % (2 * N) == (N - 1))
            unload_position = i;

        //Load Position
        if ((i + step) % (2 * N) == 0)
            load_position = i;
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);

    // 컨베이어 벨트 길이(N), 종료조건(K)
    cin >> N >> K;
    
    //컨베이어 벨트 내구성 정보
    int A;
    for (int i = 0; i < (2 * N); i++)
    {
        cin >> A;
        v.push_back({A, false});
    }

    // 내구도가 0인 칸의 개수가 K개가 될때까지
    while (K > 0)
    {    
        step++;

        moveConveyor();
        unloadRobot();

        moveRobot();
        unloadRobot();

        loadRobot();
    }

    cout << step << '\n';
    return 0;
}