#include <iostream>
#include <vector>
 
using namespace std;
 
int main (int argc, char** argv) {
    int test_case;
    int T;
    cin >> T;
 
    for (test_case = 1; test_case <= T; ++test_case) {
        int n, m, res = 0;
        cin >> n >> m;
 
        vector<vector<int>> arr(n, vector<int>(n, 0));  // 2차원 배열 0으로 초기화
        for (int i = 0; i < n; i++) {                   // 파리의 갯수 입력 받기
            for (int j = 0; j < n; j++) {
                cin >> arr[i][j];
            }
        }
 
        for (int i = 0; i < n - m + 1; i++) {           // 파리채의 영역이 m 이므로 n - m + 1번째의 인덱스까지만 순회
            for (int j = 0; j < n - m + 1; j++) {
                int temp = 0;
                 
                for (int k = 0; k < m; k++) {           // i, j번째 인덱스에서 m * m 영역의 파리의 갯수의 총합 계산
                    for (int l = 0; l < m; l++) {
                        temp += arr[i + k][j + l];
                    }
                }
 
                if (res < temp) {                       // max 값인 res 갱신
                    res = temp;
                }
            }
        }
        cout << "#" << test_case << " " << res << "\n";
    }
 
    return 0;
}