/*** 11403. 경로 찾기 ***/

#include<iostream>
#include<vector>
#include<climits>
using namespace std;

vector<vector<int>> dist;

int main() {
	int N;
	cin >> N;

	dist.assign(N, vector<int>(N));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> dist[i][j];
			if (i != j && dist[i][j] == 0) dist[i][j] = INT_MAX;
		}
	}

	for (int k = 0; k < N; k++) { // 중간 경유지
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (dist[i][k] == 1 && dist[k][j] == 1) dist[i][j] = 1; // 중간 경유지를 거쳐 i에서 j로 갈 수 있으면 1 저장
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (dist[i][j] == INT_MAX) cout << 0 << ' ';
			else cout << dist[i][j] << ' ';
		}
		cout << '\n';
	}

	return 0;
}