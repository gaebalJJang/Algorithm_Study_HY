import sys
#sys.stdin=open("input.txt", "r")
s=input()
stack=[]
cnt=0
for i in range(len(s)): #괄호 표현 탐색
    if s[i]=='(':   #여는 괄호인지 
        stack.append(s[i])
    else:   #닫는 괄호
        stack.pop()
        if s[i-1]=='(': #바로 앞에 여는 괄호가 있는지 
            cnt+=len(stack) #쇠막대기 개수에 누적
        else:   #닫는 괄호 쇠막대기 끝
            cnt+=1
print(cnt)
