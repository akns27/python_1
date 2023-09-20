def f(a, b):
    if(a%2==0):
      a+=1
    if (a <= b):
      print(a)
      f(a + 2, b)#다음 홀수 ~ b까지

a,b = map(int, input().split())
f(a, b)