// BOJ11034 : 캥거루 세마리2
// 해결 방법 : 점프를 많이 뛰기 위해서, 캥거루 사이의 거리가 더 먼 캥거리 거리를 찾아서 점프 횟수를 구하기.

#include <iostream>
#include <algorithm> 
using namespace std;
int main() {
    int A, B, C;
    while (std::cin >> A >> B >> C) {
        int AB_distance = B - A - 1;
        int BC_distance = C - B - 1;
        int max_jumps = max(AB_distance, BC_distance);
        cout << max_jumps << "\n";
    }

    return 0;
}