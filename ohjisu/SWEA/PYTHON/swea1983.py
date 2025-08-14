"""

1983. 조교의 성적 매기기 D2

학기가 끝나고, 학생들의 점수로 학점을 계산중이다.
학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.

학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영한다.
각각 아래 비율로 반영된다.

10 개의 평점을 총점이 높은 순서대로 부여하는데,
각각의 평점은 같은 비율로 부여할 수 있다.
예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성하라.


[제약사항]

1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


"""


"""
1. use dictionary
"""

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())

    test_arr = [list(map(int, input().split())) for _ in range(N)]
    result_arr = []

    for idx, item in enumerate(test_arr) :
        result_arr.append((test_arr[idx][0] * 35 +  test_arr[idx][1] * 45 +  test_arr[idx][2] * 20, idx))
    result_arr.sort(key=lambda item: item[0],reverse=True)
    
    grade_map = {
    0: 'A+',
    1: 'A0',
    2: 'A-',
    3: 'B+',
    4: 'B0',
    5: 'B-',
    6: 'C+',
    7: 'C0',
    8: 'C-',
    9: 'D0'
    }

    rank_by_idx = {}
    for rank, (score, idx) in enumerate(result_arr):
        rank_by_idx[idx] = rank

    grade = rank_by_idx[K-1] + 1
    result = grade_map[grade//10]

    
    print(f'#{tc} {result}')


"""
Use if-else
"""
T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())

    test_arr = [list(map(int, input().split())) for _ in range(N)]
    result_arr = [[0] for _ in range(N)]

    for idx in range(N) :
        result_arr[idx] = test_arr[idx][0] * 35 +  test_arr[idx][1] * 45 +  test_arr[idx][2] * 20 
    

    grade_arr = sorted(result_arr, reverse=True)
    grade = grade_arr.index(result_arr[K-1]) + 1
    if grade <= N//10 :
        result = 'A+'
    elif grade <= (N//10)*2   :
        result = 'A0'
    elif grade <= (N//10)*3 :
        result = 'A-'
    elif grade <= (N//10)*4 :
        result = 'B+'
    elif grade <= (N//10)*5 :
        result = 'B0'
    elif grade <= (N//10)*6 :
        result = 'B-'
    elif grade <= (N//10)*7 :
        result = 'C+'
    elif grade <= (N//10)*8 :
        result = 'C0'
    elif grade <= (N//10)*9 :
        result = 'C-'
    else :
        result = 'D0'
    print(f'#{tc} {result}')