# BOJ 1620. 나는야 포켓몬 마스터 이다솜 ( D2 / S4)
# ------------------------------- 2회차 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemons = ['']  # 1번부터 시작하기 위해

for i in range(N):
    pokemons.append(input().strip())

# 이름->번호 딕셔너리 컴프리헨션
name_to_num = {name: num for num, name in enumerate(pokemons) if name}

for i in range(M):
    x = input().strip()
    if x.isdecimal():
        print(pokemons[int(x)])
    else:
        print(name_to_num[x])

# ------------------------------- 1회차 풀이

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# 키값으로 찾기 위한 딕셔너리 2개 생성
# dogam_idx = {}
# dogam_name = {}

# for i in range(1, N+1):
#     name = input().strip()
#     dogam_idx[i] = name
#     dogam_name[name] = i
    
# for i in range(M): # 5문제임
#     x = input().strip()
#     if x.isdecimal():
#         print(dogam_idx[int(x)])
#     else:
#         print(dogam_name[x])