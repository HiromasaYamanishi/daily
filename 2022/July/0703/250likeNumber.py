#https://atcoder.jp/contests/abc250/tasks/abc250_d

import numpy as np
N = int(input())
M = 10**6+1
prime = np.ones(M)
prime[:2] = 0
for i in range(2, M):
  if prime[i] == 1:
    prime[2*i:M:i] = 0
    
prime_cum = np.cumsum(prime).astype(int)
ans = 0
for i in range(2,M+1):
  if i**3 > N:
    break
  else:
    if prime[i] == 1:
      div = N//(i**3)
      ans += prime_cum[min(div,i-1)]
print(ans)