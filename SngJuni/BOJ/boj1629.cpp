#include <iostream>

using namespace std;

long long a, b, c;  // 

long long r_power(long long a, long long b) {
    if (b == 0) return 1 % c;  // 지수가 0이면 결과는 1
    if (b == 1) return a % c;  // 지수가 1이면 a를 c로 나눈 나머지 반환

    long long half = r_power(a, b / 2);  // 지수를 반씩 분할해서 재귀적으로 함수 호출
    long long ret = (half * half) % c;   // 분할된 반씩 정복(곱셈)해서 반환하기 위한 변수
    if (b % 2) {  // 홀수면 a를 한 번 더 곱해야 함.
        ret = (ret * (a % c)) % c;
    }

    return ret;  // a^b (mod c) 반환
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> a >> b >> c;

    cout << r_power(a, b) << '\n';  // 재귀 함수 호출 및 결과 출력

    return 0;
}