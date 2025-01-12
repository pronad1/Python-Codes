for i in range(int(input())):
    n,a,b=map(int,input().split())
    print("NO" if abs(a-b)%2==1 else "YES")