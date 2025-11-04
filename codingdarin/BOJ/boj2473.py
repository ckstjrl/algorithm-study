# BOJ 2473. 세 용액 (G3 / D3)
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_sum = float('inf')
result = []

for i in range(n - 2):
    left = i + 1
    right = n - 1
    
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = [arr[i], arr[left], arr[right]]
        
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            print(*result)
            exit()

print(*result)