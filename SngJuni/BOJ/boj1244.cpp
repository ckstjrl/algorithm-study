#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int n, m;
    cin >> n;

    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cin >> m;

    int s, num;
    for (int i = 0; i < m; i++) {
        cin >> s >> num;

        if (s == 1) {  // 남학생
            for (int j = 0; j < n; j++) {
                if (!((j + 1) % num)) {  // num의 배수면 스위치 상태 바꿈
                    if (arr[j]) arr[j] = 0;
                    else arr[j] = 1;
                }
            }
        }
        else if (s == 2) {  // 여학생
            num--;

            for (int j = 0; j < n / 2; j++) {  // num을 기준으로 좌, 우측 순회
                if (num - j < 0 || num + j >= n) continue;

                if (arr[num - j] == arr[num + j]) {  // 같으면 스위치 상태 바꾸고
                    if (arr[num - j]) {
                        arr[num - j] = 0;
                        arr[num + j] = 0;
                    }
                    else {
                        arr[num - j] = 1;
                        arr[num + j] = 1;
                    }
                } else {  // 같지 않으면 반복문 자체를 끝냄.
                    break;
                }
            }
        }
    }

    for (int i = 0; i < (n / 20) + 1; i++) {  // 한 줄에 20개씩 출력
        for (int j = 0; j < 20 && 20 * i + j < n; j++) {
            cout << arr[20 * i + j] << ' ';
        }
        cout << '\n';
    }

    // Chat GPT로 최적화시킨 한 줄에 20개씩 출력하는 방법  
    // for (int i = 0; i < n; ++i) {
    //     cout << arr[i] << (i % 20 == 19 || i == n - 1 ? '\n' : ' ');
    // }
     
    return 0;
}