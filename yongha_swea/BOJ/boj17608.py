# BOJ17608 막대기

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 끝이 첫번째가 되기 때문에 리스트 뒤집어주기
arr_reverse = list(reversed(arr))

standard = arr_reverse[0]

count = 0

# 첫번째는 항상 보이는 기둥이기 때문에 해당 기둥보다 큰 기둥을 만나는 경우 기준의 값을 변경하고 카운팅 +1
for i in arr_reverse:
    if i > standard:
        count += 1
        standard = i

# 마지막에 자기 자신 추가해주기
print(count + 1)