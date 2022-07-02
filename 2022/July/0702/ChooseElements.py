#https://atcoder.jp/contests/abc245/tasks/abc245_c
import numpy as np
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[[0 for i in range(2)] for j in range(N)]
dp[0][0]=1
dp[0][1]=1


for i in range(1,N):
  if ((dp[i-1][0]==1) and (abs(A[i]-A[i-1])<=K)) or ((dp[i-1][1]==1) and (abs(A[i]-B[i-1])<=K)):
    dp[i][0]=1
  if ((dp[i-1][0]==1) and (abs(B[i]-A[i-1])<=K)) or ((dp[i-1][1]==1) and (abs(B[i]-B[i-1])<=K)):
    dp[i][1]=1

if sum(dp[-1])>0:
  print('Yes')
else:
  print('No')