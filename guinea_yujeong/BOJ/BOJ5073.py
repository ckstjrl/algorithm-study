'''
[문제]
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
- Equilateral :  세 변의 길이가 모두 같은 경우
- Isosceles : 두 변의 길이만 같은 경우
- Scalene : 세 변의 길이가 모두 다른 경우

단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 
예를 들어 6, 3, 2가 이 경우에 해당한다. 
가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

[입력]
각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

[출력]
각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.
'''

while True:

    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:  # 종료 조건 : 모든 입력값이 0 일 때

        break

    x, y, z = sorted([a, b, c])       # 계산하기 편하기 위한 오름차순 정렬

    if x + y <= z:                    # 삼각형 조건이 아닐 경우

        print("Invalid")

    elif x == z:                      # 세 변 모두 같은 경우

        print("Equilateral")

    elif x == y or y == z:            # 두 변만 같음

        print("Isosceles")

    else:                             # 모두 다름

        print("Scalene")

