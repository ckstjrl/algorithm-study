'''
# [Silver III] 킹 - 1063

[문제 링크](https://www.acmicpc.net/problem/1063)

### 성능 요약

메모리: 108384 KB, 시간: 104 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 10월 28일 13:33:55

### 문제 설명

<p>8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.</p>

<p>킹은 다음과 같이 움직일 수 있다.</p>

<ul>
	<li>R : 한 칸 오른쪽으로</li>
	<li>L : 한 칸 왼쪽으로</li>
	<li>B : 한 칸 아래로</li>
	<li>T : 한 칸 위로</li>
	<li>RT : 오른쪽 위 대각선으로</li>
	<li>LT : 왼쪽 위 대각선으로</li>
	<li>RB : 오른쪽 아래 대각선으로</li>
	<li>LB : 왼쪽 아래 대각선으로</li>
</ul>

<p>체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/259549ad-b275-48a1-91f7-197a7ce72a23/-/preview/"></p>

<p>입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.</p>

<p>킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.</p>

### 출력

 <p>첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.</p>

'''

import sys
input = lambda :sys.stdin.readline().rstrip()

move_dict = {
    'R':(1, 0),
    'L':(-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1),
}

king, stone, N = input().split()

king_x, stone_x = ord(king[0]) - 64, ord(stone[0]) - 64
king_y, stone_y = int(king[1]), int(stone[1])
N = int(N)

for _ in range(N):
    path = input()
    dx, dy = move_dict[path]

    new_king_x = king_x + dx
    new_king_y = king_y + dy

    if not (0 < new_king_x <= 8) or not (0 < new_king_y <= 8):
        continue

    if new_king_x == stone_x and new_king_y == stone_y:
        # 겹칠 때
        new_stone_x = stone_x + dx
        new_stone_y = stone_y + dy

        if not (0 < new_stone_x <= 8) or not (0 < new_stone_y <= 8):
            continue

        king_x, king_y = new_king_x, new_king_y
        stone_x, stone_y = new_stone_x, new_stone_y
    else:
        # 겹치지 않을 때
        king_x, king_y = new_king_x, new_king_y

king, stone = str(chr(king_x + 64)) + str(king_y), str(chr(stone_x + 64)) + str(stone_y)
print(king)
print(stone)


