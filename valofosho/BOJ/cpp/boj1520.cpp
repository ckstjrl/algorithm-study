/*
BOJ1520 - 내리막길

문제 정의
1. 각 칸에는 해당 지점의 높이가 적힘, 이동은 상하좌우만 허용
2. 좌측상단 -> 우측 하단이 이동 방향
3. 내리막길로만 이동해서 우측 하단에 도착하는 경로의 개수를 구하라

로직 생각
1번 BFS
-> 우선순위 큐를 활용해서 높이를 maxheap으로 구현
-> 위에서부터 가장 높은 지점들을 방문하면서 다음 지점을 이동할 수 있다.
2번 DFS + DP
*/

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int n, m;

vector<vector<int>> maps;
vector<vector<int>> visited;

// 방향 벡터 생성
const vector<pair<int, int>> dir = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}
};

//maxheap 우선순위 큐 선언
priority_queue<
tuple<int, int, int>,
vector<tuple<int ,int, int>>
> pq;



void bfs(){
    while (!pq.empty()){
        auto [h, x, y] = pq.top();
        pq.pop();
        // 이젠 외우자 자동으로 하나씩 매칭
        for (auto[dx, dy]:dir){
            int nx = x+dx;
            int ny = y+dy;
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] >= maps[x][y]) continue;
            
            if (!visited[nx][ny]){
                pq.push({maps[nx][ny], nx, ny});
            }

            visited[nx][ny] += visited[x][y];
        }
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    // 배열들 크기 재지정
    maps.assign(n, vector<int> (m));
    visited.assign(n, vector<int> (m));
    
    // maps 배열 입력받기
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> maps[i][j];
        }
    }
    
    // 시작점 방문처리 + 넣어주기
    visited[0][0] = 1;
    pq.push({maps[0][0], 0, 0});
    
    bfs();
    cout << visited[n-1][m-1];
    
    return 0;
}