a=[]
b=[]
f=0
x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    a.append(m)
    b.append(n)
    if m<n:
        f=1


if f:
    print("Happy Alex")
else:
    print("Poor Alex")
    