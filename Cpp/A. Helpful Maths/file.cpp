#include <bits/stdc++.h>
#include <string>
#include <vector>

using namespace std;
int main()
{
	string s;

	cin >> s;

	vector<int> vect;
	char sep = '+';

	for (int i = 0; i < s.length(); i++) {
		if (s[i] != sep) {
			vect.push_back(int(s[i]-'0'));
		}	
	}

	sort(vect.begin(), vect.end());

    for (int i = 0; i < vect.size(); i++) {
    	if (i == 0) {
    		cout << vect[i];
    	} else {
    		cout << sep << vect[i];
    	}
    }
	return 0;
}