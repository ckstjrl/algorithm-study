#boj1620 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

# 숫자에서 이름 딕트
num_to_name = {}

# 이름에서 숫자 딕트
name_to_num = {}

for i in range(1, N+1):
    name = input().strip()
    num_to_name[i] = name
    name_to_num[name] = i

# 이후 들어오는 질문에 따라서 줄 값 결정
for _ in range(M):
    question = input().strip()
    
    #숫자인지 가치 판단
    if question.isdigit():
        print(num_to_name[int(question)])
    #그 외 (이름이라면)
    else:
        print(name_to_num[question])