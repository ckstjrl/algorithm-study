#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    
    while (T--) {
        long long a, b, c;
        cin >> a >> b >> c;
        cout << min({a, b, c}) << '\n';
    }

    return 0;
}