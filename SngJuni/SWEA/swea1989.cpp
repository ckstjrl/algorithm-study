#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin >> T;
    
	for (test_case = 1; test_case <= T; ++test_case) {
		string s;
        cin >> s;

        int n = s.size();
        int flag = 1;

        for (int i = 0; i < (n / 2); i++) {
            if (s[i] != s[n - i - 1]) {
                flag = 0;
                break;
            }
        }
        cout << "#" << test_case << " " << flag << "\n";
	}
    
	return 0;
}