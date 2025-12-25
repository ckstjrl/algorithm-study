#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int L, C;
vector<char> arr;
vector<char> comb;

int check() {  // 모음 1개 이상, 자음 2개 이상인지 체크하는 함수
    int x = 0;
    int y = 0;
    
    for (int i = 0; i < L; i++) {
        if (comb[i] == 'a' || comb[i] == 'e' || comb[i] == 'i' ||
            comb[i] == 'o' || comb[i] == 'u') x++;
        else y++;
    }
    if (x >= 1 && y >= 2) return 1;
    else return 0;
}

void dfs(int depth, int prev) {
    if (depth == L && check()) {  // 조건 충족될 때, 출력
        for (int i = 0; i < L; i++) {
            cout << comb[i];
        }
        cout << '\n';
    }

    for (int i = prev; i < C; i++) {  // 재귀적으로 dfs 함수 호출하면서 조합 만들기
        comb[depth] = arr[i];
        dfs(depth + 1, i + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> L >> C;

    arr.assign(C, 0);
    comb.assign(C, 0);

    for (int i = 0; i < C; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());  // 사전 순으로 조합 만들기 위해 정렬
    dfs(0, 0);  // dfs 함수로 조합 만듦

    return 0;
}