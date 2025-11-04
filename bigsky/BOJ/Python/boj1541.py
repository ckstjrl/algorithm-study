# BOJ1541: 잃어버린 괄호
calc = input().split('-')  # - 기준으로 나눈 다음
parts = []  # 각 파트를 더해서 정수로 저장
for part in calc:
    parts.append(sum(map(int, part.split('+'))))

result = parts[0]
for part in parts[1:]:
    result -= part

print(result)