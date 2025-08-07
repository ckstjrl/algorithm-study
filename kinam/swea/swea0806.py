'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.

파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
'''
#인덱스 (M, M) 부터 시작해서 끝 지점은 (N-M, N-M)
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    di1 = [1, 0, -1 ,0] # +를 표현
    dj1 = [0, 1, 0, -1]

    di2 = [1, 1, -1, -1] # x를 표현
    dj2 = [1, -1, 1, -1]

    max_list = []
    max_plus = 0
    max_x = 0
    

    for i in range(N): #arr[i][j]를 표현하기 위한 for문
        for j in range(N):
            s = arr[i][j] # 가운데 값 할당
            for c in range(1,M): # 델타를 M까지의 길이만큼 반복할 것 
                for di, dj in list(zip(di1, dj1)): #zip을 써서 di, dj를 묶을 수 있음
                    if (0 <= (i+di*c) < N) & (0 <= (j+dj*c) < N): # 다음 인덱스가 벗어나는지 확인
                        s += arr[i+di*c][j+dj*c] # 십자 배열 더하기
            if max_plus < s :
                max_plus = s

            
            s = arr[i][j]  # 가운데 값 할당
            for c in range(1,M): # x자 파리잡기
                for di, dj in list(zip(di2, dj2)): #zip을 써서 di, dj를 묶을 수 있음
                    if (0 <= (i+di*c) < N) & (0 <= (j+dj*c) < N):
                        s += arr[i+di*c][j+dj*c] # X자 배열 더하기
            if max_x < s:
                max_x = s

    print(f"#{t} {max(max_plus, max_x)}")