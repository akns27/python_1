def func(k):
    if k==0:
      return  
    else:
      func(k-1)
      print(k)

k=int(input())
func(k)