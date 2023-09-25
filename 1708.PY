n = int(input())
score = list(map(int, input().split()))

rank = [1]*n # 1로 초기화

for i in range(n):
  for j in range(n):
    if score[i] < score[j]:
      rank[i] += 1

for r in rank:
  print(score[i])
  print (r, end= " ")