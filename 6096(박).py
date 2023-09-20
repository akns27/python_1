d = []
for i in range(20):
  d.append([])
  for j in range(20):
    d[i].append(0)#여기까지 칸을 만들어 주는 코드

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])#각 칸에 스플릿으로 0과 1을 입력받는 코드

n = int(input())
for i in range(n) :
  x,y=input().split()
  for j in range(1, 20) :
    if d[j][int(y)]==0 :
      d[j][int(y)]=1
    else :
      d[j][int(y)]=0

    if d[int(x)][j]==0 :
      d[int(x)][j]=1
    else :
      d[int(x)][j]=0 # 0과 1을 바꾸는 코드

for x in range(20) :
    for y in range(20) :
        print(d[x][y], end = ' ')#출력하는 코드
    print( )
        