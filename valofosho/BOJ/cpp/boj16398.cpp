#include <iostream>
#include <vector>

using namespace std;
using ll = long long; // 롱롱 줄이기
const long long INF = 1e18; // INF 선언


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); // 입력 빠르게
    int N;
    // 입력 받기
    cin >> N;
    vector<vector<ll>> cost(N + 1, vector<ll>(N + 1));
    // 2차원 배열 입력받기!
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            cin >> cost[i][j];
            if (i==j) {
                cost[i][j] = INF;
            }
        }
    }
    
    vector<ll> dist(N+1, INF); // 거리 갱신용 벡터 INF로 초기화
    vector<int> visited(N+1, 0); // visited 벡터 0으로 초기화
    ll mst_cost = 0;

    dist[1] = 0; // 1번 정점부터 시작

    for (int i = 1; i <= N; i++){
        int u = -1; // 추가할 정점 후보
        ll best = INF;

        for (int j = 1; j<=N; j++){
            // 미방문, 거리가 더 적으면 방문처리
            if (!visited[j] && dist[j] < best){
                best = dist[j];
                u = j;
            }
        }

        visited[u] = 1;
        mst_cost += dist[u];

        for (int v = 1; v <= N; v++){
            // 미방문, 거리 짧으면 갱신
            if (!visited[v] && cost[u][v] < dist[v]){
                dist[v] = cost[u][v];
            } 
        }
    }
    cout << mst_cost << '\n';

}