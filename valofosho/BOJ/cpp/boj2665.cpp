/*
BOJ2665 - 미로만들기
n^2의 바둑판 배열
배열은 검은 방과 흰 방으로 이루어짐
검은 방은 사면이 벽으로 막혀있어 못들어감
흰방끼리는 이동 가능
(0,0)을 시작점, (n-1, n-1)을 도착점이라고 했을 때
두 방은 모두 기본 흰방
시작점에서 도착점까지 가는데 최소 몇 개의 검은방을 흰 방으로 만들어야 갈 수 있는가

로직 정의
1. 0-1 BFS 풀면 되는 문제
    -> 각 방을 바꾸었을 때 방이 되돌아가는 로직은 없으니까
    -> 각 방을 지나는데 값이 든다고 생각하면 0-1 BFS 문제로 풀 수 있음
구현 순서
1. 우선순위 큐 선언
2. 시작점부터 갈 수 있는 정점들을 우선순위 큐에 넣기
3. w가 작은 순서부터 하나씩 뽑기
4. 갈 수 있는 조건들이면 그대로 진행

알아둬야 할 문법
1. priority queue 선언하기
    - 내림차순(기본)
        priority_queue<
        pair<int, pair<int, int>>,
        vector<pair<int, pair<int, int>>>,
        less<pair<int, pair<int, int>>
        >
    - 오름차순(선언)
        priority_queue<
        pair<int, pair<int, int>>,
        vector<pair<int, pair<int, int>>>,
        greater<pair<int, pair<int, int>>
        >
    우선순위 큐(BFS용) > maps > visited벡터 요렇게 3개 필요
    */

#include <iostream>
#include <vector>
#include <deque>
#include <string>

using namespace std;
using ll = long long;
const ll INF = 1e18;


int n;
vector<vector<int>> maps;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    
    deque<pair<int, int>> dq;
    
    vector<vector<ll>> dist(n, vector<ll>(n, INF));
    maps.assign(n, vector<int> (n));
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            char c = s[j];
            // 문제 안읽고 흰 방을 0인줄 알았...
            if(c=='1'){
                maps[i][j] = 0;    
            }
            else{
                maps[i][j] = 1;
            }
        }
    }
    dq.push_back({0,0});
    dist[0][0] = 0;
    // pq 비어질 때 까지 진행
    while (!dq.empty()){
        // cur 값 하나 빼기
        auto [i, j] = dq.front();
        dq.pop_front();
        // 우선 4방향 찾기
        const vector<pair<int, int>> dir = {
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
        };
        for (auto [di, dj] : dir){
            int ni = i + di;
            int nj = j + dj;
            // 방문 조건 정리
            //1. 갈 수 없는 땅
            if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
            // 가봤든 안가봤든 더 작으면 갱신 후 pq넣기
            ll nw = dist[i][j] + maps[ni][nj];
            if (dist[ni][nj] > nw){
                dist[ni][nj] = nw;
                if (maps[ni][nj] == 0){
                dq.push_front({ni, nj});
                }
                else{
                    dq.push_back({ni, nj});
                }
            }

        }
        
        }
        cout << dist[n-1][n-1] << '\n';
        return 0;

    }