N,Q=map(int,input().split())
XQ=[int(input()) for _ in range(Q)]

pos_to_num={}
num_to_pos={}
for i in range(N):
  pos_to_num[i+1]=i+1
  num_to_pos[i+1]=i+1
for num in XQ:
  pos=num_to_pos[num]
  if pos==N:
    swap_pos=N-1
  else:
    swap_pos=pos+1
  swap_num=pos_to_num[swap_pos]
  num_to_pos[swap_num]=pos
  num_to_pos[num]=swap_pos
  pos_to_num[pos]=swap_num
  pos_to_num[swap_pos]=num
  
A=[pos_to_num[i+1] for i in range(N)]
print(*A)