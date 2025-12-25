/*boj17608 - 막대기
아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 
각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 
일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 
즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 
예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.



N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 입출력 속도 향상
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    int cnt = 0; // 막대기 개수
    int max_height = 0; // 최대 높이

    for (int i = N - 1 ; i >= 0; i--) {
        // 거꾸로 순회하며 최대 높이가 갱신될 때 카운트 증가
        if (arr[i] > max_height) {
            max_height = arr[i];
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}