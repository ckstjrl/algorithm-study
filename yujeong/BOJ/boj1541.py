# 1541. 잃어버린 괄호

exp = input()

e1 = exp.split('-')     # '-'를 기준으로 수식 split
nums = []

for e in e1:            
    e2 = e.split('+')   # 그걸 다시 '+'를 기준으로 split하면 나눠진 부분들은 숫자
    temp = 0
    for x in e2:
        temp += int(x)  # 그 숫자들 합을 리스트에 담기
    nums.append(temp)

ans = nums[0]           # 리스트 길이가 1 = 수식에 '-' 없었음 = 이대로 결과

if len(nums) > 1:       # 리스트 길이가 1 초과 = 수식에 '-' 있었음
    for n in nums[1:]:  # => 리스트에 있는 요소들 차례로
        ans -= n        # '-' 적용하기 (차 구하기 )

print(ans)