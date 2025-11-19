#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M, a, b;
	cin >> N >> M;

	vector<int>v(N + 1);
	for (int i = 1; i <= N; i++) {
		cin >> v[i];
		v[i] += v[i - 1];
	}
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		cout << v[b] - v[a - 1] << '\n';
	}
	return 0;

}