/*
BOJ1080 : 행렬 (S1)

해결 방법 : 왼위쪽에서부터 하나씩 다르면 돌리기
잘 봐야하는 부분 : 
    1. 3*3보다 작으면 안 돌아감
    2. 3*3보다 작아도 같으면 0으로 정답처리
    3. 끝까지 갔는데도, 같지 않으면, 안 됨

메모 : 이게 되네?
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> change_arr(n, vector<int>(m));
    vector<vector<int>> ans_arr(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < m; j++) {
            change_arr[i][j] = line[j] - '0'; 
        }
    }

    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < m; j++) {
            ans_arr[i][j] = line[j] - '0';
        }
    }

    if (change_arr == ans_arr) {
        cout << 0 << endl;
        return 0;
    }

    if (n < 3 || m < 3) {
        cout << -1 << endl;
        return 0;
    }

    int cnt = 0;

    for (int i = 0; i <= n - 3; i++) {
        for (int j = 0; j <= m - 3; j++) {
            if (change_arr[i][j] != ans_arr[i][j]) {
                cnt++;
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        change_arr[k][l] = 1 - change_arr[k][l]; // 0 ↔ 1
                    }
                }
            }
        }
    }

    if (change_arr == ans_arr) {
      cout << cnt << endl;
    } else {
      cout << -1 << endl;
    }

    return 0;
}
