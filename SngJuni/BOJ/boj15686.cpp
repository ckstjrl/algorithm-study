// dist 미리 다 계산해두고 선택된 치킨집 조합으로 합산하는 방식
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, M, res = INT_MAX;
vector<pair<int, int>> home;
vector<vector<int>> dist;
vector<pair<int, int>> chicken;
vector<bool> used;  // 선택된 치킨집 표시

int calc_dist() {
    int cur_dist = 0;

    for (int i = 0; i < home.size(); i++) {
        int temp = INT_MAX;
        for (int j = 0; j < chicken.size(); j++) {
            if (used[j]) {  // 선택된 치킨집과 각 집과의 최소 거리
                temp = min(temp, dist[i][j]);
            }
        }
        cur_dist += temp;
    }
    
    return cur_dist;  // 치킨 거리 반환
}

void dfs(int start, int depth) {
    if (depth == M) {  // M개 선택되면 거리 계산하고 최솟값 갱신
        res = min(res, calc_dist());
        return;
    }

    for (int i = start; i < chicken.size(); i++) {  // 조합으로 치킨집 선택
        if (!used[i]) {
            used[i] = true;
            dfs(i + 1, depth + 1);
            used[i] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    int x;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> x;

            if (x == 1) {
                home.push_back({i, j});     // 집의 좌표
            } else if (x == 2) {
                chicken.push_back({i, j});  // 치킨집의 좌표
            }
        }
    }

    used.assign(chicken.size(), false);
    dist.assign(home.size(), vector<int>(chicken.size()));

    // 각 집에서 각 치킨집까지의 거리
    for (int i = 0; i < home.size(); i++) {
        for (int j = 0; j < chicken.size(); j++) {
            dist[i][j] = abs(home[i].first - chicken[j].first) + abs(home[i].second - chicken[j].second);
        }
    }

    dfs(0, 0);

    cout << res << '\n';

    return 0;
}

// -------------------------------------------------------------------------------------------------------
// 집별 최소 거리를 dfs 중에 갱신
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, M, res = INT_MAX;
vector<pair<int, int>> home;
vector<pair<int, int>> chicken;
vector<int> dist1;  // 집마다 현재까지 선택된 치킨집들 중 최소 거리

void dfs(int start, int depth) {
    if (depth == M) {  // M개 선택되면
        int cur_sum = 0;
        for (int i : dist1) {  // 각 최소 거리 합산
            cur_sum += i;
        }
        res = min(res, cur_sum);  // 최솟값 갱신
        return;
    }

    for (int i = start; i < chicken.size(); i++) {
        vector<int> dist_cp = dist1;  // 현재까지 최소 거리 배열 따로 저장

        int ci = chicken[i].first;
        int cj = chicken[i].second;
        for (int j = 0; j < home.size(); j++) {
            int temp = abs(home[j].first - ci) + abs(home[j].second - cj);
            dist1[j] = min(dist1[j], temp);  // 지금 선택된 치킨집이 더 가까우면 갱신
        }

        dfs(i + 1, depth + 1);

        dist1.swap(dist_cp);  // 최소 거리 다시 되돌리기 (백트래킹)
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    int x;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> x;

            if (x == 1) {
                home.push_back({i, j});     // 집의 좌표
            } else if (x == 2) {
                chicken.push_back({i, j});  // 치킨집의 좌표
            }
        }
    }

    dist1.assign(home.size(), INT_MAX);
    dfs(0, 0);

    cout << res << '\n';

    return 0;
}