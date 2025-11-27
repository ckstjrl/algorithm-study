// BOJ2720 : 세탁소 사장 동혁 (B3)
// 해결 방법 : 그리디로 동전 값이 더 높은 것부터 나누기. 나머지는 다음 높은 값의 동전으로 나누기.

#include <iostream>
using namespace std;

int main() {
    int tc;
    cin >> tc;

    while (tc--) {
        int cent;
        cin >> cent;

        int Q, D, N, P; 

        Q = cent / 25;
        cent %= 25; 

        D = cent / 10;
        cent %= 10;

        N = cent / 5;
        cent %= 5;

        P = cent; 

        cout << Q << " " << D << " " << N << " " << P << "\n";
    }

    return 0;
}