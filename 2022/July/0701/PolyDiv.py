#https://atcoder.jp/contests/abc245/tasks/abc245_d

import numpy as np
N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
A=np.array(A[::-1])
C=np.array(C[::-1])
B=list(np.polydiv(C,A)[0].astype(int))[::-1]
print(*B)