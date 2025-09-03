'''
백준 6322 문제 : 직각 삼각형의 두 변

내용
컴퓨터를 이용하면 수학 계산이 조금 쉬워진다. 다음과 같은 예를 살펴보자.
세 변의 길이가 a, b, c(c는 빗변)이면서 a2+b2=c2를 만족하는 삼각형을 직각삼각형이라고 한다.
이 공식은 피타고라스의 법칙이라고 한다.

직각 삼각형의 두 변의 길이가 주어졌을 때, 한 변의 길이를 구하는 프로그램을 작성하시오.
'''


cnt = 0         # 삼각형 번호를 매기기 위한 카운터 변수 cnt를 0으로 초기화
while True:
    cnt += 1
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if cnt > 1:
        print()
    if c == -1:
        print(f"Triangle #{cnt}")
        print("c = %.3f" % ((a**2+b**2)**0.5))
    elif max(a, b) >= c:
        print(f"Triangle #{cnt}")
        print('Impossible.')
    elif a == -1:
        print(f"Triangle #{cnt}")
        print("a = %.3f" % ((c**2-b**2)**0.5))
    elif b == -1:
        print(f"Triangle #{cnt}")
        print("b = %.3f" % ((c**2-a**2)**0.5))

    '''
    memo 
    지피티야 고마워
    '''