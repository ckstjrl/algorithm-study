#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int N, M;

void floyd(vector<vector<int>> &d) {
    for (int k = 1; k <= N; k++) {           // k번째 정점을 거쳐서
        for (int i = 1; i <= N; i++) {       // i에서
            for (int j = 1; j <= N; j++) {   // j로 가는 비용 구함.
                if (d[i][k] < INT_MAX && d[k][j] < INT_MAX) {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);  // k를 거치는게 더 작으면 최솟값 갱신
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    vector<vector<int>> dist(N + 1, vector<int>(N + 1, INT_MAX));  // 모든 정점으로의 거리 무한대로 초기화
    for (int i = 1; i <= N; i++) {
        dist[i][i] = 0;  // 자기자신까지의 거리 0으로 둠.
    }

    int a, b, c;
    while (M--) {
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);  // a-b 경로가 여러 개 있을 수 있으므로 최단거리만 넣음.
    }

    floyd(dist);  // 플로이드-워셜 알고리즘

    for (int i = 1; i <= N; i++) {  // dist가 INT_MAX 면 도달 불가, 아니면 최소 비용 출력
        for (int j = 1; j <= N; j++) {
            cout << (dist[i][j] == INT_MAX ? 0 : dist[i][j]) << (j == N ? '\n' : ' ');
        }
    }

    return 0;
}