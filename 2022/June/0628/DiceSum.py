import numpy as np
N, M, K=map(int,input().split())
dp = np.zeros(K+1)
mod = 998244353
dp[0] = 1
for _ in range(N):
  new_dp = np.zeros_like(dp)
  dp_cum=np.cumsum(dp)
  dp_cum%=mod
  for i in range(1,K+1):
    if  i<=M:
      new_dp[i]=dp_cum[i-1]
    else:
      new_dp[i]=(dp_cum[i-1]-dp_cum[i-M-1])%mod
  dp=new_dp

print(int(sum(dp[1:]))%mod)