def func(k):
    if k==0:
      return  
    else:
        print(k)
        func(k-1)
        
      

k=int(input())
func(k)