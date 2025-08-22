# 주어진 숫자부터 0까지 순서대로 찍어보세요
# 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

N = int(input())
nums = []
for n in range(N+1):
    nums.append(n)

for i in range(len(nums)):

    for j in range(0, n-i):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(*nums)