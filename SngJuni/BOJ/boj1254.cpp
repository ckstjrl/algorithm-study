#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPalindrome(const string& s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) return false;
        l++;
        r--;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int n = s.size();

    int res = 0;
    for (int i = 0; i < n; i++) {
        if (isPalindrome(s, i, n - 1)) {
            cout << n + i << '\n';
            return 0;
        }
    }

    cout << 2 * n << '\n';

    return 0;
}