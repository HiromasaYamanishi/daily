#https://atcoder.jp/contests/abc259/tasks/abc259_c
S=input()
T=input()

def count_char(text):
  l=[]
  count=0
  for i,s in enumerate(text):
    if i==0:
      pre=s
      count=1
    elif i==len(text)-1:
      if s==pre:
      	l.append((pre,count+1))
      else:
        l.append((pre,count))
        l.append((s,1))
    else:
      if s!=pre:
        l.append((pre,count))
        pre=s
        count=1
      else:
        count+=1
  return l

S_chars=count_char(S)
T_chars=count_char(T)
if len(S_chars)!=len(T_chars):
  print("No")
  exit()
  
else:
  for sc,tc in zip(S_chars,T_chars):
    if sc[0]!=tc[0] or (sc[1]==1 and tc[1]!=1) or (sc[1]>tc[1]):
      print('No')
      exit()
      
print('Yes')