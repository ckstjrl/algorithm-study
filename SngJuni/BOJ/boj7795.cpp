#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<int> A(N, 0);
        vector<int> B(M, 0);

        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        for (int i = 0; i < M; i++) {
            cin >> B[i];
        }

        sort(A.rbegin(), A.rend());
        sort(B.rbegin(), B.rend());

        int res = 0, j = 0;
        for (int i = 0; i < N; i++) {
            while (j < M && A[i] <= B[j]) {
                j++;
            }
            res += (M - j);
        }

        cout << res << '\n';
    }

    return 0;
}