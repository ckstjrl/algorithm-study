# BOJ1620. 나는야 포켓몬 마스터 이다솜
# 해시로 풀어보기...

N, M = map(int, input().split())

pokemon_num = {}
pokemon_name = {}

for i in range(1, N+1):
    name = input()
    pokemon_num[i] = name
    pokemon_name[name] = i

for _ in range(M):
    question = input()
    if question.isdigit():
        print(pokemon_num[int(question)])
    else:
        print(pokemon_name[question])
