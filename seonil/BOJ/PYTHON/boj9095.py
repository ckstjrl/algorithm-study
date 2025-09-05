"""
BOJ9095. 1, 2, 3 더하기
[문제]
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

[출력]
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""

import sys
sys.setrecursionlimit(10**6)

def count_ways(n):
    # 정확히 0이 되었을 때는 1가지 방법 완성
    if n == 0:
        return 1
    # 음수가 되면 불가능한 경우
    if n < 0:
        return 0
    # 1, 2, 3을 하나씩 빼면서 재귀 호출
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


T = int(sys.stdin.readline().strip())
for _ in range(1, T + 1):
    n = int(sys.stdin.readline().strip())
    print(count_ways(n))