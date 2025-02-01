import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    a.sort()
    cnt = [1]
    
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt[-1] += 1
        else:
            cnt.append(1)
    
    cnt.sort()
    m = len(cnt)
    
    for i in range(m - 1):
        if cnt[i] > k:
            print(m - i)
            return
        k -= cnt[i]
    
    print(1)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    solve()
