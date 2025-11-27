a, b, c, d, e, f = map(int, input().split())

def solve(a, b, c, d, e, f):
    #최저 최대값 설정
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            #방정식 풀이 후 코드로 변환하여 정리
            if a*x + b*y == c and d*x + e*y == f:
                print(x, y)
                return

solve(a, b, c, d, e, f)