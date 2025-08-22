T = int(input())  # 테스트 케이스 개수 입력

# 10개의 학점 순서 (내림차순)
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N: 학생 수, K: 학점을 알고 싶은 학생 번호(1~N)

    scores = []  # (총점, 학생 번호) 형태로 저장할 리스트

    for student_num in range(1, N + 1):
        mid, final, assignment = map(int, input().split())
        # 총점 계산 (비율: 중간 35%, 기말 45%, 과제 20%)
        total = mid * 0.35 + final * 0.45 + assignment * 0.20
        scores.append((total, student_num))

    # 총점을 기준으로 내림차순 정렬
    scores.sort(key=lambda x: x[0], reverse=True)

    # 각 학점이 몇 명에게 주어지는지 (N은 10의 배수이므로 N/10)
    students_per_grade = N // 10

    # 학점 부여: 순위별로 grades에서 선택
    student_grade_map = {}  # {학생 번호: 학점}
    for idx, (total, student_num) in enumerate(scores):
        grade_idx = idx // students_per_grade  # 몇 번째 학점 그룹인지
        student_grade_map[student_num] = grades[grade_idx]

    # K번째 학생의 학점 출력
    print(f"#{test_case} {student_grade_map[K]}")