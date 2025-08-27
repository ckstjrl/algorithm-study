# 8958. OX퀴즈
'''
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성

cnt = 연속된 O 개수
score = 총 점수
'''
T = int(input())

for tc in range(T):
    arr = list(input())
    cnt = 0     # 연속된 O 개수
    score = 0   # 총 점수
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)