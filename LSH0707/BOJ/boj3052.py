arr = set()
for _ in range(10):  # 입력값 각각 42로 나눈 나머지 세트에 add하고 len 출력
    a = int(input())
    arr.add(a % 42)
print(len(arr))  