x,a,d,n=map(int,input().split())
if d==0:
  print(abs(a-x))
  exit()
last=a+(n-1)*d
ans=min(abs(a-x),abs(last-x))
y=a+(x-a)//d*d
for i in range(-2,3):
  z= y+i*d
  if a<=z<=last or last<=z<=a:
    ans=min(ans,abs(z-x))
print(ans)