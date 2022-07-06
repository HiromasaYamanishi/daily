#https://atcoder.jp/contests/abc241/tasks/abc241_a
A=list(map(int,input().split()))
ans=0
for _ in range(3):
  ans=A[ans]
  
print(ans)