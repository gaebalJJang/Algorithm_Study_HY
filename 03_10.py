import sys
#sys.stdin=open("input.txt", "r")
def check(tmp): #체크리스트의 합이 9이면 스토쿠이고 아니면 잘못된 것.
    for i in range(9):
        ch1=[0]*10  #행 체크
        ch2=[0]*10  #열 체크
        for j in range(9):  #행,열을 탐색
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:  #행,열을 탐색한 결과 
            return False
    for i in range(3):  #9개의 그룹
        for j in range(3):
            ch3=[0]*10
            for k in range(3):  #나눈 그룹 안의 9개의 숫자
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False    #리턴하면 함수 종료
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
