#include <iostream>
using namespace std;

int N, M;
int infoScore[3];
int watchScore[3];
int ans = 0;

void dfs(int day, int prev, int sum) {
	if (day == N) {
		if (sum >= M) ans++;
		return;
	}

	for (int task = 0; task < 2; task++) {
		for (int place = 0; place < 3; place++) {
			int gain = (task == 0 ? infoScore[place] : watchScore[place]);

			if (prev == place) gain /= 2;

			dfs(day + 1, place, sum + gain);
		}
	}
}

int main() {
	cin >> N >> M;

	for (int i = 0; i < 3; i++) cin >> infoScore[i];
	for (int i = 0; i < 3; i++) cin >> watchScore[i];

	dfs(0, -1, 0);

	cout << ans << "\n";
	return 0;
}