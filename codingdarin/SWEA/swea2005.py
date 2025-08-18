# swea 2005. 파스칼의 삼각형 (D2)

#-----------------------------------2회차 풀이 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * (i+1) for i in range(N)] # 1로 채운 삼각형 배열
 
    for i in range(2, N):
        for j in range(1, i): #양 끝이 아니면
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]  #조건에 나온 대로 식 할당
 
    print(f"#{tc}")
    for i in arr:
        print(*i)
        


#-----------------------------------1회차 풀이 


T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    arr = [[0] * N for _ in range(N)]
 
    for i in range(N):
        for j in range(i+1):
            if i == 0 or i == j:
                arr[i][j] = 1
 
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
 
    print(f'#{tc}')
    for i in arr:
        while 0 in i:
            i.remove(0)
        print(*i)