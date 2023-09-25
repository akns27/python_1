def f(k):
  res = int(0)
  while 1: # 1은 참 -> 무한 루프, true라도 상관 X
    if k == 0:
      break
    res += (k%10)#이 코드는 10의 자리를 더하기
    k //= 10 #자리별로 조각조각 나누기, //=은 하나의 연산자로 봐야함! 
  return res 

n = int(input())
while 1:
  if(n < 10):#홀수 판별
    break
  n = f(n)
print(n)