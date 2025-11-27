#include <iostream>
#include <unordered_set>
#include <string>
#include <algorithm>

using namespace std;

string result[500000];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M;
	cin >> N >> M;

	unordered_set<string> hashSet;

	for (int i = 0; i < N; i++) {
		string name;
		cin >> name;
		hashSet.insert(name);
	}

	int cnt = 0;

	for (int i = 0; i < M; i++) {
		string name;
		cin >> name;
		if (hashSet.count(name)) {
			result[cnt++] = name;
		}
	}

	sort(result, result + cnt);
	cout << cnt << '\n';
	for (int i = 0; i < cnt; i++) {
		cout << result[i] << '\n';
	}

	return 0;
}