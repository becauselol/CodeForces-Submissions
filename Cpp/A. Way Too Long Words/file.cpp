#include <bits/stdc++.h>
#include <string.h>
using namespace std;
int main()
{
	string s;
	int n;
	cin >> n >> ws;
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (s.length() <= 10) {
    		cout << s;
    	} else {
    		cout << s[0];
    		cout << to_string(s.length() - 2);
    		cout << s[s.length() - 1];
    	}
    	cout << "\n";
	}
    	
	return 0;
}