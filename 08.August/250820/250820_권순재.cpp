//BAEKJOON 1074번 - Z
//r행 c열을 몇 번째로 방문하는가?
//1 ≤ N ≤ 15
//0 ≤ r, c < 2N
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
using namespace std;

struct Point
{
	int r, c;
};

Point target;
int N, r, c;
int ans;

void func(int lev, Point tar)
{
	if (lev == 0)
		return;

	Point quad = { tar.r / pow(2, lev - 1), tar.c / pow(2, lev - 1) };

	if (quad.r == 0 && quad.c == 0)
	{
		ans += 0;
	}

	if (quad.r == 0 && quad.c == 1)
	{
		ans += pow(2, lev - 1) * pow(2, lev - 1) * 1;
	}

	if (quad.r == 1 && quad.c == 0)
	{
		ans += pow(2, lev - 1) * pow(2, lev - 1) * 2;
	}

	if (quad.r == 1 && quad.c == 1)
	{
		ans += pow(2, lev - 1) * pow(2, lev - 1) * 3;
	}
	
	Point next_tar = { (tar.r % (int)pow(2, lev - 1)), (tar.c % (int)pow(2, lev - 1)) };
	
	func(lev - 1, next_tar);
}

int main()
{
	cin >> N >> r >> c;
	
	target = { r, c };
	
	func(N, target);

	cout << ans << '\n';

	return 0;
}
