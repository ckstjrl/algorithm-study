/*
BOJ2872 : 우리집엔 도서관이 있어 (S1)

해결방법 : 일단 순서대로 되어 있는 순서를 먼저 구하기.
    1. 가장 마지막 책 위에 -1한 책이 있으면 skip
    2. 그 다음에 -1한 책이 위에 있으면 skip을 일단 반복하기
    3. 반복하지 못하는 경우, 책의 수에서 반복하지 못한 수를 빼기
    4. 뺀 수가 정답
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> books(n);
    int i;
    for (i = 0; i < n; i++) {
        cin >> books[i];
    }

    reverse(books.begin(), books.end());

    int r_cnt = 0;
    int x = n;

    for (i = 0; i < n; i++) {
        if (books[i] == x) {
            r_cnt += 1;
            x -= 1;
        }
    }
    
    int ans;
    ans = n - r_cnt;
    cout << ans << endl;
    return 0;
}