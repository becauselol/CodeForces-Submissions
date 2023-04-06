#include <bits/stdc++.h>
#include <string>
#include <vector>

using namespace std;
int main()
{
	string s;
	string temp = "";

	int sum = 0;
	int arr[3];
	int dist;
	int max_coins;
	int shortage;
	int diff;
	int n;
	int slot = 0;
	char del = ' ';

	cin >> n >> ws;

	for (int i = 0; i < n; i++) {
		shortage = 0;
		for (int j = 0; j < 4; j++) {
			cin >> s;
			if (j < 3) {
				arr[j] = stoi(s);
			} else {
				dist = stoi(s);
			}
		}
		max_coins =  *max_element(arr, arr + 3);
		
		for (int j = 0; j < 3; j++) {
			diff = max_coins - arr[j];
			shortage = shortage + diff;
		}

		if (dist - shortage < 0) {
			cout << "NO";
		} else {
			dist = dist - shortage;
			if (dist % 3 == 0) {
				cout << "YES";
			} else {
				cout << "NO";
			}
		}
		cout << "\n";
	}
	return 0;
}