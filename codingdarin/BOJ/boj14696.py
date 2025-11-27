# BOJ14696. 딱지놀이 (D1 / B1)

n = int(input()) # 라운드 수

# 재귀함수 구현
def compare(n):
    if n == 0:
        print('D')
        return
    
    if a.count(n) > b.count(n):
        print('A')

    elif a.count(n) < b.count(n):
        print('B')
    
    else:
        compare(n-1)


# 각 라운드마다
for _ in range(n):
    a = list(map(int, input().split()))
    a.pop(0)    # 필요 없어서 빼주기
    
    b = list(map(int, input().split()))
    b.pop(0)    # 222

    # 답 찾기
    compare(4)

