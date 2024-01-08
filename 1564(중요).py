def f(a,b):
    while(b!=0):
      a, b = b, a%b
    return a#return 은 함수 안에서만
"""
while(a%b!=0):
...
return b
로도 풀 수 있음
"""
a, b = map(int, input().split())
print(f(a,b))

"""
선생님의 코드
a,b = map(int, input().split())
def f(a,b):
  if a%b == 0:
    return b
  return f(b,a%b)
  
print(f(a,b))
"""