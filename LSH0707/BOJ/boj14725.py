import sys
input = sys.stdin.readline
N = int(input())
food = []
for _ in range(N):
    arr = list(input().split())
    food.append(arr[1:])
food.sort()  # 주어진 먹이 정보 오름차순 정렬
for i in range(len(food[0])):  # 0번 인덱스 먹이 정보 출력
    x = '--'*i + food[0][i]
    print(x)
for i in range(1, N):
    # 좌측 인덱스 먹이 정보 비교
    left = food[i-1]
    right = food[i]
    min_len = min(len(left), len(right))
    cnt = 0
    while cnt < min_len:  # 분기되는 지점의 인덱스 구하기((ABCD, ABCE) -> cnt = 3)
        if left[cnt] == right[cnt]:
            cnt = cnt + 1
        else:
            break
    for j in range(cnt, len(food[i])):  # 분기되는 지점부터 먹이정보 출력
        x = '--'*j + food[i][j]
        print(x)
