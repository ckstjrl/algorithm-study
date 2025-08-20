#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x;
    cin >> n;

    int cnt[10001] = {0, };            // 주어진 수들의 갯수를 위한 cnt 배열

    for (int i = 0; i < n; i++) {
        cin >> x;
        cnt[x]++;
    }

    for (int i = 0; i < 10001; i++) {  // cnt 배열 순회하면서 각 수의 갯수별로 출력
        while (cnt[i]--) {
            cout << i << '\n';
        }
    }

    return 0;
}