"""
BOJ3273. 두 수의 합

[문제]
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

[출력]
문제의 조건을 만족하는 쌍의 개수를 출력한다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def find_target_sum(a, n, target):
    global cnt
    for i in range(n):  # 수열의 i번째 인덱스부터
        for j in range(i + 1, n):   # 수열의 i번째 이후 인덱스들을 j번째라고 두고 순화하면서,
            if a[i] + a[j] == x:    # i번째, j번째 수의 합이 x이면
                cnt += 1    # 찾고 있는 순서쌍이므로 count
            elif a[i] + a[j] > x:   # 만약 합이 x보다 커지면
                break   # 합 탐색 종료

# main
n = int(input())    # n : 수열의 크기
a = list(map(int, input().split())) # a : 수열
x = int(input())
a.sort()    # 수열을 오름차순으로 정렬
cnt = 0     # 구하는 순서쌍의 개수를 저장할 변수를 0으로 초기화
find_target_sum(a, n, x)    # 합이 타깃 넘버 x가 되는 순서쌍을 찾기
print(cnt)  # 결과 순서쌍의 개수 출력
