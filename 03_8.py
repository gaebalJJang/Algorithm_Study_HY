import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if (t == 0):
        for _ in range(k):  #k번 반복함
            a[h-1].append(a[h-1].pop(0))    #(큐) 0번째 수를 뺀 후 리스트 맨끝에 추가(append())
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) #(스택) 리스트의 맨끝에 수를 빼서 맨 앞에 추가(insert(0,))

res = 0
s = 0
e = n-1
for i in range(n):  #모래시계 모양으로 출력(03_7참고)
    for j in range(s,e+1):
        res += a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
