#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    vector<long long> dp(10001, 1); // dp[i] = 1로 초기화

    // 2를 사용하는 경우 추가
    for (int i = 2; i <= 10000; i++) {
        dp[i] += dp[i - 2];
    }

    // 3을 사용하는 경우 추가
    for (int i = 3; i <= 10000; i++) {
        dp[i] += dp[i - 3];
    }

    while (T--) {
        int n;
        cin >> n;
        cout << dp[n] << "\n";
    }

    return 0;
}
