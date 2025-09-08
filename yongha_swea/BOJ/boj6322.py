import math

tc = 0

while True:
    tc += 1
    #a: 높이, b: 밑변, c: 빗변
    a, b, c = map(float, input().split())

    #마지막에 0,0,0으로 종료를 선언하기 때문에 그와 동시에 루프 탈출
    if a == 0 and b == 0 and c == 0:
        break
    
    #그 외 경우에는 주어지지 않은 변 (-1)의 값을 찾기
    else:
        print(f'Triangle #{tc}')

        #변 중 0이 있는 경우에는 삼각형이 성립하지 않기 때문에 예외 처리
        if a == 0 or b == 0 or c == 0:
            print("Impossible.")
            continue
        
        #a의 값이 주어지지 않은 경우 값을 찾는 과정
        elif a == -1:
            #같거나 큰 경우 모두 삼각형 성립하지 않음 유의
            if b >= c:
                print("Impossible.")
            else:
                a = math.sqrt(c ** 2 - b ** 2)
                print(f'a = {a:.3f}')
        #b의 값이 주어지지 않은 경우 값을 찾는 과정
        elif b == -1:
            #같거나 큰 경우 모두 삼각형 성립하지 않음 유의
            if a >= c:
                print("Impossible.")
            else:
                b = math.sqrt(c ** 2 - a ** 2)
                print(f'b = {b:.3f}')
        #빗변 c의 값이 주어지지 않은 경우 값을 찾는 과정
        elif c == -1:
            c = math.sqrt(a**2 + b**2)
            print(f'c = {c:.3f}')

        print()