# 2476. 주사위 게임
'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄 : 참여하는 사람 수 N
그 다음 줄부터 주사위 눈 3개

if문 계속 써서 해결
- 3개 다 같을 경우
- 2개만 같을 경우
- 다 다를 경우로 나눠서 계산
최댓값 찾기.
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
price = 0
max_p = 0
for i in range(len(arr)):
    if arr[i][0] == arr[i][1] == arr[i][2]:
        price = 10000 + (arr[i][0] * 1000)
    elif arr[i][0] == arr[i][1] != arr[i][2]:
        price = 1000 + (arr[i][0] * 100)
    elif arr[i][0] == arr[i][2] != arr[i][1]:
        price = 1000 + (arr[i][0] * 100)
    elif arr[i][0] != arr[i][1] == arr[i][2]:
        price = 1000 + (arr[i][1] * 100)
    else:
        price = max(arr[i]) * 100
    if price > max_p:
        max_p = price
print(max_p)