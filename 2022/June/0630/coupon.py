N,K,X=map(int,input().split())
A=list(map(int,input().split()))
div=[a//X for a in A]
mod=[a%X for a in A]
ans=sum(A)
if sum(div)>=K:
  print(ans-X*K)
  
else:
  mod=sorted(mod)[::-1]
  print(ans-sum(div)*X-sum(mod[:min(K-sum(div),len(mod))]))