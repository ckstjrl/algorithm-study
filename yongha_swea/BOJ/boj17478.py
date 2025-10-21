#BOJ17478 재귀함수가 뭔가요?

def recursion(run, depth):
    indent = '____' * depth

    print(f'{indent}"재귀함수가 뭔가요?"')

    if run == 0:
        print(f'{indent}"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(f'{indent}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
        #원하는 반복 횟수 만큼 돌리기 위해 매 재귀마다 input 숫자(run)는 1씩 빼고, 앞쪽에 있는 indentation은 늘려준다 ('____') 
        recursion(run-1, depth+1)
    
    #위쪽에 재귀가 돌아간 이후에 빠져나오며 출력될수 있도록 해당 줄 추가
    print(f'{indent}라고 답변하였지.')

run = int(input())

#재귀의 영향을 받지 않고 딱 한 번만 출력되는 문구
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursion(run, 0)