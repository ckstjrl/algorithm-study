# 2775. 부녀회장이 될테야

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    # 각 n호씩 k층 의 거주민 수를 기록할 2차원 배열 
    apt = [[0]*n for _ in range(k+1)]
    
    for p in range(k+1):
        for q in range(n):
            if p == 0:          # 0층 i호에는 i명 거주 (i는 1부터 시작)
                apt[p][q] = q+1
            else:               # a층 b호에는 (a-1)층 1호~b호 사람의 합만큼의 사람이 거주
                apt[p][q] = sum(apt[p-1][:q+1])
    
    ans = apt[k][n-1]
    print(ans)
    
    