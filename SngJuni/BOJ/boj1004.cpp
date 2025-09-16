#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int T;
    cin >> T;

    int x1, y1, x2, y2, n, cx, cy, r;
    while (T--) {
        int cnt = 0;  // 진입/이탈 횟수를 위한 변수
        cin >> x1 >> y1 >> x2 >> y2 >> n;
        for (int i = 0; i < n; i++) {
            cin >> cx >> cy >> r;

            // 행성계의 중점으로부터 출발점과 도착점 사이의 거리를 위한 변수
            int dx1 = cx - x1;
            int dy1 = cy - y1;
            int dx2 = cx - x2;
            int dy2 = cy - y2;

            if (pow(dx1, 2) + pow(dy1, 2) < pow(r, 2)) {      // 출발점은 행성계 안에 있고
                if (pow(dx2, 2) + pow(dy2, 2) > pow(r, 2)) {  // 도착점은 행성계 밖에 있는 경우
                    cnt++;
                }
            }
            if (pow(dx1, 2) + pow(dy1, 2) > pow(r, 2)) {      // 출발점은 행성계 밖에 있고
                if (pow(dx2, 2) + pow(dy2, 2) < pow(r, 2)) {  // 도착점은 행성계 안에 있는 경우
                    cnt++;
                }
            }
        }
        cout << cnt << '\n';  // 결과 출력
    }

    return 0;
}