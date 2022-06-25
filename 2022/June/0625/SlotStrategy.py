N=int(input())
S=[str(input()) for _ in range(N)]
where = [[] for _ in range(10)]
for s in S:
  for i,c in enumerate(s):
    where[int(c)].append(i)

for i in range(10):
	where[i].sort()
    
for wh in where:
  for i,w in enumerate(wh):
    if i==0:
      pre=w
    else:
      if w%10==pre%10:
        pre=pre+10
        wh[i]=pre
      else:
      	pre=w
      
ans=1e9
for wh in where:
  ans = min(ans, max(wh))
  
print(ans)