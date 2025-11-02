#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];  // i번 사람이 지목하는 사람 번호 입력
    }

    vector<bool> visited(N, false);
    int cur = 0, res = 0;  // 현재 사람(cur = 0번부터 시작), 이동 횟수(res)

    while (!visited[cur]) {
        if (cur == K) {           // 현재 사람이 보성이(K)라면 
            cout << res << '\n';  // 지금까지의 이동 횟수를 출력하고 종료
            return 0;
        }

        visited[cur] = true;  // 현재 사람 방문 체크
        cur = arr[cur];       // 다음 사람으로 이동
        res++;
    }

    // 어떤 방법으로도 보성이를 만나지 못할 경우
    cout << -1 << '\n';

    return 0;
}