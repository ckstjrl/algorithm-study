#BOJ14659 한조서열정리하고옴ㅋㅋ

#한조 수
N = int(input())

arr = list(map(int, input().split()))

winner = -1

catch = []

kill = 0
max_kill = 0

#arr에서 자기보다 낮은 쪽은 연속 처치가 가능하기 때문에 작거나 같은 경우는 모두 다른 리스트에 저장해준다
#이후 해당 한조가 처치당하는 순간에 다른 리스트에 저장해놨던 처치한 한조의 수를 모두 추가해주고 킬 카운트 초기화
for bowman in arr:
    if bowman > winner:
        winner = bowman
        while catch:
            catch.pop()
            kill += 1
        if kill > max_kill:
            max_kill = kill
            kill = 0
        else:
            kill = 0
    else:
        catch.append(bowman)

#마지막에 다른 리스트에 남아있는 한조의 기록을 모두 추가해주고 위와 동일하게 킬 카운트가 최대인 경우에는 대체 아닌 경우에는 계속 진행
if catch:
    while catch:
        catch.pop()
        kill += 1
    if kill > max_kill:
        max_kill = kill
        kill = 0
    else:
        kill = 0

#최고 연속 킬 카운트 출력
print(max_kill)

