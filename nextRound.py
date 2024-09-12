n, k = map(int, input().split())

scores = list(map(int, input().split()))

kscore = scores[k - 1]
advance = 0
for score in scores:
	if score >= kscore and score > 0:
		advance += 1
print(advance)
