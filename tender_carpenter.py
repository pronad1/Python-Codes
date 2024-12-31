for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr[0]<arr[1]:
        print("YES")
    else:
        print("NO")