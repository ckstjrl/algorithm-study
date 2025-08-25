# 3431. 준환이의 운동관리 / D3

T = int(input())
for tc in range(T):
    # L분 이상 U분 이하가 적절, 운동 X분 함
    # 많이 했으면 -1, 더 필요하면 몇 분 더 필요한지 출력
    L, U, X = map(int, input().split())

    if X <= L:          # 더 운동 필요
        res = L - X     
    elif  X > U:        # 필요한 양보다 더 많이 함
        res = -1
    else:               # 적정량만큼 운동함 
        res = 0

    print(f'#{tc+1} {res}')