import sys
#sys.stdin = open("input.txt", 'r')
#각각 dx,dy를 (i,j)에 더하여 상하좌우를 나타낼 수 있음.(4방향 탐색)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)  #0으로만 이루어진 첫번째 행 추가
a.append([0]*n) #마지막 행에 0으로만 이루어진 배열 추가

for x in a: #각 행의 0번째 수와 마지막 수에 0을 추가
    x.insert(0, 0)  
    x.append(0)
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #4번을 반복한 조건이 모두 참일 때
            cnt+=1
print(cnt)
            
