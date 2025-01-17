for i in range(int(input())):
    n,m=map(int,input().split())
    moves = [tuple(map(int, input().split())) for _ in range(n)]

    p=(4*m)*n

    for i in range(1,n):
        p-=2*((m-moves[i][0])+(m-moves[i][1]))
    
    print(p)


