#include <iostream>
#include <vector>

using namespace std;

int n, m, res;
vector<vector<int>> arr;
vector<vector<pair<int, int>>> delta = {  // 각 모양별 델타 배열
    // ㅡ, ㅣ
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},

    // ㅁ
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}},

    // L
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {-1, 2}},
    {{0, 0}, {1, 0}, {2, 0}, {2, -1}},
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},
    {{0, 0}, {0, -1}, {0, -2}, {-1, -2}},
    {{0, 0}, {0, -1}, {0, -2}, {1, -2}},
    {{0, 0}, {-1, 0}, {-2, 0}, {-2, -1}},
    {{0, 0}, {-1, 0}, {-2, 0}, {-2, 1}},

    // z
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {-1, 1}, {-1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}}, 
    {{0, 0}, {1, 0}, {1, -1}, {2, -1}},

    // ㅗ
    {{0, 0}, {0, -1}, {0, 1}, {-1, 0}},
    {{0, 0}, {-1, 0}, {1, 0}, {0, -1}},
    {{0, 0}, {0, -1}, {0, 1}, {1, 0}},
    {{0, 0}, {-1, 0}, {1, 0}, {0, 1}},
};

void check(int i, int j) {
    for (auto& k : delta) {
        int sum = 0;  // 해당 모양별 칸의 합
        int cnt = 0;  // 몇 칸의 합인지 세기 위한 변수

        for (int l = 0; l < 4; l++) {  // 델타 배열 순회
            int nx = i + k[l].first;
            int ny = j + k[l].second;

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;  // 범위 벗어나면 합산 X
            sum += arr[nx][ny];
            cnt++;
        }
        if (cnt == 4) res = max(res, sum);  // 4칸의 합산일 경우에만 최댓값 갱신
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> n >> m;
    arr.assign(n, vector<int>(m, 0));  // 2차원 배열 0으로 초기화

    for (int i = 0; i < n; i++) {      // 칸에 쓰여있는 수 입력 받기
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < n; i++) {     // i, j 순회하면서 모든 모양 검사를 위한 check 함수 호출
        for (int j = 0; j < m; j++) {
            check(i, j);
        }
    }

    cout << res << '\n';

    return 0;
}