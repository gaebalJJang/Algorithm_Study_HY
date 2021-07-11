import sys
#sys.stdin=open("input.txt", "r")
a=input() # 후위표기식
stack=[]
for x in a:
    if x.isdecimal():   # 십진수인지 확인해서 스택에 넣음. 단, int로 넣어야함.
        stack.append(int(x))
    else:   # 연산자이면
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])
