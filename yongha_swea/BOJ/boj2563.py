#BOJ2563 색종이

papers = int(input())

# 100 * 100 타일을 깐다는 생각으로 리스트 생성
whole_paper = [[0] * 100 for _ in range(100)]

# 색종이를 여러장에 걸쳐서 입력 받는다
for _ in range(papers):
    
    left, bot = map(int, input().split())

    right = left + 10

    top = bot + 10
    
    # 왼쪽에서 오른쪽까지 선회 (+10)
    for x in range(left, right):
        #아래에서 위까지 선회 (+10)
        for y in range(bot, top):
            if x >= 100 or y >= 100:
                break
            whole_paper[x][y] = 1
            
sum = 0

#이후에 전체를 다시 순회하며 칠해진 부분을 1씩 더한다
for i in range(100):
    for j in range(100):
        sum += whole_paper[i][j]

print(sum)
