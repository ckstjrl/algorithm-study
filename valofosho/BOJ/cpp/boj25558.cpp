#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	long long sx, sy, ex, ey;
	cin >> N >> sx >> sy >> ex >> ey;

	vector<long long> ls;
	ls.reserve(N);

	for (int i = 0; i < N; i++) {
		long long tsx = sx;
		long long tsy = sy;
		long long diff = 0;

		int K;
		cin >> K;

		for (int j = 0; j < K; j++) {
			long long cx, cy;
			cin >> cx >> cy;
			diff += abs(tsx - cx) + abs(tsy - cy);
			tsx = cx;
			tsy = cy;
		}
		diff += abs(tsx - ex) + abs(tsy - ey);
		ls.push_back(diff);
	}

	int idx = min_element(ls.begin(), ls.end()) - ls.begin();
	cout << idx + 1 << '\n';
	
	return 0;
}
