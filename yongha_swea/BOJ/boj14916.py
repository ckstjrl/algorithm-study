#boj14916 거스름돈

change = int(input())

count = 0

#잔돈이 남아있는 동안 반복
while change:
    # 거스름돈이 0으로 떨어지지 않아서 -가 되는 경우 -1 출력
    if change < 0:
        count = -1
        break
    # 만약 5로 나눠 떨어진다면 그 수를 전체 동전 수에 더해주고 루프 탈출
    elif change % 5 == 0:
        count = count + (change // 5)
        break
    #5로 나눠 떨어지지 않는다면 잔돈에서 2를 빼고 동전 수에 1을 더해준 이후 다시금 루프 반복
    else:
        change = change - 2
        count += 1

print(count)