"""
BOJ2447 - 별찍기 -10

문제 정의
1. 재귀 패턴으로 별찍기
2. N은 3의 거듭제곱(3, 9, 27 ...)
3. [[(r,c), (r,c+1), (r,c+2)],
    [(r+1,c), (r+1,c+1), (r+1,c+2)],
    [(r+2,c), (r+2,c+1), (r+2,c+2)]]
    --> x[r+1,c+1] = ' ' 나머지는 '*'


로직 정의
1. 우선 큰 범위 부터 채워나가는게 아니라 작은 범위를 채우고 바깥을 채우는게 맞을까?

"""

"""
N = 3(k=1)
[***]
[* *]
[***]

N = 9(k=2)
[*********]0
[* ** ** *]1
[*********]2
[***   ***]3
[* *   * *]4
[***   ***]5
[*********]6
[* ** ** *]7
[*********]8

N=27(k=3)
[***************************]0
[* ** ** ** ** ** ** ** ** *]1
[***************************]2
[***   ******   ******   ***]3
[* *   * ** *   * ** *   * *]4
[***   ******   ******   ***]5
[***************************]6
[* ** ** ** ** ** ** ** ** *]7
[***************************]8
[*********         *********]9
[* ** ** *         * ** ** *]10
[*********         *********]11
[***   ***         ***   ***]12
[* *   * *         * *   * *]13
[***   ***         ***   ***]14
[*********         *********]15
[* ** ** *         * ** ** *]16
[*********         *********]17
[***************************]18
[* ** ** ** ** ** ** ** ** *]19
[***************************]20
[***   ******   ******   ***]21
[* *   * ** *   * ** *   * *]22
[***   ******   ******   ***]23
[***************************]24
[* ** ** ** ** ** ** ** ** *]25
[***************************]26
규칙은 row = 3n+1 일때 변화
row = k*(3n+1)

k = 3
1 = 3 * 0 + 1
7 = 3 * 2 + 1
19 = 3 * 6 + 1
25 = 3 * 8 + 1

1 7 19 25 
0 2 6 8 18 20 24 26
"""



import sys, itertools as it

BASE = ("***", "* *", "***")

def recur(ans, k, cnt):
    size = 3 ** cnt
    # ans를 독립 이터레이터 3개로 복제 (소비 충돌 방지)
    a1, a2, a3 = it.tee(ans, 3)

    top    = (row * 3 for row in a1)
    middle = (row + (' ' * size) + row for row in a2)
    bottom = (row * 3 for row in a3)

    merged = it.chain(top, middle, bottom)
    cnt += 1
    if cnt < k:
        return recur(merged, k, cnt)
    return merged

# 사용 예시
N = int(sys.stdin.readline())
# 3의 거듭제곱 단계 k 계산
k = int(N**(1/3)) # 3 루트로 씌워주기


ans = BASE
out = sys.stdout.write
if k == 1:
    out('\n'.join(ans) + '\n')
else:
    for line in recur(ans, k, 1):
        out(line + '\n')





# from pprint import pprint
# def recur(ans, k, cnt):    
#     num_blank = [' '*(3**(cnt-1))]
#     ans = [[''.join(x)*3 for x in ans], [''.join(x)*3 for x in ans] + num_blank*3 + [''.join(x)*3 for x in ans], [''.join(x)*3 for x in ans]]
#     cnt += 1
#     if cnt != k:
#         recur(ans, k, cnt)
#     return ans    
# N = int(input())
# k = int(N**(1/3))
# print(k)

# ans = [
#         ['*','*','*'],
#         ['*',' ','*'],
#         ['*','*','*']
#         ]
# # pprint([x*3 for x in ans])
# if k == 1:
#     print(ans)
# else:
#     ans = recur(ans,k,1)
#     pprint(ans)




# def recur(ans, k, cnt):
#     size = 3 ** cnt
#     # 각 부분(위, 중간, 아래) 구성
#     top = [row * 3 for row in ans]
#     middle = [row + ' ' * size + row for row in ans]
#     bottom = [row * 3 for row in ans]

#     ans = top + middle + bottom
#     cnt += 1

#     if cnt < k:
#         return recur(ans, k, cnt)
#     return ans


# # 입력 처리
# N = int(input())
# k = int(N**(1/3)) # 3 루트로 씌워주기

# # 기본 패턴
# ans = [
#     '***',
#     '* *',
#     '***'
# ]

# if k == 1:
#     print('\n'.join(ans))
# else:
#     ans = recur(ans, k, 1)
#     print('\n'.join(ans))

