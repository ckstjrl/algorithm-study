T = int(input())

#run time error를 막기 위해 계속 제곱을 하는 대신 미리 패턴 정리하기
pattern_dict = {
    0 : [0],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1],
}

for tc in range(T):
    a, b = map(int, input().split())

    #99까지 나올 수 있기 때문에 10으로 나눠주기 그러면 한자리 수가 된다
    a = a % 10 

    pattern_len = len(pattern_dict[a])

    #0이라서 1을 빼줘야 하는 점 유의
    result = pattern_dict[a][((b - 1) % pattern_len)]

    # 예외 케이스로 0인 경우에는 10번 컴퓨터에 할당되는 점 따로 명시
    if result == 0:
        result = 10
    
    print(result)