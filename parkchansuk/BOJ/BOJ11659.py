# BOJ 11659. 구간 합 구하기 4 / D2
'''
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

num_prefix = [0]*(N+1)
for i in range(1, N+1):
    nxt = num[i-1]
    num_prefix[i] = num_prefix[i-1] + nxt

for _ in range(M):
    i, j = map(int, input().split())
    print(num_prefix[j] - num_prefix[i-1])
    
'''
그냥 구간 합으로 진행하면 시간이나 메모리 초과 발생할 것 같아
얼마전 풀이한 문제에서 활용한 구간합 방식 사용
'''