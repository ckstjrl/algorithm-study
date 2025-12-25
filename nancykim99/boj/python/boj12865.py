'''
BOJ12865 : 평범한 배낭 (G5)

해결방법 :
1. 물건들을 sort : dp에 넣을 때 큰 수부터 넣기 -> 시간이 주는지는 모르겠음
2. item들을 거꾸로 돌면서 dp의 값들과 비교하며 max인 값을 넣기
3. 넣을 수 있는 만큼 item들이 들어가 최댓값을 얻을 수 있음

메모 : 
조합 만드는 bfs로 가지치기 까지 했는데, 시간 초과... 다 돌아가서 더 아쉬움
`
# 합 찾으면서 flag하는 함수 
def find_sum (list, k):
    total = 0
    for w, v in list:
        total += w
        if total > k:
            return False
    return True

# 조합 만드는 bfs
def bfs (idx, list, r, flag, k):
    if flag == False:
        return 
    if idx == n: # 전체를 다 돌았을때
        if len(list) == r: # r과 길이가 동일해졌을 때
            answer.append(list[:])
        return 
    list.append(products[idx])
    new_flag = find_sum(list, k)
    bfs(idx + 1, list, r, new_flag, k)
    list.pop()
    bfs(idx + 1, list, r, flag, k)

n, k = map(int, input().split())
products = []
for _ in range(n):
    w, v = map(int, input().split())
    products.append((w, v))

products.sort()

answer = []

for i in range(1, (n+1)):
    flag = True
    bfs(0, [], i, True, k)

max_sum = 0
for product in answer:
    total = 0
    for w, v in product:
        total += v
    if total > max_sum:
        max_sum = total

print(max_sum)
`
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)] 
items.sort() # dp에 뒤에서부터 넣기 위해 sort

dp = [0] * (k + 1)

for w, v in items:
    for cap in range(k, w - 1, -1): # 거꾸로 돌아야 한 번 넣은 물건을 다시 안 넣음
        candidate = dp[cap - w] + v
        if candidate > dp[cap]:
            dp[cap] = candidate

print(dp[k])
