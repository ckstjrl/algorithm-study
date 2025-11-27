#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    
    priority_queue<int, vector<int>, greater<int>> pq;
    int num;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> num;
            pq.push(num);
            if (pq.size() > N) pq.pop();
        }
    }

    cout << pq.top() << '\n';

    return 0;
}
