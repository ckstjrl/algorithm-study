# 1983. 조교의 성적 매기기 / D2

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())    # 학생수 N은 항상 10의 배수 
    scores = []
    target = 0

    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    # 총점 계산 
    for i in range(N):
        mid, fin, hw = map(int, input().split())
        total = 0.35*mid + 0.45*fin + 0.2*hw
        if i == K-1:
            target = total      # K번째 학생의 점수는 별도로 기록 
        scores.append(total)
    
    # 내림차순으로 점수 정렬 
    for i in range(N-1, -1, -1):
        for j in range(i):
            if scores[j] < scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]

    # K번째 학생의 학점 찾기 
    k_grade = grades[(scores.index(target)) // (N//10)]
    
    print(f'#{tc+1} {k_grade}')
