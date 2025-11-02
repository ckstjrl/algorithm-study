# 2160. 그림 비교
'''
각각의 그림은 5×7의 크기이고, 두 가지 색으로 되어 있다.
이때 두 가지의 색을 각각 ‘X’와 ‘.’으로 표현하기로 하자.
이러한 그림들이 주어졌을 때, 가장 비슷한 두 개의 그림을 찾아내는 프로그램을 작성하시오.

[입력]
첫째 줄에 N이 주어진다.
다음 5×N개의 줄에 7개의 문자로 각각의 그림이 주어진다.

[출력]
첫째 줄에 가장 비슷한 두 그림의 번호를 출력한다.
그림의 번호는 입력되는 순서대로 1, 2, …, N이다.
번호를 출력할 때에는 작은 것을 먼저 출력한다.
입력은 항상 답이 한 가지인 경우만 주어진다.

for문 안에서 돌면서 다른 칸의 갯수 찾기.
다른 칸의 갯수가 가장 적은 번호 뽑기.
'''
n = int(input())
total = []
for i in range(n):
    arr = []
    for _ in range(5):
        arr.append(input())
    total.append(arr)
min_val = 21e8
result = (0, 0)
for i in range(1, n+1):
    for j in range(i+1, n+1):
        diff = 0
        for r in range(5):
            for c in range(7):
                if total[i-1][r][c] != total[j-1][r][c]:
                    diff += 1
        if diff < min_val:
            min_val = diff
            result = (i, j)
print(result[0], result[1])