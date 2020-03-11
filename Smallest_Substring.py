from collections import defaultdict as d
n=d()
input=list(input())
count=0
for i in input:
  if i not in n:
    count+=1
    n.setdefault(i,count)
  elif i in n:
    n[i]=count
print(min(n.items())[1])
