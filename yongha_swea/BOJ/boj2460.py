people = [list(map(int, input().split())) for _ in range(10)]

count = 0

max_count = 0

counter = 1

for i in range(len(people)):
    for j in range(len(people[i])):
        #짝수는 탄 사람
        #홀수는 내린 사람, 매 회마다 counter에 1씩 더해서 타는지 내리는지 구분

        if counter % 2 == 0:
            counter += 1
            count = count + people[i][j]

            if count >= max_count:
                max_count = count
                
            continue
        
        if counter % 2 == 1:
            counter += 1

            count = count - people[i][j]

            if count >= max_count:
                max_count = count

            continue

print(max_count)