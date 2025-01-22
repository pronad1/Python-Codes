import sys
import math

t = int(input())
for _ in range(t):
    l, r = map(int,input().split())
    count = 0
    for i in range(l, r + 1):
        if math.gcd(i, i) == 1:
            count += 1
    print(count)