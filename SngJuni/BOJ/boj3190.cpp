#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int n, k, l;
int arr[101][101];  // 사과의 위치 정보를 위한 정적 배열
char cmd[100001];   // 방향 전환 정보를 위한 정적 배열

int dx[4] = {0, 1, 0, -1};  // 우, 하, 좌, 상 순서의 델타 배열
int dy[4] = {1, 0, -1, 0};

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> n;

    int x, y;
    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> x >> y;
        arr[x][y] = 1;  // 사과의 위치를 1로 표시
    }

    int t;
    char c;
    cin >> l;
    for (int i = 0; i < l; i++) {
        cin >> t >> c;
        cmd[t] = c;
    }

    deque<pair<int, int>> snake;  // 뱀이 차지하고 있는 좌표들을 위한 deque
    snake.push_back({1, 1});      // 1, 1 에서 시작
    int time = 0, dir = 0;        // 시간은 0에서부터, 방향도 오른쪽(0)에서부터 시작

    int flag = 0;  // 뱀 자기자신에 부딪혔을 때, 반복문 끝내기 위한 플래그
    while (1) {
        time++;  // 시간 1 증가
        
        int nx = snake.front().first + dx[dir];   // 방향에 따라 뱀의 머리가 위치할 x 좌표
        int ny = snake.front().second + dy[dir];  // 방향에 따라 뱀의 머리가 위치할 y 좌표

        if (nx < 1 || nx > n || ny < 1 || ny > n) break;  // 벽에 부딪히면 종료
        for (auto s : snake) {                            // deque 순회하며 자기자신에 부딪히면 종료
            if (nx == s.first && ny == s.second) {
                flag = 1;
                break;
            }
        }
        if (flag) break;

        snake.push_front({nx, ny});  // 뱀의 머리를 늘림.
        if (arr[nx][ny] == 1) {      // 이동한 칸에 사과가 있다면, 사과 없어지고 꼬리 그대로
            arr[nx][ny] = 0;
        } else {                     // 이동한 칸에 사과가 없다면, 몸길이 줄임. -> deque 의 마지막 pop
            snake.pop_back();
        }

        if (cmd[time] == 'L') {          // 시간에 따라 주어진 방향 전환 정보 반영
            dir = (dir + 3) % 4;
        } else if (cmd[time] == 'D') {
            dir = (dir + 1) % 4;
        }
    }
    cout << time << '\n';  // 몇 초에 끝나는지 결과 출력

    return 0;
}