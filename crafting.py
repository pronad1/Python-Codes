for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    surplus = 0
    deficit = 0

    for i in range(n):
        if a[i] > b[i]:
            surplus += a[i] - b[i]
        else:
            deficit += b[i] - a[i]
    
    print("YES" if surplus > deficit else "NO")