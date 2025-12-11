/*
BOJ1197 - 최소 스패닝 트리
문제 정의
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하라
최소 스패닝 트리는 모든 정점을 연결하는 부분 그래프 중에서 가중치의 합이 최소인 트리

정점  V와 간선 E가 주어지고 다음 E개의 줄에는 A와 B가 C의 가중치로 이어져 있다는 정보
최소 스패닝 트리의 가중치는 int 안넘음

로직 정의
1. 문제 말대로 최소 스패닝 트리를 구하는 문제
2. 프림 알고리즘을 활용하여 풀이
3. 기존의 2차원 배열 형식으로는 메모리 초과가 발생
    -> 우선순위큐 + 프림 형식으로 변환

*/


#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int v, e;

vector<vector<pair<int, int>>> adj;
vector<int> visited;

int prim(int start){
    int ans = 0;
    int cnt = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> pq;
    pq.push({0, start});

    while(!pq.empty() && cnt < v){
        auto [w, u] = pq.top();
        pq.pop();

        if(visited[u]) continue;
        visited[u] = 1;
        ans += w;
        cnt ++;

        for (int i = 0; i < adj[u].size(); i++) {
            int nv = adj[u][i].first;
            int nw = adj[u][i].second;

            if (!visited[nv]) {
                pq.push({nw, nv});
            }
        }

    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> v >> e;
    adj.assign(v+1, {});
    visited.assign(v+1, 0);

    int a, b, c;
    for(int i = 0; i < e; i++){
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        adj[b].push_back({a,c});
    }
    int answer = prim(1);

    cout << answer;
    
    return 0;
}

// 원래 1번 풀이 - 실패 (메모리 초과-> 2차원 배열 형식에서 터짐)
// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int v, e;
// const int INF = 1e9;

// vector<vector<int>> cost;
// vector<int> dist;
// vector<int> visited;

// int prim(int start){
//     int ans = 0;
//     dist[start] = 0;

//     for(int i = 1; i <= v; i++){
//         int idx = -1;
//         int mincost = INF;

//         for(int j = 1; j <= v; j++){
//             if (!visited[j] && dist[j] < mincost){
//                 mincost = dist[j];
//                 idx = j;
//             }
//         }
//         visited[idx] = 1;
//         ans += mincost;

//         for (int j = 1; j <= v; j++){
//             if(!visited[j] && cost[idx][j] < dist[j]){
//                 dist[j] = cost[idx][j];
//             }
//         }

//     }

//     return ans;
// }

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     cin >> v >> e;
//     cost.assign(v+1, vector<int>(v+1, INF));
//     visited.assign(v+1, 0);
//     dist.assign(v+1, INF);
    
//     int a, b, c;
//     for (int i = 0; i < e; i++ ){
//         cin >> a >> b >> c;
//         cost[a][b] = c;
//         cost[b][a] = c;
//     }
//     int answer = INF;
//     answer = prim(1);

//     cout << answer;



//     return 0;
// }