#include <bits/stdc++.h>
#include <string>
#include <vector>

using namespace std;

void solve(int a, int b, int c, int d) 
{
	int y_diff;

	if (d < b) {
		cout << -1;
		return;
	}

	y_diff = d - b;

	if (a + y_diff < c) {
		cout << -1;
		return;
	}

	if (c >= a && d >= b) {
		cout << y_diff + (y_diff + a) - c;
		return;
	}

	cout << 2 * (d - b) + (a - c);
}


int main()
{
	int n;

	int a, b, c, d;

	cin >> n >> ws;

	for (int i = 0; i < n; i++) {
		cin >> a;
		cin >> b;
		cin >> c;
		cin >> d;
		
		solve(a, b, c, d);

		cout << "\n";
	}
	return 0;
}