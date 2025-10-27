#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // 각 체커의 (x, y) 좌표 저장
    vector<pair<int, int>> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    // x 좌표와 y 좌표를 따로 저장
    vector<int> xs, ys;
    for (auto &a : arr) {
        xs.push_back(a.first);
        ys.push_back(a.second);
    }

    // 후보 좌표는 각 체커의 좌표들 중 하나이므로 중복 제거
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());

    // res[i]: i + 1 개의 체커를 한 칸에 모을 때 최소 이동 거리의 합
    vector<long long> res(N, LLONG_MAX);
    // 임시로 각 체커의 거리 저장
    vector<long long> dist;

    // 모든 후보 좌표 (X, Y) 에 대해 완전탐색
    for (auto X : xs) {
        for (auto Y : ys) {
            dist.clear();  // 임시 거리 배열 초기화

            // 각 체커에서 현재 후보 좌표 (X, Y)까지의 거리 계산
            for (auto &a : arr) {
                dist.push_back(abs(a.first - X) + abs(a.second - Y));
            }

            // 가까운 체커부터 정렬 -> k개를 모을 때 최소비용 계산
            sort(dist.begin(), dist.end());

            // 누적합으로 k개까지의 거리합 계산
            long long prefix = 0;
            for (int i = 0; i < N; i++) {
                prefix += dist[i];  // i번째 체커까지의 이동합
                res[i] = min(res[i], prefix);  // 최솟값 갱신
            }
        }
    }

    // 결과 출력
    for (int i = 0; i < N; i++) {
        cout << res[i] << ' ';
    }
    cout << '\n';

    return 0;
}