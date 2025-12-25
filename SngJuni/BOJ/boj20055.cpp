#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    int n = 2 * N;

    vector<int> arr(n);            // 내구도 배열
    vector<bool> robot(n, false);  // 해당 칸에 로봇 여부
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int res = 1;

    while (true) {
        // 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        int last = arr[n - 1];
        bool lastRobot = robot[n - 1];
        for (int i = n - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
            robot[i] = robot[i - 1];
        }
        arr[0] = last;
        robot[0] = lastRobot;

        if (robot[N - 1]) robot[N - 1] = false;  // 내리는 위치에서는 로봇을 내림.

        // 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        //    만약 이동할 수 없다면 가만히 있는다.
        for (int i = N - 1; i > 0; i--) {
            if (robot[i - 1] && !robot[i] && arr[i] > 0) {
                robot[i] = true;
                robot[i - 1] = false;
                arr[i]--;
            }
        }

        if (robot[N - 1]) robot[N - 1] = false;  // 내리는 위치에서는 로봇을 내림.

        // 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if (!robot[0] && arr[0] > 0) {
            robot[0] = true;
            arr[0]--;
        }

        // 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) cnt++;
        }

        if (cnt >= K) break;

        res++;
    }

    cout << res << '\n';

    return 0;
}