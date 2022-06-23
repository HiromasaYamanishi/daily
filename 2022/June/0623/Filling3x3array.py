#https://atcoder.jp/contests/abc252/tasks/abc252_c
h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0
for n1 in range(1,30):
  for n2 in range(1,30):
    for n4 in range(1,30):
      for n5 in range(1,30):
        n3=h1-n1-n2
        n6=h2-n4-n5
        n7=w1-n1-n4
        n8=w2-n2-n5
        n9=w3-n3-n6
        n9_=h3-n7-n8
        if n3>0 and n6>0 and n7>0 and n8>0 and n9>0 and (n9==n9_):
          ans+=1
          
print(ans)