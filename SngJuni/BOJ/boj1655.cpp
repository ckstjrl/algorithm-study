#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    priority_queue<int> left; // 왼쪽 (절반)
    priority_queue<int, vector<int>, greater<int>> right; // 오른쪽 (절반)

    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;

        if (left.empty() || num <= left.top()) left.push(num);
        else right.push(num);

        if (left.size() < right.size()) {
            left.push(right.top());
            right.pop();
        } else if (left.size() > right.size() + 1) {  // 왼쪽의 크기가 오른쪼과 같거나 하나 더 많도록 유지
            right.push(left.top());
            left.pop();
        }

        cout << left.top() << '\n';  // 항상 중앙값은 left의 top
    }

    return 0;
}


// 시간 초과 뜬 코드 1
// #include <iostream>
// #include <vector>
// #include <queue>
// #include <stack>

// using namespace std;

// int main() {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N;
//     cin >> N;

//     priority_queue<int> pq;
//     vector<int> arr;

//     int num;
//     for (int i = 0; i < N; i++) {
//         cin >> num;

//         pq.emplace(num);

//         int temp = 0;
//         while (!pq.empty() && temp < (i / 2) + (i % 2) + 1) {
//             arr.push_back(pq.top());
//             pq.pop();
//             temp++;
//         }

//         cout << arr.back() << '\n';

//         for (int i = 0; i < arr.size(); i++) {
//             pq.emplace(arr[i]);
//         }
//         arr.clear();
//     }

//     return 0;
// }

// 시간 초과 뜬 코드 2
// #include <iostream>
// #include <queue>

// using namespace std;

// int main() {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N;
//     cin >> N;

//     priority_queue<int> pq;

//     int num;
//     for (int i = 0; i < N; i++) {
//         cin >> num;

//         pq.emplace(num);

//         priority_queue<int> pq_copy = pq;
//         for (int j = 0; j < (i / 2) + (i % 2); j++) {
//             pq_copy.pop();
//         }
//         cout << pq_copy.top() << '\n';
//     }

//     return 0;
// }