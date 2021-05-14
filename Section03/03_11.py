import sys
#sys.stdin=open("input.txt", "r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):  #i가 3일 때는 5칸을 가지 못함. 따라서 i=0,1,2
    for j in range(7):
        tmp=board[j][i:i+5] #i를 0~4까지 슬라이스함. 행으로 탐색
        if tmp==tmp[::-1]:  #회문(역순과 같을 때)
            cnt+=1
        for k in range(2):  #03_1참고
            if board[i+k][j]!=board[i+5-k-1][j]:    #리스트[i][j]의 [0][0]과 [4][0]을 비교, [1][0]과 [3][0]을 비
                break;
        else:
            cnt+=1
print(cnt)
