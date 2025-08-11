'''
2001. 파리 퇴치

c++ 코드 참고.
'''

T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
 
    arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
 
    max_fly = 0
    for i in range(N-M+1):              # 파리채가 움직일 수 있는 범위
        for j in range(N-M+1):
            result = 0
            for col in range(i, i+M):   # 파리채의 크기 범위
                for row in range(j, j+M):
                    result += arr[col][row]
 
            if max_fly < result:
                max_fly = result
 
    print(f'#{tc} {max_fly}')