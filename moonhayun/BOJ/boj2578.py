"""
[문제]
빙고 게임은 다음과 같은 방식으로 이루어진다.
먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다.

차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.
철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
"""
import sys
input = sys.stdin.readline

B = [list(map(int, input().split())) for _ in range(5)] # 빙고판
bingo = [[0]*5 for _ in range(5)] # 사회자가 부른거 기록하기

sa = [list(map(int, input().split())) for _ in range(5)] # 사회자
answer = 0

done = False

for i in range(5):
    if done: break
    for j in range(5):
        num = sa[i][j]
        answer += 1
        for p in range(5):
            for q in range(5):
                if num == B[p][q]:
                    bingo[p][q] = 1
        check = 0
# print(bingo)
        for p in range(5):
            if sum(bingo[p]) == 5:
                check += 1
        # 세로줄
        for q in range(5):
            if sum(bingo[r][q] for r in range(5)) == 5:
                check += 1
        # 대각선 2개
        if sum(bingo[d][d] for d in range(5)) == 5:
            check += 1
        if sum(bingo[d][4-d] for d in range(5)) == 5:
            check += 1
        if  check >= 3:
            print(answer)
            done = True
            break