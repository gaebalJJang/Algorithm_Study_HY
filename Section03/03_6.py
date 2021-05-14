import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
maximum = -2147000000
for i in range(n):  #각 행의 합, 각 열의 합
    sum1 = sum2 =0
    for j in range(n):
        sum1+=a[i][j]   #행(가로의 합)
        sum2+=a[j][i]   #열(세로의 합)
    if sum1>maximum:
        maximum = sum1
    if sum2>maximum:
        maximum = sum2
sum1=sum2=0
for i in range(n):  # 대각선의 합
    sum1+= a[i][i]
    sum2+= a[i][n-i-1]
if sum1 > maximum:
    maximum = sum1
if sum2 > maximum:
    maximum = sum2
print(maximum)
