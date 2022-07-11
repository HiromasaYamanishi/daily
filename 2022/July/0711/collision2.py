from collections import defaultdict
N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
S=str(input())

Y=defaultdict(list)
for i,(x,y) in enumerate(XY):
  Y[y].append((x,S[i]))
  
for k,v in Y.items():
  v.sort()
  flag=0
  for x,c in v:
    if c=="R":
      flag=1
    elif flag==1 and c=="L":
      print("Yes")
      exit()
print("No") 