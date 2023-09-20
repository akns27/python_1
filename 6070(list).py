a = int(input())
b = ['winter','spring', 'summer', 'fall']


if a//4 == 2: #//는 나눗셈 소수점 떼고 정수 부분만
    print(b[3])
    
elif a//3 == 1:
    print(b[1])
    
elif a//6 == 1:
    print(b[2])
    
else :
    print(b[0])
"""
  12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""