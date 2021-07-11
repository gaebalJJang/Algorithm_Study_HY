import sys
#sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
num=list(map(int, str(num)))    #str(num)이어야 숫자 하나씩 각각 접근할 수 있다.
stack=[]
#앞쪽 수가 자기 자신보다 작으면 지우고 자신이 가장 앞으로 간다=자료구조 스택(LIFO)
#리스트를 이용함.pop()
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
    
#m을 다 못 지웠을 때
if m!=0:
    stack=stack[:-m]
for x in stack :
    print(x, end='')
