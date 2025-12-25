# 5073. 삼각형과 세 변
'''
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력
가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

[입력]
마지막 줄은 0 0 0 -> 계산하지 않음

[출력]
입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력

a, b, c가 같으면 Equilateral
a, b, c 중 두 변만 같으면 Isosceles
a, b, c 모두 다르면 Scalene
삼각형 조건 만족하지 못하면 Invalid
먼저 while문에서 0 0 0이 나오면 멈추게 하자.
그 다음에 각 식 구현.
'''
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or a == c or b == c:
            print('Isosceles')
        else:
            print('Scalene')