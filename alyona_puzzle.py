NT = int(input())

sqs = set()
k = 1
while k * k <= 100 * 1000:
	sqs.add(k * k)
	k += 2

for T in range(NT):
	n = int(input())
	a = list(map(int, input().split()))
	answer = 0
	cursum = 0
	for t in a:
		cursum += t
		if cursum in sqs:
			answer += 1
	print(answer)