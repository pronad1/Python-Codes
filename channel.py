for _ in range(int(input())):
    n,a,q=map(int,input().split())
    n1=a1=q1=0
    for x in input():
        if x=='-':
            q1=q1+1
        else:
            n1+=1
            a1+=q1<1
            q1-=q1>0
    if n1<n-a:
        print("NO")
    elif a1>=n-a:
        print("YES")
    else:
        print("MAYBE")
    
