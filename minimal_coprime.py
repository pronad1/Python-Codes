import sys
import math

def count_minimal_coprime_segments(l, r):
    count = 0
    for i in range(l, r + 1):
        if math.gcd(i, i) == 1:
            count += 1
    return count

t = int(sys.stdin.readline().strip())
for _ in range(t):
    l, r = map(int, sys.stdin.readline().split())
    print(r - l + 1 - sum(1 for i in range(l, r + 1) if math.gcd(l, i) != 1))
