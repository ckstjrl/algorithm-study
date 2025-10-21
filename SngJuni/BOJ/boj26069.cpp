#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    unordered_set<string> us;
    us.insert("ChongChong");

    int N;
    cin >> N;

    string s1, s2;
    for (int i = 0; i < N; i++) {
        cin >> s1 >> s2;
        if (us.find(s1) != us.end() || us.find(s2) != us.end()) {
            us.insert(s1);
            us.insert(s2);
        }
    }

    cout << us.size() << '\n';

    return 0;
}