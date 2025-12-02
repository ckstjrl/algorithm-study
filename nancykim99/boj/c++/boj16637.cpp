/*
BOJ16637 : 괄호 추가하기 (G3)

해결 방법 : 
1. 수식을 숫자와 연산자로 쪼개고, 왼쪽부터 계산
2. 현재 위치에서 DFS로 2가지 방식 진행 -> 최댓값
   1. 이번 숫자를 괄호 없이 바로 계산하는 경우
   2. 이번 숫자와 그 다음 연산·숫자를 괄호로 먼저 계산한 뒤, 그 결과를 현재 값과 계산하는 경우
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

int N;
string expr;
long long answer = LLONG_MIN;

long long calc(long long a, char op, long long b) {
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    return a * b;
}

void dfs(int idx, long long cur) {
    if (idx >= N) {
        answer = max(answer, cur);
        return;
    }

    char op = expr[idx - 1];
    long long nextNum = expr[idx] - '0';
    long long val1 = calc(cur, op, nextNum);
    dfs(idx + 2, val1);

    if (idx + 2 < N) {
        long long a = expr[idx] - '0';
        char op2 = expr[idx + 1];
        long long b = expr[idx + 2] - '0';
        long long bracket = calc(a, op2, b);
        long long val2 = calc(cur, op, bracket);
        dfs(idx + 4, val2);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    cin >> expr;

    if (N == 1) {
        cout << (expr[0] - '0') << '\n';
        return 0;
    }

    long long firstNum = expr[0] - '0';
    dfs(2, firstNum);

    cout << answer << '\n';
    return 0;
}
