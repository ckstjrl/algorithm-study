# BOJ 9070. 장보기 (D1 / B2)
# https://www.acmicpc.net/problem/9070

import sys
input = sys.stdin.readline

def buy(p_list):
    min_ratio = float('inf')
    ans_cost = float('inf')

    for weight, cost in p_list:
        ratio = cost / weight
        if ratio < min_ratio:
            min_ratio = ratio
            ans_cost = cost
        elif ratio == min_ratio:
            if cost < ans_cost:
                ans_cost = cost

    return ans_cost


T = int(input())

for _ in range(1, T+1):
    N = int(input())
    p_list = [list(map(int, input().split())) for _ in range(N)]

    print(buy(p_list))