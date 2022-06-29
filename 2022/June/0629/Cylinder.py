#https://atcoder.jp/contests/abc247/tasks/abc247_d
Q=int(input())
cylinder=[]
cursor=0
for _ in range(Q):
  query = list(map(int,input().split()))
  if query[0]==1:
    cylinder.append([query[1],query[2]])
  
  else:
    c=query[1]
    ans=0
    while c>0:
      get_num=min(c,cylinder[cursor][1])
      ans+=get_num*cylinder[cursor][0]
      c-=get_num
      cylinder[cursor][1]-=get_num
      if cylinder[cursor][1]==0:
        cursor+=1
    print(ans)