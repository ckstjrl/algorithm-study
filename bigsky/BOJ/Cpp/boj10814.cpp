#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> age[201];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int a;
		string name;
		cin >> a >> name;
		age[a].push_back(name);
	}

	for (int i = 1; i < 200; i++) {
		for (int j = 0; j < age[i].size(); j++) {
			cout << i << ' ' << age[i][j] << '\n';
		}
	}

	return 0;
}