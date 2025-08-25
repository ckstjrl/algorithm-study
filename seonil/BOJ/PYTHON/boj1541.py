def min_value(expr):
    # '-' 기준으로 합 덩어리들을 나누기
    parts = expr.split('-')
    # print(parts)

    # 첫 번째 합 덩어리는 그냥 더하기
    first_sum = sum(map(int, parts[0].split('+')))

    # 나머지 합 덩어리들은 모두 더해서 빼기
    rest_sum = 0
    for part in parts[1:]:
        rest_sum += sum(map(int, part.split('+')))

    return first_sum - rest_sum

expr = input()
print(min_value(expr))