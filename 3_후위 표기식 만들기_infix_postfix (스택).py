import sys
#sys.stdin=open("input.txt", "r")
a=input()   #중위식
stack=[]
res=''  #출력
for x in a: #x가 중위식 탐색
    if x.isdecimal():   # x가 십진수인지 확인하는 함수 사용. 십진수면 참임.
        res+=x
    else:   # 연산자이면
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':  # 연산 우선순위 같음
            while stack and (stack[-1]=='*' or stack[-1]=='/'): #이미 들어간(우선순위 빠름) *,/ 꺼냄
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': #더하기 빼기는 무조건 스택에 있는 자료가 자기보다 빠르므로 '('괄호 전까지 연산자 빼냄.
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(': #닫는 괄호는 여는 괄호까지 연산자를 처리함
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
