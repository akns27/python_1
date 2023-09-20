n = int(input())
num = input().split()

for i in range(n):
    num[i] = int(num[i])

minimum  = num[0]
for j in range(1, n):
    if num[j] < minimum:
        minimum = num[j]

print(minimum)