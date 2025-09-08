# 6322. 직각 삼각형의 두 변
'''
세 변의 길이가 a, b, c(c는 빗변)이면서 a**2+b**2=c**2를 만족하는 삼각형을 직각삼각형이라고 한다.
이 공식은 피타고라스의 법칙이라고 한다.
직각 삼각형의 두 변의 길이가 주어졌을 때, 한 변의 길이를 구하는 프로그램을 작성하시오.

tc가 안 나왔으니까 while문 돌면서 계산.
a, b, c = 0, 0, 0일 경우 -> while문 종료
a, b, c 가 -1일 경우 나눠서 계산.
'''
tc = 1

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:    # 종료조건
        break
    print(f'Triangle #{tc}')

    if a == -1:
        if c <= b:
            print("Impossible.")
        else:
            a = (c ** 2 - b ** 2) ** 0.5
            print(f"a = {a:.3f}")
    elif b == -1:
        if c <= a:
            print("Impossible.")
        else:
            b = (c ** 2 - a ** 2) ** 0.5
            print(f"b = {b:.3f}")
    elif c == -1:
        c = (a ** 2 + b ** 2) ** 0.5
        print(f"c = {c:.3f}")
    else:
        print("Impossible.")
    print()     # 출력형식 맞추기
    tc += 1