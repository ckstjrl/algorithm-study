/*
BOJ16637 - 괄호 추가하기

문제 정의
1. 길이가 N인 수식
2. 괄호 안에 괄호 넣기는 안된다
3. 괄호가 있으면 먼저 계산 or 왼쪽부터 계산
4. 괄호를 적절히 추가해 만들 수 있는 값의 최대를 구하라
5. 괄호의 개수는 정해져있지 않고, 추가하지 않아도 괜찮다.

로직 정의
DFS or 백트래킹???
-> 어쨋든 모든 경우의 수를 거의 다 보지 않으면 힘듬
가장 중요한 점은 범위에 주의하면서
음 양 모두 ll 바로 직전이라고 되어있지만 계산 과정에서 터질수도?



*/

// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;

// int n, max_ans;
// string str;

// // using ll = long long;

// int calc(int a, int b, char op){
//     int r = 0;
//     if (op == '+'){
//         r = a + b;
//     }
//     else if (op == '-')
//     {
//         r = a - b;
//     }
//     else{
//         r = a * b;
//     }
//     return r;
// }


// void dfs(int idx, int cur){
//     // 종료 조건
//     if (idx == str.length()){
//         max_ans = max(max_ans, cur);
//         return;
//     }
//     // 괄호 치지 않고 바로 연산
//     dfs(idx+2, calc(int(str[idx]), int(str[idx+2]), str[idx+1]));

//     // 괄호 치기
//     if (idx + 4 <= str.length()-1){
//         int temp = calc(int(str[idx+2]), int(str[idx+4]), str[idx+3]);
//         dfs(idx+4, calc(int(str[idx]), temp, str[idx+1]));
//     }
//     return;
// }



// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);

//     cin >> n >> str;
//     dfs(0,0);
//     cout << max_ans << '\n';
// }

#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

using ll = long long;

int N;
ll ans = LLONG_MIN;
string str;


ll calc(ll a, ll b, char op){
    if (op == '+'){
        ll r = a + b;
        return r;
    } else if (op == '-'){
        ll r = a - b;
        return r;
    } else{
        ll r = a * b;
        return r;
    }
}

void dfs(int idx, ll cur){
    if (idx >= N) {
        ans = max(ans, cur);
        return;
    }
    // 괄호 사용 X 순회
    ll nx1 = calc(cur, str[idx+1] - '0', str[idx]);
    dfs(idx+2, nx1);
    // idx 터짐 방어용
    if (idx + 3 < N){
        // 괄호 내부 계산
        ll temp = calc(str[idx+1] - '0', str[idx+3] - '0', str[idx+2]);
        // 괄호 이전 값과 연산 진행
        dfs(idx + 4, calc(cur, temp, str[idx]));
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> str;
    if (N == 1){
        // c++에서 char(숫자) -'0'이 int(char)이다.
        cout << (str[0] - '0') << '\n';
        return 0;
    }

    dfs(1, str[0] - '0');
    cout << ans << '\n';
}