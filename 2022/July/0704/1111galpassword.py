#https://atcoder.jp/contests/abc242/tasks/abc242_c
N = int(input())
dp=[1]*9
mod=998244353
for i in range(N-1):
    new_dp=[0]*9
    for j in range(9):
        if j==0:
            new_dp[j]=(dp[j]+dp[j+1])%mod
        elif j==8:
            new_dp[j]=(dp[j-1]+dp[j])%mod

        else:
            new_dp[j]=(dp[j-1]+dp[j]+dp[j+1])%mod
    dp=new_dp

print(sum(dp))