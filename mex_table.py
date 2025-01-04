def calculate_max_mex_sum(n, m):
    min_dim = min(n, m)
    return (n + m - 1) * min_dim

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        results.append(calculate_max_mex_sum(n, m))
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
