n = int(input())

arr = list(map(int, input().split()))

key = int(input())

answer = 0

#리스트를 생각했지만, 다른 풀이를 보고 효율과 중복 방지를 위해 set채택
used = set()

for num in arr:
    #조합 = 목표 - 현 숫자
    comb = key - num
    # 생각을 못 했던 부분인데 꼭 앞에 수를 먼저 넣을 필요 없다. 
    # 먼저 있는 수를 다른 곳에 둔 뒤 새로 꺼낸 수가 앞에 나온 수와 조합하여 목표값이 나오는지 확인하는 방식을 채택하였다.
    if comb in used:
        answer += 1
    used.add(num)

print(answer)