# 8 * 8 크기 체스판
# 가장 왼쪽 위칸 (0, 0)은 하얀색

board = [list(map(str, input())) for _ in range(8)]

# 간단한 계산을 위해서 1차원 배열로 변경
# 해당 방법으로는 답이 나오지 않음을 확인 2차 배열에서 진행 필요
# flat_board = sum(board, [])

#흰색 칸 위에 말의 수를 세기
count = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        #홀수 라인
        if i % 2 == 0:
            if j % 2 == 0:
                if board[i][j] == 'F':
                    count += 1
        #짝수 라인
        if i % 2 == 1:
            if j % 2 == 1:
                if board[i][j] == 'F':
                    count += 1

print(count)