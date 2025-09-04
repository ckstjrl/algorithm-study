#boj1152: 단어의 개수

#공백을 기준으로 각 단어를 별개의 아이템으로 저장하기
arr = list(input().split())

count = 0

#아이템 하나마다 count + 1
for i in range(len(arr)):
    count += 1

#count값 출력
print(count)