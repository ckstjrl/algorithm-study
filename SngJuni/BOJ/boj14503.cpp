#include <iostream>
#include <vector>

using namespace std;

int N, M, r, c, d;
vector<vector<int>> room;

// 북(0), 동(1), 남(2), 서(3) 순의 방향 델타
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};


int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> N >> M;
    cin >> r >> c >> d;

    room.resize(N, vector<int>(M));  
    
    for (int i = 0; i < N; i++) {    // 방 좌표별 상태 저장
        for (int j = 0; j < M; j++) {
            cin >> room[i][j];
        }
    }

    int res = 0;

    while (true) {
        // 1. 현재 칸 청소
        if (room[r][c] == 0) {
            room[r][c] = 2;
            res++;
        }

        // 주변 4칸 탐색
        bool unclean = false;
        for (int i = 0; i < 4; i++) {
            int ny = r + dy[i];
            int nx = c + dx[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (room[ny][nx] == 0) {
                unclean = true;
                break;
            }
        }

        // 2. 청소되지 않은 빈 칸 없는 경우
        if (!unclean) {
            int backDir = (d + 2) % 4;  // 바라보는 방향 기준 후진 방향
            int by = r + dy[backDir];
            int bx = c + dx[backDir];

            if (room[by][bx] == 1) break;  // 바라보는 방향의 뒤쪽 칸이 벽이라면 후진 불가 -> 작동 중지
            // 후진하고 1번으로 돌아감.
            r = by;
            c = bx;
        }
        // 3. 청소되지 않은 빈 칸 있는 경우
        else {
            d = (d + 3) % 4;  // 반시계 방향 90도 회전
            int ny = r + dy[d];
            int nx = c + dx[d];

            if (room[ny][nx] == 0) {  // 바라보는 방향의 앞쪽 칸이 청소되지 않은 빈 칸인 경우 전진
                r = ny;
                c = nx;
            }
        }
    }
    cout << res << '\n';  // 결과 출력

    return 0;
}