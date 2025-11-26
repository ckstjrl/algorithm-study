# BOJ 1912. 연속합 / D2
'''
문제
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

dp = [-1001]*N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))


# 누적합으로 구하려다 시간 초과
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

prefix_max =[]
for i in range(N):
    prefix = [-1001]*N
    prefix[i] = arr[i]
    for j in range(i, N-1):
        prefix[j+1] = prefix[j] + arr[j+1]
    max_v = max(prefix)
    prefix_max.append(max_v)

ans = max(prefix_max)
print(ans)
'''

'''
그냥 단순하게 생각하면 되는 문제였음.
arr[i]와 dp[i-1]+arr[i] 중 더 큰 값을 dp에 넣고 끝까지 반복하면 큰 값이 나올 수 밖에 없음
'''