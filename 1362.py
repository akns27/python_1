n = int(input())
num = 0
for i in range(1, n+1):#1~n까지의 합
  for i in range(1, i+1):
    num += 1

for i in range(1, n+1):
  for j in range(1, i+1):
    print(num, end = " ")
    num -= 1
  print()
  # 재귀로도 풀었으면...