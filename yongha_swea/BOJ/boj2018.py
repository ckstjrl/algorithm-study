# BOJ2018 수들의 합 5

N = int(input())

start, end = 0, 0

count = 0

sum = 0

# 끝이 N보다 커지는 순간 조건을 깨고 나가기 때문에 작거나 같은 동안
while end <= N:

    #수의 합이 주어진 N보다 작은 경우 끝을 하나씩 늘려나가기
    if sum < N:
        end += 1
        sum += end
    #수의 합이 주어진 N보다 커지는 경우 시작을 하나씩 앞으로 당겨오기
    elif sum > N:
        sum -= start
        start += 1
    #수의 합이 주어진 N과 같은 경우 count를 1늘리고, 끝을 하나 늘려서 다음 수 확인
    else:
        count += 1
        end += 1
        sum += end

print(count)