# 1979. 어디에 단어가 들어갈 수 있을까 / D2
 
T = int(input())
 
for t in range(T):
    N, K = map(int, input().split())    # 퍼즐 판 크기 N, 단어 길이 K
    puzzle = [input().split() for _ in range(N)]
    answer_cnt = 0
    
    # 퍼즐판을 검은색(0) 기준으로 split
    # 그렇게 나눠진 흰색(1)이 정확히 K칸이면 answe_cnt +1

    # 가로로
    for p in puzzle:
        p = list(''.join(p).split('0'))
        for row in p:
            if len(row) == K:
                answer_cnt += 1
    
     
    # 세로로
    new_puzzle = list(map(list, zip(*puzzle)))
    for p in new_puzzle:
        p = list(''.join(p).split('0'))
        for col in p:
            if len(col) == K:
                answer_cnt += 1
                 
 
    print(f'#{t+1} {answer_cnt}')