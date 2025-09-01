# swea 1974. 스도쿠 검증 (D2)

T = int(input())
for tc in range(1, T+1):
    N = 9   # 스도쿠 가로, 세로
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 1 # 문제 없다고 가정
   
    myset = set()   # 체크할 빈 세트
    set_ans = {1,2,3,4,5,6,7,8,9} #정답 비교용 세트

    now = 0    # 가로 체크
    for i in range(N):
        for j in range(N):
                myset.add(arr[i][j]) # 세트에 추가  
        if myset != set_ans: # 정답과 다르면
            ans = 0
            break
        myset.clear()            
    
    for j in range(N):
        for i in range(N):
                myset.add(arr[i][j])  # 세트에 추가
        if myset != set_ans:
            ans = 0    
            break
        myset.clear()
    
    #스퀘어 체크
    dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for i in range(0,N,3):
        for j in range(0,N,3):
            for x, y in zip(dx,dy):
                myset.add(arr[i+x][j+y])
            if myset != set_ans:# 세트와 다르면
                ans = 0    
                break
            myset.clear()

    print(f"#{tc} {ans}")