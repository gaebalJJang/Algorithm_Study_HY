import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):  #격자의 가운데 수확
        res += a[i][j]
    if i < n//2:    #격자 중앙을 기준으로 양 옆 한칸씩
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
    
        
        
        
