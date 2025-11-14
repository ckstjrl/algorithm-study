#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, H, sy, sx, res;
vector<pair<int, int>> milk;  // 민트초코우유 좌표
vector<bool> visited;         // 민트초코우유 방문배열

void dfs(int si, int sj, int health, int cnt) {
    int home = abs(si - sy) + abs(sj - sx);  // 현재 위치에서 집까지의 거리

    if (health >= home) {  // 집으로 돌아갈 수 있다면 res 값 갱신
        res = max(res, cnt);
    }

    for (int i = 0; i < milk.size(); i++) {  // 민트초코우유 좌표 순회하면서
        int cur = abs(si - milk[i].first) + abs(sj - milk[i].second);  // 현재 위치에서 해당 민트초코우유까지의 거리

        if (!visited[i] && health >= cur) {  // 아직 방문하지 않았고 민트초코우유까지 갈 수 있는 체력이 있다면
            visited[i] = true;
            dfs(milk[i].first, milk[i].second, health - cur + H, cnt + 1);  // 다음 민트초코우유로 이동
            visited[i] = false;  // 백트래킹
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> H;

    int x;
    sy = -1, sx = -1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> x;

            if (x == 1) {  
                sy = i, sx = j;          // 진우 집 좌표
            }
            else if (x == 2) {
                milk.push_back({i, j});  // 민트초코우유 좌표
            }
        }
    }

    visited.assign(milk.size(), false);  // 방문배열 초기화

    dfs(sy, sx, M, 0);  // dfs 탐색
    
    cout << res << '\n';  // 결과 출력

    return 0;
}