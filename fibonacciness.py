t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

for a1, a2, a4, a5 in test_cases:
    possible_a3_values = [a4 - a2, a5 - a4]
    max_fib = 0
    for a3 in possible_a3_values:
        fib_count = 0
        if a3 == a1 + a2:
            fib_count += 1
        if a4 == a2 + a3:
            fib_count += 1
        if a5 == a3 + a4:
            fib_count += 1
        max_fib = max(max_fib, fib_count)
    print(max_fib)
