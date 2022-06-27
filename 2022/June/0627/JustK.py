N,K=map(int,input().split())
SN=[str(input()) for _ in range(N)]

ans = 0
for i in range(2**N):
    counter = [0]*26
    for j,S in enumerate(SN):
        if i&(1<<j):
            for s in S:
                counter[ord(s)-ord('a')] += 1
    ans = max(ans, counter.count(K))
print(ans)
