'''
빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다



다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.



차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.



이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.



철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
'''



board = []
for _ in range(5):
    line = input().split()
    row = [int(x) for x in line]
    board.append(row)

calls = []
for _ in range(5):
    line = input().split()
    for x in line:
        calls.append(int(x))  # 그냥 25개 일렬로 저장함.

# 숫자를 보드에서 찾아서 0으로 바꾸는 함수. 아마도 항상 전체 탐색?
def mark_number(num):
    found = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                found = True
    return found

# 현재 보드의 빙고 줄 개수를 세는 함수.
def count_bingo_lines():
    cnt = 0

    for i in range(5):
        all_zero = True
        for j in range(5):
            if board[i][j] != 0:
                all_zero = False
        if all_zero:
            cnt += 1

    # 세로줄
    for j in range(5):
        all_zero = True
        for i in range(5):
            if board[i][j] != 0:
                all_zero = False
        if all_zero:
            cnt += 1

    # 대각선 (왼쪽 위 -> 오른쪽 아래)
    all_zero = True
    for k in range(5):
        if board[k][k] != 0:
            all_zero = False
    if all_zero:
        cnt += 1

    # 대각선 (오른쪽 위 -> 왼쪽 아래)
    all_zero = True
    for k in range(5):
        if board[k][4 - k] != 0:
            all_zero = False
    if all_zero:
        cnt += 1

    return cnt

# 사회자가 부르는 순서대로 처리하면서, 빙고 줄이 3개 이상 되면 그 시점 출력한다.
answer = None
call_count = 0

for num in calls:
    call_count += 1
    mark_number(num)              # 전체 뒤져서 표시
    lines = count_bingo_lines()
    if lines >= 3:
        answer = call_count
        break



print(answer)