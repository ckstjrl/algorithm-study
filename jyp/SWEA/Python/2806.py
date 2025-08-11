# N-Queen

T = int(input())


def Queen(N, x, current_y):   # x: 열, current_y: [퀸이 존재하는 행] index: 열 current_y[1] = 0 => 1번 열, 0번째 행에 퀸 존재
    global num
    if x == N:
        num += 1
        return
 
    for j in range(N):    # 오른쪽으로 한칸씩 퀸을 둘 수 있는 자리를 찾는다

        if is_available(x, j, current_y): #퀸을 둘 수 있다면
            current_y.append(j)
            Queen(N, x+1, current_y)        # 퀸을 둘 수 있다면 아래 행 탐색
            current_y.pop()                 # 탐색을 다 돌면 이 시점의 current_y 행을 제거하고 다음 열 확인 (백트래킹)

        

def is_available(x, y, current_y):
    if current_y:
        if y in current_y:              # 퀸이 같은 열에 존재하면 둘 수 없음
            return False  
        for i in range(len(current_y)):
            if x-i == abs(y-current_y[i]):  # 퀸이 대각선에 존재하면 둘 수 없음 (현재 x - 퀸이 존재하는 행 = |현재 y - 퀸이 존재하는 열| 이면 대각선에 존재함)
                return False
   
    
    return True

for tc in range(1, T+1):
    num = 0
    N = int(input())
    current_y = []
    Queen(N, 0, current_y)
    print(f'#{tc} {num}')
