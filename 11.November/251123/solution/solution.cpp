#include <iostream>
#include <vector>

using namespace std;

// 전역 변수로 선언하거나 main 내부에 선언할 수 있습니다.
// 최대 입력값이 10000이므로 크기를 10001로 잡습니다.
int dp[10001];

int main() {
    // C++의 입출력 속도를 높이기 위한 설정 (백준 등 알고리즘 문제 풀이 시 필수)
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 1. dp[i] = 1로 초기화 (1만 사용하는 경우)
    for (int i = 0; i <= 10000; ++i) {
        dp[i] = 1;
    }

    // 2. 2를 사용하는 경우 추가
    // Python: for i in range(2, 10001): dp[i] += dp[i-2]
    for (int i = 2; i <= 10000; ++i) {
        dp[i] += dp[i - 2];
    }

    // 3. 3을 사용하는 경우 추가
    // Python: for i in range(3, 10001): dp[i] += dp[i-3]
    for (int i = 3; i <= 10000; ++i) {
        dp[i] += dp[i - 3];
    }

    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;
        // 줄바꿈은 endl 보다 "\n"이 빠릅니다.
        cout << dp[n] << "\n";
    }

    return 0;
}