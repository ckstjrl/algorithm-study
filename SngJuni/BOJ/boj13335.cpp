#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, W, L;
    cin >> N >> W >> L;

    vector<int> trucks(N);
    for (int i = 0; i < N; i++) {
        cin >> trucks[i];
    }

    queue<int> bridge;
    int time = 0;
    int cur_weight = 0;
    int idx = 0;

    // 처음에 다리 길이만큼 0으로 채워두기 (빈 칸)
    for (int i = 0; i < W; i++) {
        bridge.push(0);
    }

    // 다리 위에 뭔가(0이든 트럭이든) 남아 있는 동안 진행
    while (!bridge.empty()) {
        time++;

        // 한 칸 전진: 맨 앞 칸 나감
        cur_weight -= bridge.front();
        bridge.pop();

        // 올릴 트럭이 아직 남아 있을 때만 트럭/0을 새로 올림
        if (idx < N) {
            if (cur_weight + trucks[idx] <= L) {
                // 트럭 올릴 수 있으면 올리기
                bridge.push(trucks[idx]);
                cur_weight += trucks[idx];
                idx++;
            } else {
                // 못 올리면 빈 칸(0) 채우기
                bridge.push(0);
            }
        }
        // idx == N 이면 더 이상 push 안 함 → 큐가 한 칸씩 줄어들면서 언젠가 비게 됨
    }

    cout << time << '\n';
    return 0;
}
