# Ladder1 / D4
for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    i, j = 99, 0 # 시작은 마지막 줄에서 시작
    for y in range(100):
        if ladder[99][y] == 2:
            j = y # 마지막 줄에서 2 찾아서 j에 idx 값 넣어줌
            break
    while i > 0:
        if j >0 and ladder[i][j-1] == 1: # 왼쪽이 조건과 맞는지 확인
            while j > 0 and ladder[i][j-1] == 1: # 한번 왼쪽을 만족하면 같은 행에서는 오른쪽을 확인할 필요가 없어서 계속 왼쪽 확인
                j -= 1 # 왼쪽으로 이동 while 조건 통과한 만큼
            i -= 1 # 왼쪽으로 다 이동했으면 오른쪽은 지나온 길이므로 위로 올라감
        
        elif j < 99 and ladder[i][j+1] == 1: # 오른쪽이 조건과 맞는지 확인
            while j < 99 and ladder[i][j+1] == 1: # 한번 오른쪽을 만족하면 같은 행 왼쪽 확인 필요 없으니 계속 오른쪽 확인
                j += 1 # 오른쪽으로 이동 while 조건 통과한 만큼
            i -= 1 # 오른쪽 다 이동했으면 왼쪽은 지나온 길이므로 위로 올라감
        
        else: # 왼쪽, 오른쪽 둘다 조건만족 안하면 위로 올라감
            i -= 1
    print(f'#{T} {j}')
    # runtime Error 해결하기 위해 while - if - while 사용