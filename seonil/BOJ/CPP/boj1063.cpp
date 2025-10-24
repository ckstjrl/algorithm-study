/*
BOJ1063. 킹

[문제]
8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다.
체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다.
열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.
킹은 다음과 같이 움직일 수 있다.

* R : 한 칸 오른쪽으로
* L : 한 칸 왼쪽으로
* B : 한 칸 아래로
* T : 한 칸 위로
* RT : 오른쪽 위 대각선으로
* LT : 왼쪽 위 대각선으로
* RB : 오른쪽 아래 대각선으로
* LB : 왼쪽 아래 대각선으로

체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.
입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

[출력]
첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.
*/

#include <iostream>
#include <string>
#include <map>
using namespace std;

// 방향 매핑 (명령어 → dx, dy)
const map<string, pair<int, int>> directions = {
    {"R",  {1, 0}},
    {"L",  {-1, 0}},
    {"B",  {0, -1}},
    {"T",  {0, 1}},
    {"RT", {1, 1}},
    {"LT", {-1, 1}},
    {"RB", {1, -1}},
    {"LB", {-1, -1}}
};

// 체스 좌표 → 인덱스 좌표로 변환 (예: "A1" → (0,0))
pair<int, int> toIndex(const string& pos) {
    int x = pos[0] - 'A';
    int y = pos[1] - '1';
    return {x, y};
}

// 인덱스 좌표 → 체스 좌표로 변환 (예: (0,0) → "A1")
string toPosition(int x, int y) {
    string pos;
    pos += (char)('A' + x);
    pos += (char)('1' + y);
    return pos;
}

// 한 번의 이동 명령에 의한 킹의 이동 시뮬레이션을 수행하는 함수
void simulateKingMovement(string& kingPos, string& stonePos, const string& move) {

    // 현재 킹과 돌의 위치를 인덱스 좌표로 변환
    auto [kx, ky] = toIndex(kingPos);
    auto [sx, sy] = toIndex(stonePos);

    // 이동 벡터(dx, dy) 가져오기
    int dx = directions.at(move).first;
    int dy = directions.at(move).second;

    // 킹의 다음 위치 계산
    int nkx = kx + dx;
    int nky = ky + dy;

    // 킹이 체스판 밖으로 나가면 이동 무시(종료)
    if (nkx < 0 || nkx >= 8 || nky < 0 || nky >= 8) return;

    // 킹이 이동하려는 곳에 돌이 있는 경우,
    if (nkx == sx && nky == sy) {
        // 돌의 새로운 위치 계산(이동 방향으로 1칸 밀린다)
        int nsx = sx + dx;
        int nsy = sy + dy;

        // 돌이 밖으로 나가면 이동 불가
        if (nsx < 0 || nsx >= 8 || nsy < 0 || nsy >= 8) return;

        // 돌 이동
        sx = nsx;
        sy = nsy;
    }

    // 킹 이동
    kx = nkx;
    ky = nky;

    // 내부 인덱스 좌표를 다시 체스 좌표로 변환해 결과 반환
    kingPos = toPosition(kx, ky);
    stonePos = toPosition(sx, sy);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string king, stone;
    int N;
    cin >> king >> stone >> N;  // 킹의 위치 king, 돌의 위치 stone, 움직이는 횟수 N 입력 받기

    for (int i = 0; i < N; i++) {  // N번 동안,
        string move;
        cin >> move;  // 킹의 커맨드(이동 명령) 입력 받기
        simulateKingMovement(king, stone, move);  // 킹에 입력된 커맨드에 따른 이동 시뮬레이션 수행
    }

    cout << king << '\n' << stone << '\n';  // 시뮬레이션 종료 후 킹의 위치 king, 돌의 위치 stone 출력
    return 0;
}