# 1983. 조교의 성적 매기기 (D2)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    grade_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 학점

    total_score = [0] * N

    for i in range(N):
        m, f, h = map(int, input().split())
        total_score[i] = 0.35*m + 0.45*f + 0.2*h    # 입력 받는대로 총 점수 계산

    sorted_score = sorted(total_score, reverse=True)    # 총 점수를 내림차순으로 정렬

    for j in range(N):
        if total_score[K-1] == sorted_score[j]:    # K번째 학생의 점수와 성적순 리스트의 점수가 같다면 인덱스(등수) 저장
            rank = j
            break

    grade = grade_lst[rank//(N//10)]    # 등수에서 각 학점별 받을 수 있는 학생수로 나눔

    print(f'#{tc} {grade}')