from collections import defaultdict
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a_dic=defaultdict(int)
b_dic=defaultdict(int)
for a in A:
  a_dic[a]+=1
  
for b in B:
  b_dic[b]+=1

for k,v in b_dic.items():
  if a_dic[k]<v:
    print('No')
    exit()
    
print('Yes')
exit()