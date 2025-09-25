#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int T, k;
    cin >> T;
 
    while (T--) {
        cin >> k;

        // 최대 힙 - 최댓값을 바로 꺼내기 위해
        priority_queue<pair<int, int>> max_heap;
        // 최소 힙 - 최솟값을 바로 꺼내기 위해
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;
        // 각 힙에 유효한 정수인지 확인하기 위해
        vector<bool> check(k);

        char Q;
        int num, idx = 0;
        for (int i = 0; i < k; i++) {
            cin >> Q >> num;
            if (Q == 'I') {         // 삽입 연산
                min_heap.push({num, idx});
                max_heap.push({num, idx});
                check[idx] = true;  // 현재 인덱스의 원소는 유효하다고 체크
                idx++;  // 인덱스 증가
            } else if (Q == 'D') {  // 삭제 연산
                if (num == 1) {     // 최댓값 삭제
                    while (!max_heap.empty()) {  // 최대 힙이 비지 않은 동안
                        int top = max_heap.top().second;
                        if (check[top]) break;  // 유효한 정수(top) 찾아서 탈출
                        max_heap.pop();         // 유효하지 않은 정수 제거
                    }
                    if (!max_heap.empty()) {
                        int top = max_heap.top().second;  // 유효한 최댓값 찾아서 유효하지 않다고 표시 (이후 제거됨.)
                        check[top] = false;
                    }
                } else if (num == -1) {  // 최솟값 삭제
                    while (!min_heap.empty()) {  // 최소 힙이 비지 않은 동안
                        int top = min_heap.top().second;
                        if (check[top]) break;  // 유효한 정수(top) 찾아서 탈출
                        min_heap.pop();         // 유효하지 않은 정수 제거
                    }
                    if (!min_heap.empty()) {
                        int top = min_heap.top().second;  // 유효한 최솟값 찾아서 유효하지 않다고 표시 (이후 제거됨.)
                        check[top] = false;
                    }
                }
            }
        }

        // 두 힙에서 유효하지 않은 정수 제거
        while (!max_heap.empty()) {
            int top = max_heap.top().second;
            if (check[top]) break;
            max_heap.pop();
        }
        while (!min_heap.empty()) {
            int top = min_heap.top().second;
            if (check[top]) break;
            min_heap.pop();
        }

       
        if (max_heap.empty() || min_heap.empty()) {   // 두 힙 중 하나라도 비었으면 EMPTY 출력
            cout << "EMPTY\n";
        } else {  // 양쪽 다 비지 않았다면 최댓값과 최솟값 출력
            cout << max_heap.top().first << ' ' << min_heap.top().first << '\n';
        }
    }
    
    return 0;
}