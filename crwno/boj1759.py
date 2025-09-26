L, C = map(int, input().split())
alphabet = input().split()
a = [0, 4, 8, 14, 20]
nums = []

for i in range(C):
    nums.append(ord(alphabet[i]) - 97)
nums.sort()
visited = [0] * 26
ans = []


def pick(n, k, cnt):

    if n == L and 0 < cnt < L - 1:
        print(''.join(ans))

    for i in range(C):
        if visited[nums[i]] == 0:
            visited[k:nums[i] + 1] = [1 for _ in range(nums[i] + 1 - k)]
            ans.append(chr(nums[i] + 97))
            if nums[i] in a:
                pick(n + 1, nums[i], cnt + 1)
            else:
                pick(n + 1, nums[i], cnt)
            visited[k:nums[i] + 1] = [0 for _ in range(nums[i] + 1 - k)]
            ans.pop()


pick(0, 0, 0)