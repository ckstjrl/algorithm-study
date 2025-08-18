T = int(input())
for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    avg_score = [[],[]] # [학생번호],[점수]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):  # arr = [[학생번호] [총점]]
        avg = 0.35 * arr[i][0] + 0.45 * arr[i][1] + 0.2 * arr[i][2]
        avg_score[0].append(i+1)
        avg_score[1].append(avg)
 
    for i in range(N-1, 0, -1):
        for j in range(i):  # arr 내림차순 정렬
            if avg_score[1][j] < avg_score[1][j+1]:
                avg_score[0][j], avg_score[0][j + 1] = avg_score[0][j + 1], avg_score[0][j]
                avg_score[1][j], avg_score[1][j+1] = avg_score[1][j+1], avg_score[1][j]
 
    for i in range(N):
        if avg_score[0][i] == K:
            rank = i   # K번 학생의 등수 인덱스 = rank
 
    grade_s = grade[int((rank/N)*10)]  # int(등수/인원수)*10 -> 0 1 2 ...
    print(f'#{test_case} {grade_s}')