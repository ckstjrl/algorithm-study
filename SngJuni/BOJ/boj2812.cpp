#include <iostream>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >>K;

    string s;
    cin >> s;

    stack<char> st;
    for (const auto& c : s) {  // 문자열 순회하면서
        while (!st.empty() && K > 0 && st.top() < c) {  // 현재의 c보다 작은 값을 스택에서 모두 pop -> 지움.
            st.pop();
            K--;
        }
        st.push(c);  // 현재 c를 스택에 push
    }

    while (K > 0 && !st.empty()) {  // 지워야할 수가 남아있으면 끝에서 남은 K만큼 지움.
        st.pop();
        K--;
    }

    string res = "";  // 결과를 담음.
    while (!st.empty()) {
        res += st.top();
        st.pop();
    }
    reverse(res.begin(), res.end());  // 스택이라 순서가 반대로 나와서 뒤집어줌.

    cout << res << '\n';

    return 0;
}

// 최소 힙 써서 풀어본 코드 -> 가장 작은 수를 없애는 방식이지만 최댓값을 위해서는 왼쪽에서부터 지워야해서 반례가 있음.
// #include <iostream>
// #include <vector>
// #include <string>
// #include <queue>
// #include <unordered_set>

// using namespace std;

// int main() {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N, K;
//     cin >> N >>K;

//     string s;
//     cin >> s;

//     vector<int> num(N);
//     priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> pq;

//     for (int i = 0; i < N; i++) {
//         num[i] = s[i] - '0';
//         pq.push({s[i] - '0', i});
//     }

//     unordered_set<int> removedIdx;
//     for (int i = 0; i < K; i++) {
//         removedIdx.insert(pq.top().second);
//         pq.pop();
//     }
//     string res = "";
//     for (int i = 0; i < N; i++) {
//         if (removedIdx.find(i) == removedIdx.end()) {
//             res += to_string(num[i]);
//         }
//     }

//     cout << res << '\n';

//     return 0;
// }