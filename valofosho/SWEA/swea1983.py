# 총점 = 중간 35 + 기말 45 + 과제 20
# 학점 = A+, A0, A-, B+, B0, B-, C+, C0, C-, D0
T = int(input())
for test_case in range(1, T+1):
    N, K= map(int, input().split())
    # 학점 리스트
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    students = []
    # students 리스트에 총점 입력
    for i in range(N):
        mid, final, asm = map(int, input().split())
        student = mid * 0.35 + final * 0.45 + asm * 0.2
        students.append(student)
    # 점수가 높은 순서대로 SORTED LIST 생성
    rev = sorted(students,reverse=True)
    # 원하는 학생 점수는 score
    score = students[K-1] # 학생 점수
    # 높은 순서의 리스트
    num = rev.index(score)
    # 학점은 총 N//10 
    grade_1 = N//10
    # 등수를 다시 grade_1으로 나누면 된다
    grade = grades[num//grade_1]
    print(rev, score, num, grade_1, grade)
    print(f"#{test_case} {grade}")