for _ in range(int(input())):
    n,k=map(int,input().split())
    p = list(range(k, 0, -1)) + list(range(k + 1, n + 1))
    print(" ".join(map(str, p)))