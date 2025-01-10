a=[]
b=[]
x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    a.append(m)
    b.append(n)
# a.sort()
# b.sort()

f=0
for i in range(x):
    if a[i]==b[i]:
        f=1
        break
if f:
    print("Poor Alex")
else:
    print("Happy Alex")