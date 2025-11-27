/*** 11404. 플로이드 ***/

// 거리를 저장할 2차원 벡터에 거리를 저장한다 (벡터의 초기값을 max로 설정)
// k를 거쳐 갈 때의 거리가 더 짧으면 갱신한다

#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector<vector<int>> dist(n, vector<int>(n, INT_MAX));

	for (int i = 0; i < n; i++) dist[i][i] = 0; // 자기자신은 0으로 저장

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		dist[a - 1][b - 1] = min(dist[a-1][b-1], c); // 같은 위치에 여러 거리가 들어올 수 있으므로 최소값 선택
	}

	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			if (dist[i][k] == INT_MAX) continue; // max값이면 가지치기
			for (int j = 0; j < n; j++) {
				if (dist[k][j] == INT_MAX) continue; // max값이면 가지치기
				if (dist[i][j] > dist[i][k] + dist[k][j]) dist[i][j] = dist[i][k] + dist[k][j]; // k를 경유한 거리가 기존 저장된 거리보다 짧으면 갱신
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << (dist[i][j] == INT_MAX ? 0 : dist[i][j]) << ' '; // 거리가 max값이면 0 출력, 아니면 거리 출력
		}
		cout << '\n';
	}

	return 0;
}