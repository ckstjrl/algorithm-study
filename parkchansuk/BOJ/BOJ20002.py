# BOJ 20002. 사과나무 / D3
'''
문제
N × N 크기의 정사각형 모양 과수원이 있고, N × N 개의 사과나무가 1 × 1 크기의 간격으로 모든 칸에 심어져있다.

농부 형곤이가 가을을 맞아 사과를 수확하려는데, 땅주인 신영이가 "너는 과수원 내에 사과나무를 K × K 의 크기의 정사각형 모양으로만 수확해 가져갈 수 있어, 이때 K는 1보다 크거나 같고 N보다 작거나 같은 정수라구! 나머지는 내가 먹을께! 하하!" 라고 통보했다.

하나의 사과나무를 수확할 때, 사과를 통해 얻을 수 있는 이익과 노동비로 빠져나가는 손해가 동시에 이루어진다.

그래서 형곤이는 나무의 위치를 좌표로 하여, 사과를 통해 얻은 이익과 노동비를 더한 총이익을 2차원 배열의 형태로 정리했다.

악독한 땅주인 신영이로부터 고통받는 귀여운 형곤이에게 최대 총이익을 안겨주고 싶은 당신, 형곤이를 도와주자!

입력
첫 번째 줄에는 과수원의 크기 N이 주어진다. (1 ≤ N ≤ 300)

두 번째 줄부터 N + 1번째 줄까지, 해당 나무를 수확했을 때 얻을 수 있는 총이익을 표시한다.

총이익은 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫 번째 줄에 최댓값을 출력한다.
'''
import sys
input = sys.stdin.readline
N = int(input().strip())
apple = [list(map(int, input().split())) for _ in range(N)]

prefix = [[0]*(N+1) for _ in range(N+1)] # apple[0][0]을 기준으로 그 i, j까지 직사각형들의 합
for i in range(N):
    y_sum = 0
    for j in range(N):
        y_sum += apple[i][j]
        prefix[i+1][j+1] = prefix[i][j+1] + y_sum

def total_price(i1, j1, i2, j2):
    return (prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1])


max_sum = -1000*300*300
for k in range(1, N+1):
    for y in range(N-k+1):
        for x in range(N-k+1):
            k_sum = total_price(y, x, y+k-1, x+k-1)
            if k_sum > max_sum:
                max_sum = k_sum
print(max_sum)
# 시간 복잡도 생각 없이 구현
'''
import sys
input = sys.stdin.readline
N = int(input().strip())
apple = [list(map(int, input().split())) for _ in range(N)]
max_sum = -1000
for k in range(1, N):
    k_sum = []
    for i in range(N-k+1):
        for j in range(N-k+1):
            k_sum.append((i, j))
    for a in range(len(k_sum)):
        si, sj = k_sum[a]
        k_sum_ = 0
        for y in range(k):
            for x in range(k):
                k_sum_ += apple[si+y][sj+x]
        k_sum[a] = k_sum_
    max_k = max(k_sum)
    if max_sum < max_k:
        max_sum = max_k

print(max_sum)
'''

'''
그냥 구현하게 되면 시간복잡도 O(N^6)
순간마다 사각형 내부 합을 구하는게 아니라 미리 0,0에서부터 i,j까지 직사각형의 합의 구하고
정사각형의 길이가 나왔을 때 해당 좌표를 넣어 미리 누적합 해놓은 이차원배열 원소끼리 빼는 것이
훨씬 시간복잡도 감소
But,
def total_price(i1, j1, i2, j2):
    return (prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1])
이거 고민하는게 생각보다 어려웠음
'''