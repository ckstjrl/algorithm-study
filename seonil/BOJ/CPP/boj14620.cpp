/*
BOJ14620. 꽃길

[문제]
2017년 4월 5일 식목일을 맞이한 진아는 나무를 심는 대신 하이테크관 앞 화단에 꽃을 심어 등교할 때 마다 꽃길을 걷고 싶었다.
진아가 가진 꽃의 씨앗은 꽃을 심고나면 정확히 1년후에 꽃이 피므로 진아는 다음해 식목일 부터 꽃길을 걸을 수 있다.
하지만 진아에게는 꽃의 씨앗이 세개밖에 없었으므로 세 개의 꽃이 하나도 죽지 않고 1년후에 꽃잎이 만개하길 원한다.
꽃밭은 N*N의 격자 모양이고 진아는 씨앗을 (1,1)~(N,N)의 지점 중 한곳에 심을 수 있다. 꽃의 씨앗은 그림 (a)처럼 심어지며 1년 후 꽃이 피면 그림 (b)모양이 된다.

꽃을 심을 때는 주의할 점이있다. 어떤 씨앗이 꽃이 핀 뒤 다른 꽃잎(혹은 꽃술)과 닿게 될 경우 두 꽃 모두 죽어버린다. 또 화단 밖으로 꽃잎이 나가게 된다면 그 꽃은 죽어버리고 만다.
그림(c)는 세 꽃이 정상적으로 핀 모양이고 그림(d)는 두 꽃이 죽어버린 모양이다.

하이테크 앞 화단의 대여 가격은 격자의 한 점마다 다르기 때문에 진아는 서로 다른 세 씨앗을 모두 꽃이 피게하면서 가장 싼 가격에 화단을 대여하고 싶다.
단 화단을 대여할 때는 꽃잎이 핀 모양을 기준으로 대여를 해야하므로 꽃 하나당 5평의 땅을 대여해야만 한다.
돈이 많지 않은 진아를 위하여 진아가 꽃을 심기 위해 필요한 최소비용을 구해주자!

[입력]
입력의 첫째 줄에 화단의 한 변의 길이 N(6≤N≤10)이 들어온다.
이후 N개의 줄에 N개씩 화단의 지점당 가격(0≤G≤200)이 주어진다.

[출력]
꽃을 심기 위한 최소 비용을 출력한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N;
vector<vector<int>> flowerbed; // flowerbed = 2차원 동적 배열
vector<vector<bool>> visited; // visited = 2차원 동적 배열

// 상하좌우 델타 벡터
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

// (x, y)에 꽃을 심을 때 드는 비용 계산
// 꽃은 중앙과 상하좌우 4칸을 차지하므로 총 5칸 비용을 합산
int flowerCost(int x, int y) {
    int sum = flowerbed[x][y];  // 중앙 비용
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        sum += flowerbed[nx][ny]; // 상하좌우 비용 더하기
    }
    return sum; // 결과값 반환
}

// (x, y)에 꽃을 심을 수 있는지 확인
// 중앙과 주변 4칸이 모두 비어 있으면 True, 아니면 False 반환
bool canPlant(int x, int y) {
    if (visited[x][y]) return false; // (x, y)에 꽃이 있다면 False
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (visited[nx][ny]) return false; // 주변 4칸 중 하나라도 꽃이라면 False
    }
    return true;  // 위의 꽃 검사를 통과해서 5칸 모두 빈 칸임이 확인되면 True
}

// (x, y)에 꽃 심기/해제
// state : True -> 심기, False -> 해제
void setFlower(int x, int y, bool state) {
    visited[x][y] = state;  // 중앙 칸에 꽃을 state에 맞게 설정
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        visited[nx][ny] = state;  // 주변 4칸도 중앙 칸과 state가 같도록 설정
    }
}

int answer = INT_MAX; // 최소 비용을 저장할 변수, 초기값은 매우 큰 값(INT_MAX)으로 설정

// DFS로 꽃 3개 심는 모든 경우를 탐색
// count: 심은 꽃 개수, cost: 현재까지 비용 합
void dfs(int count, int cost) {
    if (count == 3) { // 꽃 3개를 모두 심었다면,
        answer = min(answer, cost); // 최소 비용 갱신
        return;
    }

    // 꽃은 가장자리에는 심을 수 없으므로, 1~(N-2)까지 반복
    for (int i = 1; i < N - 1; i++) {
        for (int j = 1; j < N - 1; j++) {
            if (canPlant(i, j)) { // 심을 수 있는 위치라면
                int c = flowerCost(i, j); // 비용 계산
                setFlower(i, j, true); // 꽃 심기
                dfs(count + 1, cost + c); // 재귀 호출로 다음 꽃 심기
                setFlower(i, j, false); // 백트래킹 : 꽃 해제
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N; // 화단 한 변의 길이 N 받기
    flowerbed.assign(N, vector<int>(N)); // N * N 화단 배열을 0으로 초기화
    visited.assign(N, vector<bool>(N, false)); // N * N visited 배열을 False로 초기화

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> flowerbed[i][j]; // 화단의 지점당 가격 G를 입력받아 화단 배열에 저장

    dfs(0, 0);  // DFS 실시
    cout << answer << "\n"; // 꽃을 심기 위한 최소 비용 answer 출력
    return 0;
}
