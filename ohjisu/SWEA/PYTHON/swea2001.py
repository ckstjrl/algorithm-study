"""
2001. 파리 퇴치 D2

N X N의 배열 안에서
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.

"""

T = int(input())
 
for test_case in range(1, T+1) :
    # 입력 받기
    N, M = list(map(int, input().split()))
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    # 초기 변수 설정
    max_sum = 0
    for i in range(N-M+1): # 0~N-M
        for j in range(N-M+1): # 0~N-M
            inner_max = 0
            for p in range(i, i + M): # i~i+M-1
                for q in range(j, j + M): # j~j+M-1
                    inner_max += N_arr[p][q]
 
            if inner_max > max_sum:
                max_sum = inner_max
 
 
    print(f"#{test_case} {max_sum}")