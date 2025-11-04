"""
[문제]
세 양의 정수 a, b, c가 주어질 때, 다음 조건을 만족하는 정수 쌍 (x, y, z)의 개수를 구하시오.

1 <= x <= a
1 <= y <= b
1 <= z <= c

(x mod y) = (y mod z) = (z bmod x)$

(A mod B)는 A를 B로 나눈 나머지를 의미한다.

[입력]
첫째 줄에 테스트 케이스의 수 T가 주어진다. (1 <= T <= 600,000)
다음 T개의 각 줄에는 세 정수 a, b, c가 공백으로 구분되어 주어진다. (1 <= a, b, c <= 100,000)

[출력]
한 줄에 하나씩 정답을 출력한다.
"""
import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
    a, b, c = map(int, input().split())
    ans.append(str(min(a,b,c)))
print("\n".join(ans))
