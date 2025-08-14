# 1983. 조교의 성적 매기기 / D2
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = (arr[K-1][0] * 35 + arr[K-1][1] * 45 + arr[K-1][2] * 20) / 100 # k의 점수 미리 파악
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    score_list = [0] * N
    for i in range(N): # 점수 계산하여 넣기
        score = (arr[i][0] * 35 + arr[i][1] * 45 + arr[i][2] * 20) / 100
        score_list[i] = score

    for s in range(N-1, 0, -1): # sort 진행
        for j in range(s):
            if score_list[j] < score_list[j + 1]:
                score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j]

    rank_k = score_list.index(k) # k의 등수 찾기
    a = N//10 # 한 학점당 받을 수 있는 인원 계산하기
    for g in range(10): # k의 학점이 무엇인지 등수의 위치로 파악하기
        if a * g <= rank_k < a * (g+1) :
           grade_k = grade[g]

    print(f'#{tc} {grade_k}')