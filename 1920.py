def f(n):
    if (n > 0):
        f(n // 2)
        print(n % 2, end="")#end=""를 쓰면서 공백제거 -> 붙여서 결과 값이 나옴

n = int(input()) 
if (n <= 0):
  print("0")
else:
    f(n)