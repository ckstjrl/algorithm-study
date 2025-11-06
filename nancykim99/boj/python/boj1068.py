# BOJ1068. 트리
# trial 1) 트리로 풀려고 했는데, 오히려 그렇게 하면 꼬이는 느낌
# trial 2) 그냥 인접리스트 만들어서, dfs로 시도... 80%에서 실패
# trial 3) 인접리스트 없이 그냥 바로 수정하는 dfs... 이게 뭐야!


N = int(input())
arr = list(map(int, input().split()))
target = int(input())

def dfs(target):
    arr[target] = '*'
    for i in range(N):
        if arr[i] == target:
            dfs(i)

dfs(target)

cnt = 0
for i in range(N):
    if arr[i] != '*' and i not in arr:
        cnt += 1

print(cnt)