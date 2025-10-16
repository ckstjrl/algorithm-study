#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int N, M;
        cin >> N >> M;
        int a, b;
        for (int i = 0; i < M; i++) {
            cin >> a >> b;
        }
        cout << N - 1 << '\n';
    }

    return 0;
}