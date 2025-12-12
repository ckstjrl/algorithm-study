#include <iostream>

using namespace std;

int dfs(int n, int r, int c) {
    if (n == 0) {  // 더 이상 쪼갤 수 없는 칸일 때
        return 0;
    }

    int half = 1 << (n - 1);  // 현재 정사각형 한 변의 절반 길이 - 2^(n-1)
    int quadrant = 0;         // 0 - 좌상, 1 - 우상, 2 - 좌하, 3 - 우하

    if (r >= half) {     // 행이 아래쪽 절반에 있으면
        quadrant += 2;   // 2 또는 3번 사분면
        r -= half;       // 해당 사분면 내부 좌표로 이동
    }

    if (c >= half) {     // 열이 오른쪽 절반에 있으면
        quadrant += 1;   // 1 또는 3번 사분면
        c -= half;       // 해당 사분면 내부 좌표로 이동
    }

    // 해당 사분면 이전까지의 방문 개수 + 사분면 내부에서의 위치(재귀)
    return quadrant * half * half + dfs(n - 1, r, c);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, R, C;
    cin >> N >> R >> C;

    cout << dfs(N, R, C) << '\n';  // 결과 출력

    return 0;
}