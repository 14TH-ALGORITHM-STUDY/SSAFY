// 백준 1253 좋다 (모범 풀이)
#include <bits/stdc++.h>
using namespace std;

inline bool isGood(const vector<long long>& a, int i) {
    int l = 0, r = (int)a.size() - 1;
    const long long target = a[i];

    // 종료 조건: l와 r이 교차하기 전까지 투포인터 탐색
    while (l < r) {
        if (l == i) { ++l; continue; }
        if (r == i) { --r; continue; }

        // 두 수의 합을 이용한 판별
        const long long s = a[l] + a[r];
        if (s == target) return true;
        if (s < target)  ++l;
        else             --r;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 문제 도입부
    int N;
    cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // 기본 아이디어
    sort(a.begin(), a.end());

    int cnt = 0;
    for (int i = 0; i < N; ++i)
        if (isGood(a, i)) ++cnt;

    cout << cnt << '\n';
    return 0;
}
