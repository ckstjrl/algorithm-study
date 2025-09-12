# 2798. 블랙잭
'''
N장의 카드 중에서 3장의 카드를 고를 때 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

n장 중 3장을 뽑아 합을 할 때 그 합이 가장 큰 것을 구하기.
3장을 뽑기 위해 for문을 3개 돌린다. -> 시간복잡도에 걸릴 수 있음.
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = arr[i] + arr[j] + arr[k]
            if card_sum <= m:  # 카드 합이 m을 넘지 않으면
                if card_sum > result:  # 더 큰 합이 나오면 result를 갱신
                    result = card_sum
print(result)