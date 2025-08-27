T = int(input())
for test_case in range(1, 1+T):
    q = input()
    score = 1
    ans = 0
    for i in q:
        if i == 'O':  # O면 점수 추가하고 다음에 추가할 점수 +1
            ans = ans + score
            score = score + 1 
        else:   # x면 추가할점수 초기화
            score = 1 
    print(ans)