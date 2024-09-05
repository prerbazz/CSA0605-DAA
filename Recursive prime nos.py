def prime(n):
  l=[]
  for i in range(1,n):
    p=True
    for j in range(2,i):
      if i%j==0:
        p=False
    if p:
      l.append(i)
  for i in l:
    print(i,end=" ")
n=int(input())
prime(n)
